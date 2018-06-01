class MyClass:
    def __init__(self):
        print "Inside MyClass __init__"

_VideoFilenamePreviousFormat = "w%02d_z%02d%s"


class AnotherClass:
    one = MyClass()
    two = MyClass()

    def __init__(self):
        print "Inside AnotherClass __init__"


one = AnotherClass()
two = AnotherClass()

print "hi"

fileName = _VideoFilenamePreviousFormat % (16, 10, ".png")
print fileName


fileName = _VideoFilenamePreviousFormat % (16, 10, ".y800")
print fileName

fileName = _VideoFilenamePreviousFormat % (1, 1, ".y800")
print fileName

if True:
    print "true"
elif False:
    print false



