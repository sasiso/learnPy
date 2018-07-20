import sys
import glob
import serial
import serial.tools.list_ports


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)

            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def find_connected_boards(name_hint="OpenMV"):
    """
    Returns name of com ports where hint is part of port description
    :return: list of string representing com ports
    """
    ports = list(serial.tools.list_ports.comports())
    connected = []
    for p in ports:
        if name_hint in p[1]:
            connected.append(p[0])
    return connected


if __name__ == '__main__':
    print(find_connected_boards())
