import uuid
from http.client import HTTPConnection
from urllib.parse import urlencode

import requests
import serial
from urllib3 import HTTPConnectionPool

BASE_URL = 'http://127.0.0.1:7777/v0/'
API_CAPTURE_IMAGE = 'CaptureImage'


class SerialPort:

    def __init__(self):
        self.s = serial.Serial()
        self.s.baudrate = 400000
        self.s.port = 'COM13'
        self.s.set_buffer_size(rx_size=4096 * 2, tx_size=4096)
        self.s.open()

    def sendall(self, data):
        self.s.write(data=data)

    def close(self):
        pass

    def settimeout(self, read_timeout):
        # print ("Setting timeout to %d" % read_timeout)
        self.s.timeout = read_timeout
        pass

    def makefile(self, x):
        return self

    def readline(self, size):
        r = self.s.readline(size)
        return r

    def flush(self):
        pass

    def readinto(self, b):
        assert self.s.is_open
        return self.s.readinto(b)


class SerialConnection(HTTPConnection):

    def __init__(self, *args, **kw):
        super().__init__(host="127.0.0.1")

    def connect(self):
        """Connect to the host and port specified in __init__."""
        self.sock = SerialPort()


HTTPConnectionPool.ConnectionCls = SerialConnection
from PIL import ImageTk
from tkinter import *

root = Tk()
panel = Label(root)

count_lbl = Label(root, text="Hello", fg="blue",
                  bg="yellow", font="Verdana 10 bold")
count_lbl.pack()

text = Label(root, text="Hello", fg="blue",
             bg="yellow", font="Verdana 10 bold")
text.pack()


uuid_sent = Label(root, text="Hello", fg="blue",
                  bg="yellow", font="Verdana 10 bold")
uuid_sent.pack()

uuid_rcvd = Label(root, text="Hello", fg="blue",
                  bg="yellow", font="Verdana 10 bold")
uuid_rcvd.pack()
import random
count = 0
while True:
    r = None
    try:
        i = random.randint(1, 5000)
        params = {}
        params['exposure'] = str(int(i))
        params['uuid'] = str(uuid.uuid1())

        url = BASE_URL + API_CAPTURE_IMAGE + "?" + urlencode(params)
        r = requests.get(url, timeout=5)
        count +=1

        from PIL import Image

        l = len(r.content)
        print(l)
        import io

        img = Image.open(io.BytesIO(r.content))

        photoimg = ImageTk.PhotoImage(img)

        panel.configure(image=photoimg)
        panel.image = photoimg

        panel.pack(side="bottom", fill="both", expand="yes")

        text.configure(text=url)
        text.pack()

        count_lbl.configure(text= str(count))
        count_lbl.pack()


        uuid_sent.configure(text= params['uuid'])
        uuid_sent.pack()

        uuid_rcvd.configure(text=r.reason)
        uuid_rcvd.pack()

        text.configure(text=url)
        text.pack()

        root.update()
    except Exception as ex:
        print(ex)
        continue
