#!/usr/bin/env python
#
# Redirect data from a TCP/IP connection to a serial port and vice versa.
#
# (C) 2002-2016 Chris Liechti <cliechti@gmx.net>
#
# SPDX-License-Identifier:    BSD-3-Clause

import sys

import time
import asyncio
import asyncio.base_events
import serial_asyncio
import serial
import serial.tools.list_ports


class Server(asyncio.base_events.Server):
    """
    Override base asyncio Server with max_connections implementation from
    https://github.com/python/asyncio/pull/448
    max_connections default updated to 1
    """

    def __init__(self, loop, sockets, protocol_factory, ssl, backlog, max_connections=1):
        self._loop = loop
        self.sockets = sockets
        self._protocol_factory = protocol_factory
        self._ssl = ssl
        self._backlog = backlog
        self._max_connections = max_connections
        self._paused = False
        self._active_count = 0
        self._waiters = []

    def _attach(self):
        assert self.sockets is not None
        self._active_count += 1
        if self._max_connections is not None and \
           not self._paused and \
           self._active_count >= self._max_connections:
            self.pause()

    def _detach(self):
        assert self._active_count > 0
        self._active_count -= 1
        if self._active_count == 0 and self.sockets is None:
            self._wakeup()
        elif self._paused and self._max_connections is not None and \
             self._active_count < self._max_connections:
            self.resume()

    def pause(self):
        """Pause future calls to accept()."""
        assert not self._paused
        self._paused = True
        for sock in self.sockets:
            self._loop.remove_reader(sock.fileno())

    def resume(self):
        """Resume use of accept() on listening socket(s)."""
        assert self._paused
        self._paused = False
        for sock in self.sockets:
            self._loop._start_serving(self._protocol_factory, sock, self._ssl, self)

    def close(self):
        self._protocol_factory = None
        sockets = self.sockets
        if sockets is None:
            return
        self.sockets = None
        for sock in sockets:
            self._loop._stop_serving(sock)
        if self._active_count == 0:
            self._wakeup()


class Pipe(asyncio.Protocol):
    def __init__(self):
        self.other = None  # type: Pipe
        self.transport = None  # type: asyncio.Transport

    def register_other(self, other):
        self.other = other

    def connection_made(self, transport):
        self.transport = transport
        # print('port opened', transport)
        # transport.serial.rts = False  # You can manipulate Serial object via transport
        # transport.write(b'Hello, World!\n')  # Write serial data via transport

    def data_received(self, data):
        if self.other and self.other.transport:
            if self.other.__class__ is Serial and self.other.transport.is_closing():
                asyncio.get_event_loop().stop()

            self.other.transport.write(data)

            print(self.__class__.__name__, repr(data))

    def connection_lost(self, exc):
        print('%s port closed' % self.__class__.__name__)


class Serial(Pipe):
    def connection_lost(self, exc):
        print('%s port closed' % self.__class__.__name__)
        asyncio.get_event_loop().stop()


class TCP(Pipe):
    pass


if __name__ == '__main__':  # noqa
    import argparse

    parser = argparse.ArgumentParser(
        description='Simple Serial to Network (TCP/IP) redirector.',
        epilog="""\
NOTE: no security measures are implemented. Anyone can remotely connect
to this service over the network.
Only one connection at once is supported. When the connection is terminated
it waits for the next connect.
""")

    parser.add_argument(
        'SERIALPORT',
        help="serial port name")

    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='suppress non error messages',
        default=False)

    parser.add_argument(
        '--develop',
        action='store_true',
        help='Development mode, prints Python internals on errors',
        default=False)

    # group = parser.add_argument_group('serial port')


    group = parser.add_argument_group('network settings')

    exclusive_group = group.add_mutually_exclusive_group()

    exclusive_group.add_argument(
        '-P', '--localport',
        type=int,
        help='local TCP port',
        default=7777)

    exclusive_group.add_argument(
        '-c', '--client',
        metavar='HOST:PORT',
        help='make the connection as a client, instead of running a server',
        default=False)

    args = parser.parse_args()

    try:
        with serial.Serial(args.SERIALPORT) as _:
            serial_port = args.SERIALPORT
    except Exception as ex:
        ports = list(serial.tools.list_ports.grep(args.SERIALPORT))
        if not ports:
            raise
        serial_port = ports[0].device

    if not args.quiet:
        sys.stderr.write(
            '--- TCP/IP to Serial redirect on {serial_port} <-> 127.0.0.1:{args.localport} ---\n'
            '--- type Ctrl-C / BREAK to quit\n'.format(args=args, serial_port=serial_port))

    while True:
        ser_pipe = Serial()
        tcp_pipe = TCP()

        ser_pipe.register_other(tcp_pipe)
        tcp_pipe.register_other(ser_pipe)

        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        ser_coro = serial_asyncio.create_serial_connection(loop, lambda: ser_pipe, serial_port, baudrate=400000)

        asyncio.base_events.Server = lambda loop, sockets: Server(loop, sockets, lambda: tcp_pipe, ssl=None, backlog=100)
        tcp_coro = loop.create_server(lambda: tcp_pipe, '127.0.0.1', port=args.localport)
        try:
            loop.run_until_complete(asyncio.gather(ser_coro, tcp_coro))
            loop.run_forever()
        except Exception as ex:
            print(ex)
        loop.close()
        print("Restarting")
        time.sleep(1)

    sys.stderr.write('\n--- exit ---\n')
