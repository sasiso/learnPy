from concurrent.futures import ThreadPoolExecutor
from time import sleep
import sys
import serial
from serial.threaded import ReaderThread
from serial.threaded import Packetizer , FramedPacket
import time
import traceback

def read():
    data = b''
    print ("inside read")
    while s.is_open:
        data += s.read(s.in_waiting or 1)
        print(data)
    print("leaving read")


s = serial.Serial(port='COM12', timeout=1)
t = ThreadPoolExecutor(max_workers=1)


data = b'GET /send_json HTTP/1.1\r\nHost: 127.0.0.1:7777\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9,und;q=0.8,hi;q=0.7\r\n\r\n'
print(len(data))
print(s.write(data))

while True:
    buff = b''
    if s.in_waiting:
        buff += s.read(s.in_waiting or 1)
        if buff[-18:] == b'kinder_ends_serial':
            break

print((buff[:-18]))

