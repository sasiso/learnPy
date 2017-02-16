#abs()	

def demo_abs():
  # abs function returns absolute value of a number  
  b = -10
  print("absolute value of %d is %d" %(b,abs(b)))


#dict()	
#help()	
#min()	
#setattr()
#all()	
#dir()	
#hex()	
#next()	
#slice()
#any()	
#divmod()	
#id()	
#object()	
#sorted()
#ascii()	
#enumerate()	
#input()	
#oct()	
#staticmethod()
#bin()	
#eval()	
#int()	
#open()	
#str()
#bool()	
#exec()	
#isinstance()	
#ord()	
#sum()
#bytearray()
def demo_bytearray():
    """
    Return a new array of bytes. The bytearray type is a mutable sequence of integers in the range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods that the bytes type has, see Bytes and Byte Array Methods.

    The optional source parameter can be used to initialize the array in a few different ways:

    If it is a string, you must also give the encoding (and optionally, errors) parameters; bytearray() then converts the string to bytes using str.encode().
    If it is an integer, the array will have that size and will be initialized with null bytes.
    If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.
    If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial contents of the array.
    """
    l=[]
    for i in range(100):
      l.append(l)

    b = bytearray(str(l))
    print b
    for i in b:
      i += 1

    print b



#filter()	
#issubclass()	
#pow()	
#super()
#bytes()	
#float()	
#ter()	
#print()	
#tuple()
#callable()	
#format()	
#len()	
#property()	
#type()
#chr()	
#frozenset()	
#list()	
#range()	
#vars()
#classmethod()	
#getattr()	
#locals()	
#repr()	
#zip()
#compile()	
#globals()	
#map()	
#reversed()	
#__import__()
#complex()	
#hasattr()	
#max()	
#round()	 
#delattr()	
#hash()	
#memoryview()	
#set()	


demo_abs()
demo_bytearray()
