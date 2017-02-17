import datetime
import time

a = datetime.datetime.now()
time.sleep(5.02390)
b = datetime.datetime.now()


c = b - a
print str(c)
print c.seconds
print c.microseconds
