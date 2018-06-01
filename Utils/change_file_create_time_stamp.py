import os
from time import sleep
import multiprocessing
import dateutil
import datetime
from datetime import timedelta

import pywintypes, win32file, win32con
def changeFileCreationTime(fname, newtime):
    wintime = pywintypes.Time(newtime)
    winfile = win32file.CreateFile(
        fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None)

    win32file.SetFileTime(winfile, wintime, None, None)

    winfile.close()


for root, dirs, files in os.walk("C:\\Users\\Geri\\AppData\\Local\\Temp"):
    for filename in files:
        print(filename)
        now = datetime.datetime.now()
        d = now - timedelta(days=2)

        full_path = os.path.join(root, filename)
        changeFileCreationTime(full_path, d)