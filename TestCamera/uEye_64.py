###############################################################
# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
#   Copyright (c) 2015, Planet Innovation
#   436 Elgar Road, Box Hill VIC 3128 Australia
#   Phone: +61 3 9945 7510
#
#   The copyright to the computer program(s) herein is the property of
#   Planet Innovation, Australia.
#   The program(s) may be used and/or copied only with the written permission
#   of Planet Innovation or in accordance with the terms and conditions
#   stipulated in the agreement/contract under which the program(s) have been
#   supplied.
#
#   @file
#   @brief uEye Camera driver interface.
#
#

'''Wrapper for uEye.h

Generated with:
E:\pi\129_Burton_Trunk\04_Software\Workspaces\BurtonInstrument\workspace\utils\virtualenvs\burton_amd64\Scripts\ctypesgen.py --cpp=clang -m64 -E -lueye_api_64 uEye.h -o uEye_64_gen.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                dll_in_file_dir = os.path.join(os.path.dirname(__file__), name % libname)
                if os.path.exists(dll_in_file_dir):
                    yield dll_in_file_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["ueye_api_64"] = load_library("ueye_api_64")

# 1 libraries
# End libraries

# No modules

DWORD = c_ulong # /mingw/include\\windef.h: 229

WINBOOL = c_int # /mingw/include\\windef.h: 230

BOOL = WINBOOL # /mingw/include\\windef.h: 234

BYTE = c_ubyte # /mingw/include\\windef.h: 238

WORD = c_ushort # /mingw/include\\windef.h: 241

INT = c_int # /mingw/include\\windef.h: 250

UINT = c_uint # /mingw/include\\windef.h: 251

CHAR = c_char # /mingw/include\\winnt.h: 77

ULONG = c_ulong # /mingw/include\\winnt.h: 83

HANDLE = POINTER(None) # /mingw/include\\winnt.h: 148

# /mingw/include\\windef.h: 275
class struct_HDC__(Structure):
    pass

struct_HDC__.__slots__ = [
    'i',
]
struct_HDC__._fields_ = [
    ('i', c_int),
]

HDC = POINTER(struct_HDC__) # /mingw/include\\windef.h: 275

# /mingw/include\\windef.h: 299
class struct_HWND__(Structure):
    pass

struct_HWND__.__slots__ = [
    'i',
]
struct_HWND__._fields_ = [
    ('i', c_int),
]

HWND = POINTER(struct_HWND__) # /mingw/include\\windef.h: 299

IS_CHAR = c_char # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1747

HIDS = DWORD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1754

HCAM = DWORD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1757

HFALC = DWORD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1760

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1789
class struct_anon_204(Structure):
    pass

struct_anon_204.__slots__ = [
    'SerNo',
    'ID',
    'Version',
    'Date',
    'Select',
    'Type',
    'Reserved',
]
struct_anon_204._fields_ = [
    ('SerNo', c_char * 12),
    ('ID', c_char * 20),
    ('Version', c_char * 10),
    ('Date', c_char * 12),
    ('Select', c_ubyte),
    ('Type', c_ubyte),
    ('Reserved', c_char * 8),
]

BOARDINFO = struct_anon_204 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1789

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1780
class struct_anon_205(Structure):
    pass

struct_anon_205.__slots__ = [
    'SerNo',
    'ID',
    'Version',
    'Date',
    'Select',
    'Type',
    'Reserved',
]
struct_anon_205._fields_ = [
    ('SerNo', c_char * 12),
    ('ID', c_char * 20),
    ('Version', c_char * 10),
    ('Date', c_char * 12),
    ('Select', c_ubyte),
    ('Type', c_ubyte),
    ('Reserved', c_char * 8),
]

PBOARDINFO = POINTER(struct_anon_205) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1789

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1807
class struct__SENSORINFO(Structure):
    pass

struct__SENSORINFO.__slots__ = [
    'SensorID',
    'strSensorName',
    'nColorMode',
    'nMaxWidth',
    'nMaxHeight',
    'bMasterGain',
    'bRGain',
    'bGGain',
    'bBGain',
    'bGlobShutter',
    'wPixelSize',
    'nUpperLeftBayerPixel',
    'Reserved',
]
struct__SENSORINFO._fields_ = [
    ('SensorID', WORD),
    ('strSensorName', IS_CHAR * 32),
    ('nColorMode', c_char),
    ('nMaxWidth', DWORD),
    ('nMaxHeight', DWORD),
    ('bMasterGain', BOOL),
    ('bRGain', BOOL),
    ('bGGain', BOOL),
    ('bBGain', BOOL),
    ('bGlobShutter', BOOL),
    ('wPixelSize', WORD),
    ('nUpperLeftBayerPixel', c_char),
    ('Reserved', c_char * 13),
]

SENSORINFO = struct__SENSORINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1807

PSENSORINFO = POINTER(struct__SENSORINFO) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1807

enum__BAYER_PIXEL = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1816

BAYER_PIXEL_RED = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1816

BAYER_PIXEL_GREEN = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1816

BAYER_PIXEL_BLUE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1816

BAYER_PIXEL = enum__BAYER_PIXEL # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1816

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1841
class struct__REVISIONINFO(Structure):
    pass

struct__REVISIONINFO.__slots__ = [
    'size',
    'Sensor',
    'Cypress',
    'Blackfin',
    'DspFirmware',
    'USB_Board',
    'Sensor_Board',
    'Processing_Board',
    'Memory_Board',
    'Housing',
    'Filter',
    'Timing_Board',
    'Product',
    'Power_Board',
    'Logic_Board',
    'FX3',
    'FPGA',
    'reserved',
]
struct__REVISIONINFO._fields_ = [
    ('size', WORD),
    ('Sensor', WORD),
    ('Cypress', WORD),
    ('Blackfin', DWORD),
    ('DspFirmware', WORD),
    ('USB_Board', WORD),
    ('Sensor_Board', WORD),
    ('Processing_Board', WORD),
    ('Memory_Board', WORD),
    ('Housing', WORD),
    ('Filter', WORD),
    ('Timing_Board', WORD),
    ('Product', WORD),
    ('Power_Board', WORD),
    ('Logic_Board', WORD),
    ('FX3', WORD),
    ('FPGA', WORD),
    ('reserved', BYTE * 92),
]

REVISIONINFO = struct__REVISIONINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1841

PREVISIONINFO = POINTER(struct__REVISIONINFO) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1841

enum__UEYE_CAPTURE_STATUS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

IS_CAP_STATUS_API_NO_DEST_MEM = 162 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

IS_CAP_STATUS_API_CONVERSION_FAILED = 163 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

IS_CAP_STATUS_API_IMAGE_LOCKED = 165 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

IS_CAP_STATUS_DRV_OUT_OF_BUFFERS = 178 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

IS_CAP_STATUS_DRV_DEVICE_NOT_READY = 180 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

IS_CAP_STATUS_USB_TRANSFER_FAILED = 199 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

IS_CAP_STATUS_DEV_TIMEOUT = 214 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

IS_CAP_STATUS_ETH_BUFFER_OVERRUN = 228 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

IS_CAP_STATUS_ETH_MISSED_IMAGES = 229 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

UEYE_CAPTURE_STATUS = enum__UEYE_CAPTURE_STATUS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1863

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1872
class struct__UEYE_CAPTURE_STATUS_INFO(Structure):
    pass

struct__UEYE_CAPTURE_STATUS_INFO.__slots__ = [
    'dwCapStatusCnt_Total',
    'reserved',
    'adwCapStatusCnt_Detail',
]
struct__UEYE_CAPTURE_STATUS_INFO._fields_ = [
    ('dwCapStatusCnt_Total', DWORD),
    ('reserved', BYTE * 60),
    ('adwCapStatusCnt_Detail', DWORD * 256),
]

UEYE_CAPTURE_STATUS_INFO = struct__UEYE_CAPTURE_STATUS_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1872

enum_E_CAPTURE_STATUS_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1880

IS_CAPTURE_STATUS_INFO_CMD_RESET = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1880

IS_CAPTURE_STATUS_INFO_CMD_GET = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1880

CAPTURE_STATUS_CMD = enum_E_CAPTURE_STATUS_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1880

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1883
if hasattr(_libs['ueye_api_64'], 'is_CaptureStatus'):
    is_CaptureStatus = _libs['ueye_api_64'].is_CaptureStatus
    is_CaptureStatus.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_CaptureStatus.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1902
class struct__UEYE_CAMERA_INFO(Structure):
    pass

struct__UEYE_CAMERA_INFO.__slots__ = [
    'dwCameraID',
    'dwDeviceID',
    'dwSensorID',
    'dwInUse',
    'SerNo',
    'Model',
    'dwStatus',
    'dwReserved',
    'FullModelName',
    'dwReserved2',
]
struct__UEYE_CAMERA_INFO._fields_ = [
    ('dwCameraID', DWORD),
    ('dwDeviceID', DWORD),
    ('dwSensorID', DWORD),
    ('dwInUse', DWORD),
    ('SerNo', IS_CHAR * 16),
    ('Model', IS_CHAR * 16),
    ('dwStatus', DWORD),
    ('dwReserved', DWORD * 2),
    ('FullModelName', IS_CHAR * 32),
    ('dwReserved2', DWORD * 5),
]

UEYE_CAMERA_INFO = struct__UEYE_CAMERA_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1902

PUEYE_CAMERA_INFO = POINTER(struct__UEYE_CAMERA_INFO) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1902

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1921
class struct__UEYE_CAMERA_LIST(Structure):
    pass

struct__UEYE_CAMERA_LIST.__slots__ = [
    'dwCount',
    'uci',
]
struct__UEYE_CAMERA_LIST._fields_ = [
    ('dwCount', ULONG),
    ('uci', UEYE_CAMERA_INFO * 1),
]

UEYE_CAMERA_LIST = struct__UEYE_CAMERA_LIST # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1921

PUEYE_CAMERA_LIST = POINTER(struct__UEYE_CAMERA_LIST) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1921

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1975
class struct__AUTO_BRIGHT_STATUS(Structure):
    pass

struct__AUTO_BRIGHT_STATUS.__slots__ = [
    'curValue',
    'curError',
    'curController',
    'curCtrlStatus',
]
struct__AUTO_BRIGHT_STATUS._fields_ = [
    ('curValue', DWORD),
    ('curError', c_long),
    ('curController', DWORD),
    ('curCtrlStatus', DWORD),
]

AUTO_BRIGHT_STATUS = struct__AUTO_BRIGHT_STATUS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1975

PAUTO_BRIGHT_STATUS = POINTER(struct__AUTO_BRIGHT_STATUS) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1975

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1984
class struct__AUTO_WB_CHANNNEL_STATUS(Structure):
    pass

struct__AUTO_WB_CHANNNEL_STATUS.__slots__ = [
    'curValue',
    'curError',
    'curCtrlStatus',
]
struct__AUTO_WB_CHANNNEL_STATUS._fields_ = [
    ('curValue', DWORD),
    ('curError', c_long),
    ('curCtrlStatus', DWORD),
]

AUTO_WB_CHANNNEL_STATUS = struct__AUTO_WB_CHANNNEL_STATUS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1984

PAUTO_WB_CHANNNEL_STATUS = POINTER(struct__AUTO_WB_CHANNNEL_STATUS) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1984

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1992
class struct__AUTO_WB_STATUS(Structure):
    pass

struct__AUTO_WB_STATUS.__slots__ = [
    'RedChannel',
    'GreenChannel',
    'BlueChannel',
    'curController',
]
struct__AUTO_WB_STATUS._fields_ = [
    ('RedChannel', AUTO_WB_CHANNNEL_STATUS),
    ('GreenChannel', AUTO_WB_CHANNNEL_STATUS),
    ('BlueChannel', AUTO_WB_CHANNNEL_STATUS),
    ('curController', DWORD),
]

AUTO_WB_STATUS = struct__AUTO_WB_STATUS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1992

PAUTO_WB_STATUS = POINTER(struct__AUTO_WB_STATUS) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1992

enum_E_AUTO_SHUTTER_PHOTOM = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2004

AS_PM_NONE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2004

AS_PM_SENS_CENTER_WEIGHTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2004

AS_PM_SENS_CENTER_SPOT = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2004

AS_PM_SENS_PORTRAIT = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2004

AS_PM_SENS_LANDSCAPE = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2004

AS_PM_SENS_CENTER_AVERAGE = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2004

AUTO_SHUTTER_PHOTOM = enum_E_AUTO_SHUTTER_PHOTOM # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2004

enum_E_AUTO_GAIN_PHOTOM = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2014

AG_PM_NONE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2014

AG_PM_SENS_CENTER_WEIGHTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2014

AG_PM_SENS_CENTER_SPOT = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2014

AG_PM_SENS_PORTRAIT = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2014

AG_PM_SENS_LANDSCAPE = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2014

AUTO_GAIN_PHOTOM = enum_E_AUTO_GAIN_PHOTOM # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2014

enum_E_ANTI_FLICKER_MODE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2023

ANTIFLCK_MODE_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2023

ANTIFLCK_MODE_SENS_AUTO = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2023

ANTIFLCK_MODE_SENS_50_FIXED = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2023

ANTIFLCK_MODE_SENS_60_FIXED = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2023

ANTI_FLICKER_MODE = enum_E_ANTI_FLICKER_MODE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2023

enum_E_WHITEBALANCE_MODE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

WB_MODE_DISABLE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

WB_MODE_AUTO = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

WB_MODE_ALL_PULLIN = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

WB_MODE_INCANDESCENT_LAMP = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

WB_MODE_FLUORESCENT_DL = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

WB_MODE_OUTDOOR_CLEAR_SKY = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

WB_MODE_OUTDOOR_CLOUDY = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

WB_MODE_FLUORESCENT_LAMP = 64 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

WB_MODE_FLUORESCENT_NL = 128 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

WHITEBALANCE_MODE = enum_E_WHITEBALANCE_MODE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2038

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2050
class struct__UEYE_AUTO_INFO(Structure):
    pass

struct__UEYE_AUTO_INFO.__slots__ = [
    'AutoAbility',
    'sBrightCtrlStatus',
    'sWBCtrlStatus',
    'AShutterPhotomCaps',
    'AGainPhotomCaps',
    'AAntiFlickerCaps',
    'SensorWBModeCaps',
    'reserved',
]
struct__UEYE_AUTO_INFO._fields_ = [
    ('AutoAbility', DWORD),
    ('sBrightCtrlStatus', AUTO_BRIGHT_STATUS),
    ('sWBCtrlStatus', AUTO_WB_STATUS),
    ('AShutterPhotomCaps', DWORD),
    ('AGainPhotomCaps', DWORD),
    ('AAntiFlickerCaps', DWORD),
    ('SensorWBModeCaps', DWORD),
    ('reserved', DWORD * 8),
]

UEYE_AUTO_INFO = struct__UEYE_AUTO_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2050

PUEYE_AUTO_INFO = POINTER(struct__UEYE_AUTO_INFO) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2050

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2058
class struct__DC_INFO(Structure):
    pass

struct__DC_INFO.__slots__ = [
    'nSize',
    'hDC',
    'nCx',
    'nCy',
]
struct__DC_INFO._fields_ = [
    ('nSize', c_uint),
    ('hDC', HDC),
    ('nCx', c_uint),
    ('nCy', c_uint),
]

DC_INFO = struct__DC_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2058

PDC_INFO = POINTER(struct__DC_INFO) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2058

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2069
if hasattr(_libs['ueye_api_64'], 'is_SetSaturation'):
    is_SetSaturation = _libs['ueye_api_64'].is_SetSaturation
    is_SetSaturation.argtypes = [HIDS, INT, INT]
    is_SetSaturation.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2070
if hasattr(_libs['ueye_api_64'], 'is_PrepareStealVideo'):
    is_PrepareStealVideo = _libs['ueye_api_64'].is_PrepareStealVideo
    is_PrepareStealVideo.argtypes = [HIDS, c_int, ULONG]
    is_PrepareStealVideo.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2071
if hasattr(_libs['ueye_api_64'], 'is_GetNumberOfDevices'):
    is_GetNumberOfDevices = _libs['ueye_api_64'].is_GetNumberOfDevices
    is_GetNumberOfDevices.argtypes = []
    is_GetNumberOfDevices.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2077
if hasattr(_libs['ueye_api_64'], 'is_StopLiveVideo'):
    is_StopLiveVideo = _libs['ueye_api_64'].is_StopLiveVideo
    is_StopLiveVideo.argtypes = [HIDS, INT]
    is_StopLiveVideo.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2078
if hasattr(_libs['ueye_api_64'], 'is_FreezeVideo'):
    is_FreezeVideo = _libs['ueye_api_64'].is_FreezeVideo
    is_FreezeVideo.argtypes = [HIDS, INT]
    is_FreezeVideo.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2079
if hasattr(_libs['ueye_api_64'], 'is_CaptureVideo'):
    is_CaptureVideo = _libs['ueye_api_64'].is_CaptureVideo
    is_CaptureVideo.argtypes = [HIDS, INT]
    is_CaptureVideo.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2080
if hasattr(_libs['ueye_api_64'], 'is_IsVideoFinish'):
    is_IsVideoFinish = _libs['ueye_api_64'].is_IsVideoFinish
    is_IsVideoFinish.argtypes = [HIDS, POINTER(INT)]
    is_IsVideoFinish.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2081
if hasattr(_libs['ueye_api_64'], 'is_HasVideoStarted'):
    is_HasVideoStarted = _libs['ueye_api_64'].is_HasVideoStarted
    is_HasVideoStarted.argtypes = [HIDS, POINTER(BOOL)]
    is_HasVideoStarted.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2083
if hasattr(_libs['ueye_api_64'], 'is_AllocImageMem'):
    is_AllocImageMem = _libs['ueye_api_64'].is_AllocImageMem
    is_AllocImageMem.argtypes = [HIDS, INT, INT, INT, POINTER(POINTER(c_char)), POINTER(c_int)]
    is_AllocImageMem.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2084
if hasattr(_libs['ueye_api_64'], 'is_SetImageMem'):
    is_SetImageMem = _libs['ueye_api_64'].is_SetImageMem
    is_SetImageMem.argtypes = [HIDS, String, c_int]
    is_SetImageMem.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2085
if hasattr(_libs['ueye_api_64'], 'is_FreeImageMem'):
    is_FreeImageMem = _libs['ueye_api_64'].is_FreeImageMem
    is_FreeImageMem.argtypes = [HIDS, String, c_int]
    is_FreeImageMem.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2086
if hasattr(_libs['ueye_api_64'], 'is_GetImageMem'):
    is_GetImageMem = _libs['ueye_api_64'].is_GetImageMem
    is_GetImageMem.argtypes = [HIDS, POINTER(POINTER(None))]
    is_GetImageMem.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2087
if hasattr(_libs['ueye_api_64'], 'is_GetActiveImageMem'):
    is_GetActiveImageMem = _libs['ueye_api_64'].is_GetActiveImageMem
    is_GetActiveImageMem.argtypes = [HIDS, POINTER(POINTER(c_char)), POINTER(c_int)]
    is_GetActiveImageMem.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2088
if hasattr(_libs['ueye_api_64'], 'is_InquireImageMem'):
    is_InquireImageMem = _libs['ueye_api_64'].is_InquireImageMem
    is_InquireImageMem.argtypes = [HIDS, String, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    is_InquireImageMem.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2089
if hasattr(_libs['ueye_api_64'], 'is_GetImageMemPitch'):
    is_GetImageMemPitch = _libs['ueye_api_64'].is_GetImageMemPitch
    is_GetImageMemPitch.argtypes = [HIDS, POINTER(INT)]
    is_GetImageMemPitch.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2091
if hasattr(_libs['ueye_api_64'], 'is_SetAllocatedImageMem'):
    is_SetAllocatedImageMem = _libs['ueye_api_64'].is_SetAllocatedImageMem
    is_SetAllocatedImageMem.argtypes = [HIDS, INT, INT, INT, String, POINTER(c_int)]
    is_SetAllocatedImageMem.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2092
if hasattr(_libs['ueye_api_64'], 'is_CopyImageMem'):
    is_CopyImageMem = _libs['ueye_api_64'].is_CopyImageMem
    is_CopyImageMem.argtypes = [HIDS, String, c_int, String]
    is_CopyImageMem.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2093
if hasattr(_libs['ueye_api_64'], 'is_CopyImageMemLines'):
    is_CopyImageMemLines = _libs['ueye_api_64'].is_CopyImageMemLines
    is_CopyImageMemLines.argtypes = [HIDS, String, c_int, c_int, String]
    is_CopyImageMemLines.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2095
if hasattr(_libs['ueye_api_64'], 'is_AddToSequence'):
    is_AddToSequence = _libs['ueye_api_64'].is_AddToSequence
    is_AddToSequence.argtypes = [HIDS, String, INT]
    is_AddToSequence.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2096
if hasattr(_libs['ueye_api_64'], 'is_ClearSequence'):
    is_ClearSequence = _libs['ueye_api_64'].is_ClearSequence
    is_ClearSequence.argtypes = [HIDS]
    is_ClearSequence.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2097
if hasattr(_libs['ueye_api_64'], 'is_GetActSeqBuf'):
    is_GetActSeqBuf = _libs['ueye_api_64'].is_GetActSeqBuf
    is_GetActSeqBuf.argtypes = [HIDS, POINTER(INT), POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    is_GetActSeqBuf.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2098
if hasattr(_libs['ueye_api_64'], 'is_LockSeqBuf'):
    is_LockSeqBuf = _libs['ueye_api_64'].is_LockSeqBuf
    is_LockSeqBuf.argtypes = [HIDS, INT, String]
    is_LockSeqBuf.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2099
if hasattr(_libs['ueye_api_64'], 'is_UnlockSeqBuf'):
    is_UnlockSeqBuf = _libs['ueye_api_64'].is_UnlockSeqBuf
    is_UnlockSeqBuf.argtypes = [HIDS, INT, String]
    is_UnlockSeqBuf.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2101
if hasattr(_libs['ueye_api_64'], 'is_GetError'):
    is_GetError = _libs['ueye_api_64'].is_GetError
    is_GetError.argtypes = [HIDS, POINTER(INT), POINTER(POINTER(IS_CHAR))]
    is_GetError.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2102
if hasattr(_libs['ueye_api_64'], 'is_SetErrorReport'):
    is_SetErrorReport = _libs['ueye_api_64'].is_SetErrorReport
    is_SetErrorReport.argtypes = [HIDS, INT]
    is_SetErrorReport.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2104
if hasattr(_libs['ueye_api_64'], 'is_ReadEEPROM'):
    is_ReadEEPROM = _libs['ueye_api_64'].is_ReadEEPROM
    is_ReadEEPROM.argtypes = [HIDS, INT, String, INT]
    is_ReadEEPROM.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2105
if hasattr(_libs['ueye_api_64'], 'is_WriteEEPROM'):
    is_WriteEEPROM = _libs['ueye_api_64'].is_WriteEEPROM
    is_WriteEEPROM.argtypes = [HIDS, INT, String, INT]
    is_WriteEEPROM.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2107
if hasattr(_libs['ueye_api_64'], 'is_SetColorMode'):
    is_SetColorMode = _libs['ueye_api_64'].is_SetColorMode
    is_SetColorMode.argtypes = [HIDS, INT]
    is_SetColorMode.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2108
if hasattr(_libs['ueye_api_64'], 'is_GetColorDepth'):
    is_GetColorDepth = _libs['ueye_api_64'].is_GetColorDepth
    is_GetColorDepth.argtypes = [HIDS, POINTER(INT), POINTER(INT)]
    is_GetColorDepth.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2111
if hasattr(_libs['ueye_api_64'], 'is_RenderBitmap'):
    is_RenderBitmap = _libs['ueye_api_64'].is_RenderBitmap
    is_RenderBitmap.argtypes = [HIDS, INT, HWND, INT]
    is_RenderBitmap.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2113
if hasattr(_libs['ueye_api_64'], 'is_SetDisplayMode'):
    is_SetDisplayMode = _libs['ueye_api_64'].is_SetDisplayMode
    is_SetDisplayMode.argtypes = [HIDS, INT]
    is_SetDisplayMode.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2114
if hasattr(_libs['ueye_api_64'], 'is_SetDisplayPos'):
    is_SetDisplayPos = _libs['ueye_api_64'].is_SetDisplayPos
    is_SetDisplayPos.argtypes = [HIDS, INT, INT]
    is_SetDisplayPos.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2116
if hasattr(_libs['ueye_api_64'], 'is_SetHwnd'):
    is_SetHwnd = _libs['ueye_api_64'].is_SetHwnd
    is_SetHwnd.argtypes = [HIDS, HWND]
    is_SetHwnd.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2118
if hasattr(_libs['ueye_api_64'], 'is_GetVsyncCount'):
    is_GetVsyncCount = _libs['ueye_api_64'].is_GetVsyncCount
    is_GetVsyncCount.argtypes = [HIDS, POINTER(c_long), POINTER(c_long)]
    is_GetVsyncCount.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2121
if hasattr(_libs['ueye_api_64'], 'is_GetDLLVersion'):
    is_GetDLLVersion = _libs['ueye_api_64'].is_GetDLLVersion
    is_GetDLLVersion.argtypes = []
    is_GetDLLVersion.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2123
if hasattr(_libs['ueye_api_64'], 'is_InitEvent'):
    is_InitEvent = _libs['ueye_api_64'].is_InitEvent
    is_InitEvent.argtypes = [HIDS, HANDLE, INT]
    is_InitEvent.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2124
if hasattr(_libs['ueye_api_64'], 'is_ExitEvent'):
    is_ExitEvent = _libs['ueye_api_64'].is_ExitEvent
    is_ExitEvent.argtypes = [HIDS, INT]
    is_ExitEvent.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2125
if hasattr(_libs['ueye_api_64'], 'is_EnableEvent'):
    is_EnableEvent = _libs['ueye_api_64'].is_EnableEvent
    is_EnableEvent.argtypes = [HIDS, INT]
    is_EnableEvent.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2126
if hasattr(_libs['ueye_api_64'], 'is_DisableEvent'):
    is_DisableEvent = _libs['ueye_api_64'].is_DisableEvent
    is_DisableEvent.argtypes = [HIDS, INT]
    is_DisableEvent.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2128
if hasattr(_libs['ueye_api_64'], 'is_SetExternalTrigger'):
    is_SetExternalTrigger = _libs['ueye_api_64'].is_SetExternalTrigger
    is_SetExternalTrigger.argtypes = [HIDS, INT]
    is_SetExternalTrigger.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2129
if hasattr(_libs['ueye_api_64'], 'is_SetTriggerCounter'):
    is_SetTriggerCounter = _libs['ueye_api_64'].is_SetTriggerCounter
    is_SetTriggerCounter.argtypes = [HIDS, INT]
    is_SetTriggerCounter.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2130
if hasattr(_libs['ueye_api_64'], 'is_SetRopEffect'):
    is_SetRopEffect = _libs['ueye_api_64'].is_SetRopEffect
    is_SetRopEffect.argtypes = [HIDS, INT, INT, INT]
    is_SetRopEffect.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2134
if hasattr(_libs['ueye_api_64'], 'is_InitCamera'):
    is_InitCamera = _libs['ueye_api_64'].is_InitCamera
    is_InitCamera.argtypes = [POINTER(HIDS), HWND]
    is_InitCamera.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2135
if hasattr(_libs['ueye_api_64'], 'is_ExitCamera'):
    is_ExitCamera = _libs['ueye_api_64'].is_ExitCamera
    is_ExitCamera.argtypes = [HIDS]
    is_ExitCamera.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2136
if hasattr(_libs['ueye_api_64'], 'is_GetCameraInfo'):
    is_GetCameraInfo = _libs['ueye_api_64'].is_GetCameraInfo
    is_GetCameraInfo.argtypes = [HIDS, PBOARDINFO]
    is_GetCameraInfo.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2137
if hasattr(_libs['ueye_api_64'], 'is_CameraStatus'):
    is_CameraStatus = _libs['ueye_api_64'].is_CameraStatus
    is_CameraStatus.argtypes = [HIDS, INT, ULONG]
    is_CameraStatus.restype = ULONG

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2138
if hasattr(_libs['ueye_api_64'], 'is_GetCameraType'):
    is_GetCameraType = _libs['ueye_api_64'].is_GetCameraType
    is_GetCameraType.argtypes = [HIDS]
    is_GetCameraType.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2139
if hasattr(_libs['ueye_api_64'], 'is_GetNumberOfCameras'):
    is_GetNumberOfCameras = _libs['ueye_api_64'].is_GetNumberOfCameras
    is_GetNumberOfCameras.argtypes = [POINTER(INT)]
    is_GetNumberOfCameras.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2141
if hasattr(_libs['ueye_api_64'], 'is_GetUsedBandwidth'):
    is_GetUsedBandwidth = _libs['ueye_api_64'].is_GetUsedBandwidth
    is_GetUsedBandwidth.argtypes = [HIDS]
    is_GetUsedBandwidth.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2144
if hasattr(_libs['ueye_api_64'], 'is_GetFrameTimeRange'):
    is_GetFrameTimeRange = _libs['ueye_api_64'].is_GetFrameTimeRange
    is_GetFrameTimeRange.argtypes = [HIDS, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    is_GetFrameTimeRange.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2145
if hasattr(_libs['ueye_api_64'], 'is_SetFrameRate'):
    is_SetFrameRate = _libs['ueye_api_64'].is_SetFrameRate
    is_SetFrameRate.argtypes = [HIDS, c_double, POINTER(c_double)]
    is_SetFrameRate.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2148
if hasattr(_libs['ueye_api_64'], 'is_GetFramesPerSecond'):
    is_GetFramesPerSecond = _libs['ueye_api_64'].is_GetFramesPerSecond
    is_GetFramesPerSecond.argtypes = [HIDS, POINTER(c_double)]
    is_GetFramesPerSecond.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2151
if hasattr(_libs['ueye_api_64'], 'is_GetSensorInfo'):
    is_GetSensorInfo = _libs['ueye_api_64'].is_GetSensorInfo
    is_GetSensorInfo.argtypes = [HIDS, PSENSORINFO]
    is_GetSensorInfo.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2154
if hasattr(_libs['ueye_api_64'], 'is_GetRevisionInfo'):
    is_GetRevisionInfo = _libs['ueye_api_64'].is_GetRevisionInfo
    is_GetRevisionInfo.argtypes = [HIDS, PREVISIONINFO]
    is_GetRevisionInfo.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2157
if hasattr(_libs['ueye_api_64'], 'is_EnableAutoExit'):
    is_EnableAutoExit = _libs['ueye_api_64'].is_EnableAutoExit
    is_EnableAutoExit.argtypes = [HIDS, INT]
    is_EnableAutoExit.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2160
if hasattr(_libs['ueye_api_64'], 'is_EnableMessage'):
    is_EnableMessage = _libs['ueye_api_64'].is_EnableMessage
    is_EnableMessage.argtypes = [HIDS, INT, HWND]
    is_EnableMessage.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2163
if hasattr(_libs['ueye_api_64'], 'is_SetHardwareGain'):
    is_SetHardwareGain = _libs['ueye_api_64'].is_SetHardwareGain
    is_SetHardwareGain.argtypes = [HIDS, INT, INT, INT, INT]
    is_SetHardwareGain.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2166
if hasattr(_libs['ueye_api_64'], 'is_SetWhiteBalance'):
    is_SetWhiteBalance = _libs['ueye_api_64'].is_SetWhiteBalance
    is_SetWhiteBalance.argtypes = [HIDS, INT]
    is_SetWhiteBalance.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2167
if hasattr(_libs['ueye_api_64'], 'is_SetWhiteBalanceMultipliers'):
    is_SetWhiteBalanceMultipliers = _libs['ueye_api_64'].is_SetWhiteBalanceMultipliers
    is_SetWhiteBalanceMultipliers.argtypes = [HIDS, c_double, c_double, c_double]
    is_SetWhiteBalanceMultipliers.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2168
if hasattr(_libs['ueye_api_64'], 'is_GetWhiteBalanceMultipliers'):
    is_GetWhiteBalanceMultipliers = _libs['ueye_api_64'].is_GetWhiteBalanceMultipliers
    is_GetWhiteBalanceMultipliers.argtypes = [HIDS, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    is_GetWhiteBalanceMultipliers.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2171
if hasattr(_libs['ueye_api_64'], 'is_SetColorCorrection'):
    is_SetColorCorrection = _libs['ueye_api_64'].is_SetColorCorrection
    is_SetColorCorrection.argtypes = [HIDS, INT, POINTER(c_double)]
    is_SetColorCorrection.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2173
if hasattr(_libs['ueye_api_64'], 'is_SetSubSampling'):
    is_SetSubSampling = _libs['ueye_api_64'].is_SetSubSampling
    is_SetSubSampling.argtypes = [HIDS, INT]
    is_SetSubSampling.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2174
if hasattr(_libs['ueye_api_64'], 'is_ForceTrigger'):
    is_ForceTrigger = _libs['ueye_api_64'].is_ForceTrigger
    is_ForceTrigger.argtypes = [HIDS]
    is_ForceTrigger.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2177
if hasattr(_libs['ueye_api_64'], 'is_GetBusSpeed'):
    is_GetBusSpeed = _libs['ueye_api_64'].is_GetBusSpeed
    is_GetBusSpeed.argtypes = [HIDS]
    is_GetBusSpeed.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2180
if hasattr(_libs['ueye_api_64'], 'is_SetBinning'):
    is_SetBinning = _libs['ueye_api_64'].is_SetBinning
    is_SetBinning.argtypes = [HIDS, INT]
    is_SetBinning.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2183
if hasattr(_libs['ueye_api_64'], 'is_ResetToDefault'):
    is_ResetToDefault = _libs['ueye_api_64'].is_ResetToDefault
    is_ResetToDefault.argtypes = [HIDS]
    is_ResetToDefault.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2186
if hasattr(_libs['ueye_api_64'], 'is_SetCameraID'):
    is_SetCameraID = _libs['ueye_api_64'].is_SetCameraID
    is_SetCameraID.argtypes = [HIDS, INT]
    is_SetCameraID.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2187
if hasattr(_libs['ueye_api_64'], 'is_SetBayerConversion'):
    is_SetBayerConversion = _libs['ueye_api_64'].is_SetBayerConversion
    is_SetBayerConversion.argtypes = [HIDS, INT]
    is_SetBayerConversion.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2190
if hasattr(_libs['ueye_api_64'], 'is_SetHardwareGamma'):
    is_SetHardwareGamma = _libs['ueye_api_64'].is_SetHardwareGamma
    is_SetHardwareGamma.argtypes = [HIDS, INT]
    is_SetHardwareGamma.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2193
if hasattr(_libs['ueye_api_64'], 'is_GetCameraList'):
    is_GetCameraList = _libs['ueye_api_64'].is_GetCameraList
    is_GetCameraList.argtypes = [PUEYE_CAMERA_LIST]
    is_GetCameraList.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2196
if hasattr(_libs['ueye_api_64'], 'is_SetAutoParameter'):
    is_SetAutoParameter = _libs['ueye_api_64'].is_SetAutoParameter
    is_SetAutoParameter.argtypes = [HIDS, INT, POINTER(c_double), POINTER(c_double)]
    is_SetAutoParameter.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2197
if hasattr(_libs['ueye_api_64'], 'is_GetAutoInfo'):
    is_GetAutoInfo = _libs['ueye_api_64'].is_GetAutoInfo
    is_GetAutoInfo.argtypes = [HIDS, POINTER(UEYE_AUTO_INFO)]
    is_GetAutoInfo.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2199
if hasattr(_libs['ueye_api_64'], 'is_GetImageHistogram'):
    is_GetImageHistogram = _libs['ueye_api_64'].is_GetImageHistogram
    is_GetImageHistogram.argtypes = [HIDS, c_int, INT, POINTER(DWORD)]
    is_GetImageHistogram.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2200
if hasattr(_libs['ueye_api_64'], 'is_SetTriggerDelay'):
    is_SetTriggerDelay = _libs['ueye_api_64'].is_SetTriggerDelay
    is_SetTriggerDelay.argtypes = [HIDS, INT]
    is_SetTriggerDelay.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2203
if hasattr(_libs['ueye_api_64'], 'is_SetGainBoost'):
    is_SetGainBoost = _libs['ueye_api_64'].is_SetGainBoost
    is_SetGainBoost.argtypes = [HIDS, INT]
    is_SetGainBoost.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2205
if hasattr(_libs['ueye_api_64'], 'is_SetGlobalShutter'):
    is_SetGlobalShutter = _libs['ueye_api_64'].is_SetGlobalShutter
    is_SetGlobalShutter.argtypes = [HIDS, INT]
    is_SetGlobalShutter.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2206
if hasattr(_libs['ueye_api_64'], 'is_SetExtendedRegister'):
    is_SetExtendedRegister = _libs['ueye_api_64'].is_SetExtendedRegister
    is_SetExtendedRegister.argtypes = [HIDS, INT, WORD]
    is_SetExtendedRegister.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2207
if hasattr(_libs['ueye_api_64'], 'is_GetExtendedRegister'):
    is_GetExtendedRegister = _libs['ueye_api_64'].is_GetExtendedRegister
    is_GetExtendedRegister.argtypes = [HIDS, INT, POINTER(WORD)]
    is_GetExtendedRegister.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2210
if hasattr(_libs['ueye_api_64'], 'is_SetHWGainFactor'):
    is_SetHWGainFactor = _libs['ueye_api_64'].is_SetHWGainFactor
    is_SetHWGainFactor.argtypes = [HIDS, INT, INT]
    is_SetHWGainFactor.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2213
if hasattr(_libs['ueye_api_64'], 'is_Renumerate'):
    is_Renumerate = _libs['ueye_api_64'].is_Renumerate
    is_Renumerate.argtypes = [HIDS, INT]
    is_Renumerate.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2216
if hasattr(_libs['ueye_api_64'], 'is_WriteI2C'):
    is_WriteI2C = _libs['ueye_api_64'].is_WriteI2C
    is_WriteI2C.argtypes = [HIDS, INT, INT, POINTER(BYTE), INT]
    is_WriteI2C.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2217
if hasattr(_libs['ueye_api_64'], 'is_ReadI2C'):
    is_ReadI2C = _libs['ueye_api_64'].is_ReadI2C
    is_ReadI2C.argtypes = [HIDS, INT, INT, POINTER(BYTE), INT]
    is_ReadI2C.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2225
class struct__KNEEPOINT(Structure):
    pass

struct__KNEEPOINT.__slots__ = [
    'x',
    'y',
]
struct__KNEEPOINT._fields_ = [
    ('x', c_double),
    ('y', c_double),
]

KNEEPOINT = struct__KNEEPOINT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2225

PKNEEPOINT = POINTER(struct__KNEEPOINT) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2225

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2232
class struct__KNEEPOINTARRAY(Structure):
    pass

struct__KNEEPOINTARRAY.__slots__ = [
    'NumberOfUsedKneepoints',
    'Kneepoint',
]
struct__KNEEPOINTARRAY._fields_ = [
    ('NumberOfUsedKneepoints', INT),
    ('Kneepoint', KNEEPOINT * 10),
]

KNEEPOINTARRAY = struct__KNEEPOINTARRAY # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2232

PKNEEPOINTARRAY = POINTER(struct__KNEEPOINTARRAY) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2232

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2245
class struct__KNEEPOINTINFO(Structure):
    pass

struct__KNEEPOINTINFO.__slots__ = [
    'NumberOfSupportedKneepoints',
    'NumberOfUsedKneepoints',
    'MinValueX',
    'MaxValueX',
    'MinValueY',
    'MaxValueY',
    'DefaultKneepoint',
    'Reserved',
]
struct__KNEEPOINTINFO._fields_ = [
    ('NumberOfSupportedKneepoints', INT),
    ('NumberOfUsedKneepoints', INT),
    ('MinValueX', c_double),
    ('MaxValueX', c_double),
    ('MinValueY', c_double),
    ('MaxValueY', c_double),
    ('DefaultKneepoint', KNEEPOINT * 10),
    ('Reserved', INT * 10),
]

KNEEPOINTINFO = struct__KNEEPOINTINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2245

PKNEEPOINTINFO = POINTER(struct__KNEEPOINTINFO) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2245

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2249
if hasattr(_libs['ueye_api_64'], 'is_GetHdrMode'):
    is_GetHdrMode = _libs['ueye_api_64'].is_GetHdrMode
    is_GetHdrMode.argtypes = [HIDS, POINTER(INT)]
    is_GetHdrMode.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2250
if hasattr(_libs['ueye_api_64'], 'is_EnableHdr'):
    is_EnableHdr = _libs['ueye_api_64'].is_EnableHdr
    is_EnableHdr.argtypes = [HIDS, INT]
    is_EnableHdr.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2251
if hasattr(_libs['ueye_api_64'], 'is_SetHdrKneepoints'):
    is_SetHdrKneepoints = _libs['ueye_api_64'].is_SetHdrKneepoints
    is_SetHdrKneepoints.argtypes = [HIDS, POINTER(KNEEPOINTARRAY), INT]
    is_SetHdrKneepoints.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2252
if hasattr(_libs['ueye_api_64'], 'is_GetHdrKneepoints'):
    is_GetHdrKneepoints = _libs['ueye_api_64'].is_GetHdrKneepoints
    is_GetHdrKneepoints.argtypes = [HIDS, POINTER(KNEEPOINTARRAY), INT]
    is_GetHdrKneepoints.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2253
if hasattr(_libs['ueye_api_64'], 'is_GetHdrKneepointInfo'):
    is_GetHdrKneepointInfo = _libs['ueye_api_64'].is_GetHdrKneepointInfo
    is_GetHdrKneepointInfo.argtypes = [HIDS, POINTER(KNEEPOINTINFO), INT]
    is_GetHdrKneepointInfo.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2255
if hasattr(_libs['ueye_api_64'], 'is_SetOptimalCameraTiming'):
    is_SetOptimalCameraTiming = _libs['ueye_api_64'].is_SetOptimalCameraTiming
    is_SetOptimalCameraTiming.argtypes = [HIDS, INT, INT, POINTER(INT), POINTER(c_double)]
    is_SetOptimalCameraTiming.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2257
if hasattr(_libs['ueye_api_64'], 'is_GetSupportedTestImages'):
    is_GetSupportedTestImages = _libs['ueye_api_64'].is_GetSupportedTestImages
    is_GetSupportedTestImages.argtypes = [HIDS, POINTER(INT)]
    is_GetSupportedTestImages.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2258
if hasattr(_libs['ueye_api_64'], 'is_GetTestImageValueRange'):
    is_GetTestImageValueRange = _libs['ueye_api_64'].is_GetTestImageValueRange
    is_GetTestImageValueRange.argtypes = [HIDS, INT, POINTER(INT), POINTER(INT)]
    is_GetTestImageValueRange.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2259
if hasattr(_libs['ueye_api_64'], 'is_SetSensorTestImage'):
    is_SetSensorTestImage = _libs['ueye_api_64'].is_SetSensorTestImage
    is_SetSensorTestImage.argtypes = [HIDS, INT, INT]
    is_SetSensorTestImage.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2261
if hasattr(_libs['ueye_api_64'], 'is_GetColorConverter'):
    is_GetColorConverter = _libs['ueye_api_64'].is_GetColorConverter
    is_GetColorConverter.argtypes = [HIDS, INT, POINTER(INT), POINTER(INT), POINTER(INT)]
    is_GetColorConverter.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2262
if hasattr(_libs['ueye_api_64'], 'is_SetColorConverter'):
    is_SetColorConverter = _libs['ueye_api_64'].is_SetColorConverter
    is_SetColorConverter.argtypes = [HIDS, INT, INT]
    is_SetColorConverter.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2264
if hasattr(_libs['ueye_api_64'], 'is_WaitForNextImage'):
    is_WaitForNextImage = _libs['ueye_api_64'].is_WaitForNextImage
    is_WaitForNextImage.argtypes = [HIDS, UINT, POINTER(POINTER(c_char)), POINTER(INT)]
    is_WaitForNextImage.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2265
if hasattr(_libs['ueye_api_64'], 'is_InitImageQueue'):
    is_InitImageQueue = _libs['ueye_api_64'].is_InitImageQueue
    is_InitImageQueue.argtypes = [HIDS, INT]
    is_InitImageQueue.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2266
if hasattr(_libs['ueye_api_64'], 'is_ExitImageQueue'):
    is_ExitImageQueue = _libs['ueye_api_64'].is_ExitImageQueue
    is_ExitImageQueue.argtypes = [HIDS]
    is_ExitImageQueue.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2268
if hasattr(_libs['ueye_api_64'], 'is_SetTimeout'):
    is_SetTimeout = _libs['ueye_api_64'].is_SetTimeout
    is_SetTimeout.argtypes = [HIDS, UINT, UINT]
    is_SetTimeout.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2269
if hasattr(_libs['ueye_api_64'], 'is_GetTimeout'):
    is_GetTimeout = _libs['ueye_api_64'].is_GetTimeout
    is_GetTimeout.argtypes = [HIDS, UINT, POINTER(UINT)]
    is_GetTimeout.restype = INT

enum_eUEYE_GET_ESTIMATED_TIME_MODE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2277

IS_SE_STARTER_FW_UPLOAD = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2277

IS_CP_STARTER_FW_UPLOAD = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2277

IS_STARTER_FW_UPLOAD = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2277

UEYE_GET_ESTIMATED_TIME_MODE = enum_eUEYE_GET_ESTIMATED_TIME_MODE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2277

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2280
if hasattr(_libs['ueye_api_64'], 'is_GetDuration'):
    is_GetDuration = _libs['ueye_api_64'].is_GetDuration
    is_GetDuration.argtypes = [HIDS, UINT, POINTER(INT)]
    is_GetDuration.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2294
class struct__SENSORSCALERINFO(Structure):
    pass

struct__SENSORSCALERINFO.__slots__ = [
    'nCurrMode',
    'nNumberOfSteps',
    'dblFactorIncrement',
    'dblMinFactor',
    'dblMaxFactor',
    'dblCurrFactor',
    'nSupportedModes',
    'bReserved',
]
struct__SENSORSCALERINFO._fields_ = [
    ('nCurrMode', INT),
    ('nNumberOfSteps', INT),
    ('dblFactorIncrement', c_double),
    ('dblMinFactor', c_double),
    ('dblMaxFactor', c_double),
    ('dblCurrFactor', c_double),
    ('nSupportedModes', INT),
    ('bReserved', BYTE * 84),
]

SENSORSCALERINFO = struct__SENSORSCALERINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2294

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2297
if hasattr(_libs['ueye_api_64'], 'is_GetSensorScalerInfo'):
    is_GetSensorScalerInfo = _libs['ueye_api_64'].is_GetSensorScalerInfo
    is_GetSensorScalerInfo.argtypes = [HIDS, POINTER(SENSORSCALERINFO), INT]
    is_GetSensorScalerInfo.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2298
if hasattr(_libs['ueye_api_64'], 'is_SetSensorScaler'):
    is_SetSensorScaler = _libs['ueye_api_64'].is_SetSensorScaler
    is_SetSensorScaler.argtypes = [HIDS, UINT, c_double]
    is_SetSensorScaler.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2310
class struct__UEYETIME(Structure):
    pass

struct__UEYETIME.__slots__ = [
    'wYear',
    'wMonth',
    'wDay',
    'wHour',
    'wMinute',
    'wSecond',
    'wMilliseconds',
    'byReserved',
]
struct__UEYETIME._fields_ = [
    ('wYear', WORD),
    ('wMonth', WORD),
    ('wDay', WORD),
    ('wHour', WORD),
    ('wMinute', WORD),
    ('wSecond', WORD),
    ('wMilliseconds', WORD),
    ('byReserved', BYTE * 10),
]

UEYETIME = struct__UEYETIME # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2310

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2336
if hasattr(_libs['ueye_api_64'], 'is_ImageFormat'):
    is_ImageFormat = _libs['ueye_api_64'].is_ImageFormat
    is_ImageFormat.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_ImageFormat.restype = INT

enum_E_IMAGE_FORMAT_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2349

IMGFRMT_CMD_GET_NUM_ENTRIES = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2349

IMGFRMT_CMD_GET_LIST = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2349

IMGFRMT_CMD_SET_FORMAT = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2349

IMGFRMT_CMD_GET_ARBITRARY_AOI_SUPPORTED = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2349

IMGFRMT_CMD_GET_FORMAT_INFO = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2349

IMAGE_FORMAT_CMD = enum_E_IMAGE_FORMAT_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2349

enum_E_CAPTUREMODE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2367

CAPTMODE_FREERUN = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2367

CAPTMODE_SINGLE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2367

CAPTMODE_TRIGGER_SOFT_SINGLE = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2367

CAPTMODE_TRIGGER_SOFT_CONTINUOUS = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2367

CAPTMODE_TRIGGER_HW_SINGLE = 256 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2367

CAPTMODE_TRIGGER_HW_CONTINUOUS = 512 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2367

CAPTUREMODE = enum_E_CAPTUREMODE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2367

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2384
class struct_S_IMAGE_FORMAT_INFO(Structure):
    pass

struct_S_IMAGE_FORMAT_INFO.__slots__ = [
    'nFormatID',
    'nWidth',
    'nHeight',
    'nX0',
    'nY0',
    'nSupportedCaptureModes',
    'nBinningMode',
    'nSubsamplingMode',
    'strFormatName',
    'dSensorScalerFactor',
    'nReserved',
]
struct_S_IMAGE_FORMAT_INFO._fields_ = [
    ('nFormatID', INT),
    ('nWidth', UINT),
    ('nHeight', UINT),
    ('nX0', INT),
    ('nY0', INT),
    ('nSupportedCaptureModes', UINT),
    ('nBinningMode', UINT),
    ('nSubsamplingMode', UINT),
    ('strFormatName', IS_CHAR * 64),
    ('dSensorScalerFactor', c_double),
    ('nReserved', UINT * 22),
]

IMAGE_FORMAT_INFO = struct_S_IMAGE_FORMAT_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2384

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2393
class struct_S_IMAGE_FORMAT_LIST(Structure):
    pass

struct_S_IMAGE_FORMAT_LIST.__slots__ = [
    'nSizeOfListEntry',
    'nNumListElements',
    'nReserved',
    'FormatInfo',
]
struct_S_IMAGE_FORMAT_LIST._fields_ = [
    ('nSizeOfListEntry', UINT),
    ('nNumListElements', UINT),
    ('nReserved', UINT * 4),
    ('FormatInfo', IMAGE_FORMAT_INFO * 1),
]

IMAGE_FORMAT_LIST = struct_S_IMAGE_FORMAT_LIST # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2393

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2396
if hasattr(_libs['ueye_api_64'], 'is_FaceDetection'):
    is_FaceDetection = _libs['ueye_api_64'].is_FaceDetection
    is_FaceDetection.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_FaceDetection.restype = INT

enum_E_FDT_CAPABILITY_FLAGS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INVALID = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_SUPPORTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_SEARCH_ANGLE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_SEARCH_AOI = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INFO_POSX = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INFO_POSY = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INFO_WIDTH = 64 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INFO_HEIGHT = 128 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INFO_ANGLE = 256 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INFO_POSTURE = 512 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INFO_FACENUMBER = 1024 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INFO_OVL = 2048 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INFO_NUM_OVL = 4096 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAP_INFO_OVL_LINEWIDTH = 8192 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

FDT_CAPABILITY_FLAGS = enum_E_FDT_CAPABILITY_FLAGS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2415

enum_E_FDT_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_CAPABILITIES = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_SET_DISABLE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_SET_ENABLE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_SET_SEARCH_ANGLE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_SEARCH_ANGLE = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_SET_SEARCH_ANGLE_ENABLE = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_SET_SEARCH_ANGLE_DISABLE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_SEARCH_ANGLE_ENABLE = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_SET_SEARCH_AOI = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_SEARCH_AOI = 9 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_FACE_LIST = 10 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_NUMBER_FACES = 11 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_SET_SUSPEND = 12 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_SET_RESUME = 13 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_MAX_NUM_FACES = 14 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_SET_INFO_MAX_NUM_OVL = 15 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_INFO_MAX_NUM_OVL = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_SET_INFO_OVL_LINE_WIDTH = 17 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_INFO_OVL_LINE_WIDTH = 18 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_ENABLE = 19 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_SUSPEND = 20 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_HORIZONTAL_RESOLUTION = 21 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD_GET_VERTICAL_RESOLUTION = 22 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

FDT_CMD = enum_E_FDT_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2469

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2472
if hasattr(_libs['ueye_api_64'], 'is_Focus'):
    is_Focus = _libs['ueye_api_64'].is_Focus
    is_Focus.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Focus.restype = INT

enum_E_FOCUS_CAPABILITY_FLAGS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2484

FOC_CAP_INVALID = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2484

FOC_CAP_AUTOFOCUS_SUPPORTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2484

FOC_CAP_MANUAL_SUPPORTED = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2484

FOC_CAP_GET_DISTANCE = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2484

FOC_CAP_SET_AUTOFOCUS_RANGE = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2484

FOC_CAP_AUTOFOCUS_FDT_AOI = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2484

FOC_CAP_AUTOFOCUS_ZONE = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2484

FOCUS_CAPABILITY_FLAGS = enum_E_FOCUS_CAPABILITY_FLAGS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2484

enum_E_FOCUS_RANGE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2492

FOC_RANGE_NORMAL = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2492

FOC_RANGE_ALLRANGE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2492

FOC_RANGE_MACRO = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2492

FOCUS_RANGE = enum_E_FOCUS_RANGE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2492

enum_E_FOCUS_STATUS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2501

FOC_STATUS_ERROR = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2501

FOC_STATUS_FOCUSED = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2501

FOC_STATUS_FOCUSING = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2501

FOC_STATUS_TIMEOUT = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2501

FOC_STATUS_CANCEL = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2501

FOCUS_STATUS = enum_E_FOCUS_STATUS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2501

enum_E_FOCUS_ZONE_WEIGHT = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2510

FOC_ZONE_WEIGHT_DISABLE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2510

FOC_ZONE_WEIGHT_WEAK = 33 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2510

FOC_ZONE_WEIGHT_MIDDLE = 50 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2510

FOC_ZONE_WEIGHT_STRONG = 66 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2510

FOCUS_ZONE_WEIGHT = enum_E_FOCUS_ZONE_WEIGHT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2510

enum_E_FOCUS_ZONE_AOI_PRESET = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

FOC_ZONE_AOI_PRESET_CENTER = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

FOC_ZONE_AOI_PRESET_UPPER_LEFT = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

FOC_ZONE_AOI_PRESET_BOTTOM_LEFT = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

FOC_ZONE_AOI_PRESET_UPPER_RIGHT = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

FOC_ZONE_AOI_PRESET_BOTTOM_RIGHT = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

FOC_ZONE_AOI_PRESET_UPPER_CENTER = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

FOC_ZONE_AOI_PRESET_BOTTOM_CENTER = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

FOC_ZONE_AOI_PRESET_CENTER_LEFT = 64 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

FOC_ZONE_AOI_PRESET_CENTER_RIGHT = 128 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

FOCUS_ZONE_AOI_PRESET = enum_E_FOCUS_ZONE_AOI_PRESET # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2527

enum_E_FOCUS_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_CAPABILITIES = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_SET_DISABLE_AUTOFOCUS = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_SET_ENABLE_AUTOFOCUS = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ENABLE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_SET_AUTOFOCUS_RANGE = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_RANGE = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_DISTANCE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_SET_MANUAL_FOCUS = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_MANUAL_FOCUS = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_MANUAL_FOCUS_MIN = 9 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_MANUAL_FOCUS_MAX = 10 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_MANUAL_FOCUS_INC = 11 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_SET_ENABLE_AF_FDT_AOI = 12 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_SET_DISABLE_AF_FDT_AOI = 13 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AF_FDT_AOI_ENABLE = 14 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_SET_ENABLE_AUTOFOCUS_ONCE = 15 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_STATUS = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_SET_AUTOFOCUS_ZONE_AOI = 17 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_AOI = 18 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_AOI_DEFAULT = 19 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_POS_MIN = 20 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_POS_MAX = 21 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_POS_INC = 22 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_SIZE_MIN = 23 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_SIZE_MAX = 24 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_SIZE_INC = 25 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_SET_AUTOFOCUS_ZONE_WEIGHT = 26 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_WEIGHT = 27 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_WEIGHT_COUNT = 28 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_WEIGHT_DEFAULT = 29 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_SET_AUTOFOCUS_ZONE_AOI_PRESET = 30 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_AOI_PRESET = 31 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_AOI_PRESET_DEFAULT = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOC_CMD_GET_AUTOFOCUS_ZONE_ARBITRARY_AOI_SUPPORTED = 33 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

FOCUS_CMD = enum_E_FOCUS_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2567

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2570
if hasattr(_libs['ueye_api_64'], 'is_ImageStabilization'):
    is_ImageStabilization = _libs['ueye_api_64'].is_ImageStabilization
    is_ImageStabilization.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_ImageStabilization.restype = INT

enum_E_IMGSTAB_CAPABILITY_FLAGS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2577

IMGSTAB_CAP_INVALID = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2577

IMGSTAB_CAP_IMAGE_STABILIZATION_SUPPORTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2577

IMGSTAB_CAPABILITY_FLAGS = enum_E_IMGSTAB_CAPABILITY_FLAGS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2577

enum_E_IMGSTAB_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2587

IMGSTAB_CMD_GET_CAPABILITIES = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2587

IMGSTAB_CMD_SET_DISABLE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2587

IMGSTAB_CMD_SET_ENABLE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2587

IMGSTAB_CMD_GET_ENABLE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2587

IMGSTAB_CMD = enum_E_IMGSTAB_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2587

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2590
if hasattr(_libs['ueye_api_64'], 'is_ScenePreset'):
    is_ScenePreset = _libs['ueye_api_64'].is_ScenePreset
    is_ScenePreset.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_ScenePreset.restype = INT

enum_E_SCENE_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2598

SCENE_CMD_GET_SUPPORTED_PRESETS = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2598

SCENE_CMD_SET_PRESET = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2598

SCENE_CMD_GET_PRESET = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2598

SCENE_CMD_GET_DEFAULT_PRESET = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2598

SCENE_CMD = enum_E_SCENE_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2598

enum_E_SCENE_PRESET = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2612

SCENE_INVALID = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2612

SCENE_SENSOR_AUTOMATIC = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2612

SCENE_SENSOR_PORTRAIT = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2612

SCENE_SENSOR_SUNNY = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2612

SCENE_SENSOR_ENTERTAINMENT = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2612

SCENE_SENSOR_NIGHT = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2612

SCENE_SENSOR_SPORTS = 64 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2612

SCENE_SENSOR_LANDSCAPE = 128 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2612

SCENE_PRESET = enum_E_SCENE_PRESET # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2612

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2615
if hasattr(_libs['ueye_api_64'], 'is_Zoom'):
    is_Zoom = _libs['ueye_api_64'].is_Zoom
    is_Zoom.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Zoom.restype = INT

enum_E_ZOOM_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2627

ZOOM_CMD_GET_CAPABILITIES = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2627

ZOOM_CMD_DIGITAL_GET_NUM_LIST_ENTRIES = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2627

ZOOM_CMD_DIGITAL_GET_LIST = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2627

ZOOM_CMD_DIGITAL_SET_VALUE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2627

ZOOM_CMD_DIGITAL_GET_VALUE = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2627

ZOOM_CMD_DIGITAL_GET_VALUE_RANGE = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2627

ZOOM_CMD_DIGITAL_GET_VALUE_DEFAULT = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2627

ZOOM_CMD = enum_E_ZOOM_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2627

enum_E_ZOOM_CAPABILITY_FLAGS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2634

ZOOM_CAP_INVALID = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2634

ZOOM_CAP_DIGITAL_ZOOM = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2634

ZOOM_CAPABILITY_FLAGS = enum_E_ZOOM_CAPABILITY_FLAGS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2634

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2637
if hasattr(_libs['ueye_api_64'], 'is_Sharpness'):
    is_Sharpness = _libs['ueye_api_64'].is_Sharpness
    is_Sharpness.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Sharpness.restype = INT

enum_E_SHARPNESS_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2650

SHARPNESS_CMD_GET_CAPABILITIES = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2650

SHARPNESS_CMD_GET_VALUE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2650

SHARPNESS_CMD_GET_MIN_VALUE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2650

SHARPNESS_CMD_GET_MAX_VALUE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2650

SHARPNESS_CMD_GET_INCREMENT = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2650

SHARPNESS_CMD_GET_DEFAULT_VALUE = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2650

SHARPNESS_CMD_SET_VALUE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2650

SHARPNESS_CMD = enum_E_SHARPNESS_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2650

enum_E_SHARPNESS_CAPABILITY_FLAGS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2658

SHARPNESS_CAP_INVALID = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2658

SHARPNESS_CAP_SHARPNESS_SUPPORTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2658

SHARPNESS_CAPABILITY_FLAGS = enum_E_SHARPNESS_CAPABILITY_FLAGS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2658

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2661
if hasattr(_libs['ueye_api_64'], 'is_Saturation'):
    is_Saturation = _libs['ueye_api_64'].is_Saturation
    is_Saturation.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Saturation.restype = INT

enum_E_SATURATION_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2674

SATURATION_CMD_GET_CAPABILITIES = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2674

SATURATION_CMD_GET_VALUE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2674

SATURATION_CMD_GET_MIN_VALUE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2674

SATURATION_CMD_GET_MAX_VALUE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2674

SATURATION_CMD_GET_INCREMENT = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2674

SATURATION_CMD_GET_DEFAULT_VALUE = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2674

SATURATION_CMD_SET_VALUE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2674

SATURATION_CMD = enum_E_SATURATION_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2674

enum_E_SATURATION_CAPABILITY_FLAGS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2682

SATURATION_CAP_INVALID = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2682

SATURATION_CAP_SATURATION_SUPPORTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2682

SATURATION_CAPABILITY_FLAGS = enum_E_SATURATION_CAPABILITY_FLAGS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2682

enum_E_TRIGGER_DEBOUNCE_MODE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2694

TRIGGER_DEBOUNCE_MODE_NONE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2694

TRIGGER_DEBOUNCE_MODE_FALLING_EDGE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2694

TRIGGER_DEBOUNCE_MODE_RISING_EDGE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2694

TRIGGER_DEBOUNCE_MODE_BOTH_EDGES = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2694

TRIGGER_DEBOUNCE_MODE_AUTOMATIC = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2694

TRIGGER_DEBOUNCE_MODE = enum_E_TRIGGER_DEBOUNCE_MODE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2694

enum_E_TRIGGER_DEBOUNCE_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD_SET_MODE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD_SET_DELAY_TIME = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD_GET_SUPPORTED_MODES = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD_GET_MODE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD_GET_DELAY_TIME = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD_GET_DELAY_TIME_MIN = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD_GET_DELAY_TIME_MAX = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD_GET_DELAY_TIME_INC = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD_GET_MODE_DEFAULT = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD_GET_DELAY_TIME_DEFAULT = 9 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

TRIGGER_DEBOUNCE_CMD = enum_E_TRIGGER_DEBOUNCE_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2711

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2714
if hasattr(_libs['ueye_api_64'], 'is_TriggerDebounce'):
    is_TriggerDebounce = _libs['ueye_api_64'].is_TriggerDebounce
    is_TriggerDebounce.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_TriggerDebounce.restype = INT

enum_E_RGB_COLOR_MODELS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2725

RGB_COLOR_MODEL_SRGB_D50 = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2725

RGB_COLOR_MODEL_SRGB_D65 = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2725

RGB_COLOR_MODEL_CIE_RGB_E = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2725

RGB_COLOR_MODEL_ECI_RGB_D50 = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2725

RGB_COLOR_MODEL_ADOBE_RGB_D65 = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2725

RGB_COLOR_MODELS = enum_E_RGB_COLOR_MODELS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2725

enum_E_LENS_SHADING_MODELS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2734

LSC_MODEL_AGL = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2734

LSC_MODEL_TL84 = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2734

LSC_MODEL_D50 = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2734

LSC_MODEL_D65 = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2734

LENS_SHADING_MODELS = enum_E_LENS_SHADING_MODELS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2734

enum_E_COLOR_TEMPERATURE_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_SET_TEMPERATURE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_SET_RGB_COLOR_MODEL = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_SUPPORTED_RGB_COLOR_MODELS = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_TEMPERATURE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_RGB_COLOR_MODEL = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_TEMPERATURE_MIN = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_TEMPERATURE_MAX = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_TEMPERATURE_INC = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_TEMPERATURE_DEFAULT = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_RGB_COLOR_MODEL_DEFAULT = 9 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_SET_LENS_SHADING_MODEL = 10 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_LENS_SHADING_MODEL = 11 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_LENS_SHADING_MODEL_SUPPORTED = 12 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD_GET_LENS_SHADING_MODEL_DEFAULT = 13 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

COLOR_TEMPERATURE_CMD = enum_E_COLOR_TEMPERATURE_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2754

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2756
if hasattr(_libs['ueye_api_64'], 'is_ColorTemperature'):
    is_ColorTemperature = _libs['ueye_api_64'].is_ColorTemperature
    is_ColorTemperature.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_ColorTemperature.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2763
class struct__OPENGL_DISPLAY(Structure):
    pass

struct__OPENGL_DISPLAY.__slots__ = [
    'nWindowID',
    'pDisplay',
]
struct__OPENGL_DISPLAY._fields_ = [
    ('nWindowID', c_int),
    ('pDisplay', POINTER(None)),
]

OPENGL_DISPLAY = struct__OPENGL_DISPLAY # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2763

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2765
if hasattr(_libs['ueye_api_64'], 'is_DirectRenderer'):
    is_DirectRenderer = _libs['ueye_api_64'].is_DirectRenderer
    is_DirectRenderer.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_DirectRenderer.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2767
if hasattr(_libs['ueye_api_64'], 'is_HotPixel'):
    is_HotPixel = _libs['ueye_api_64'].is_HotPixel
    is_HotPixel.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_HotPixel.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2774
class struct_anon_206(Structure):
    pass

struct_anon_206.__slots__ = [
    's32X',
    's32Y',
]
struct_anon_206._fields_ = [
    ('s32X', INT),
    ('s32Y', INT),
]

IS_POINT_2D = struct_anon_206 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2774

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2780
class struct_anon_207(Structure):
    pass

struct_anon_207.__slots__ = [
    's32Width',
    's32Height',
]
struct_anon_207._fields_ = [
    ('s32Width', INT),
    ('s32Height', INT),
]

IS_SIZE_2D = struct_anon_207 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2780

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2788
class struct_anon_208(Structure):
    pass

struct_anon_208.__slots__ = [
    's32X',
    's32Y',
    's32Width',
    's32Height',
]
struct_anon_208._fields_ = [
    ('s32X', INT),
    ('s32Y', INT),
    ('s32Width', INT),
    ('s32Height', INT),
]

IS_RECT = struct_anon_208 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2788

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2807
class struct_anon_209(Structure):
    pass

struct_anon_209.__slots__ = [
    's32AOIIndex',
    's32NumberOfCycleRepetitions',
    's32X',
    's32Y',
    'dblExposure',
    's32Gain',
    's32BinningMode',
    's32SubsamplingMode',
    's32DetachImageParameters',
    'dblScalerFactor',
    'byReserved',
]
struct_anon_209._fields_ = [
    ('s32AOIIndex', INT),
    ('s32NumberOfCycleRepetitions', INT),
    ('s32X', INT),
    ('s32Y', INT),
    ('dblExposure', c_double),
    ('s32Gain', INT),
    ('s32BinningMode', INT),
    ('s32SubsamplingMode', INT),
    ('s32DetachImageParameters', INT),
    ('dblScalerFactor', c_double),
    ('byReserved', BYTE * 64),
]

AOI_SEQUENCE_PARAMS = struct_anon_209 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2807

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2810
if hasattr(_libs['ueye_api_64'], 'is_AOI'):
    is_AOI = _libs['ueye_api_64'].is_AOI
    is_AOI.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_AOI.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2825
class struct_S_RANGE_OF_VALUES_U32(Structure):
    pass

struct_S_RANGE_OF_VALUES_U32.__slots__ = [
    'u32Minimum',
    'u32Maximum',
    'u32Increment',
    'u32Default',
    'u32Infinite',
]
struct_S_RANGE_OF_VALUES_U32._fields_ = [
    ('u32Minimum', UINT),
    ('u32Maximum', UINT),
    ('u32Increment', UINT),
    ('u32Default', UINT),
    ('u32Infinite', UINT),
]

RANGE_OF_VALUES_U32 = struct_S_RANGE_OF_VALUES_U32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2825

enum_E_TRANSFER_CAPABILITY_FLAGS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2847

TRANSFER_CAP_IMAGEDELAY = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2847

TRANSFER_CAP_PACKETINTERVAL = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2847

TRANSFER_CAPABILITY_FLAGS = enum_E_TRANSFER_CAPABILITY_FLAGS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2847

enum_E_TRANSFER_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD_QUERY_CAPABILITIES = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD_SET_IMAGEDELAY_US = 1000 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD_SET_PACKETINTERVAL_US = 1005 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD_GET_IMAGEDELAY_US = 2000 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD_GET_PACKETINTERVAL_US = 2005 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD_GETRANGE_IMAGEDELAY_US = 3000 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD_GETRANGE_PACKETINTERVAL_US = 3005 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD_SET_IMAGE_DESTINATION = 5000 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD_GET_IMAGE_DESTINATION = 5001 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD_GET_IMAGE_DESTINATION_CAPABILITIES = 5002 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

TRANSFER_CMD = enum_E_TRANSFER_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2916

enum_E_TRANSFER_TARGET = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2924

IS_TRANSFER_DESTINATION_DEVICE_MEMORY = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2924

IS_TRANSFER_DESTINATION_USER_MEMORY = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2924

TRANSFER_TARGET = enum_E_TRANSFER_TARGET # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2924

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2940
if hasattr(_libs['ueye_api_64'], 'is_Transfer'):
    is_Transfer = _libs['ueye_api_64'].is_Transfer
    is_Transfer.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Transfer.restype = INT

IS_BOOTBOOST_ID = BYTE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2953

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2982
class struct_S_IS_BOOTBOOST_IDLIST(Structure):
    pass

struct_S_IS_BOOTBOOST_IDLIST.__slots__ = [
    'u32NumberOfEntries',
    'aList',
]
struct_S_IS_BOOTBOOST_IDLIST._fields_ = [
    ('u32NumberOfEntries', DWORD),
    ('aList', IS_BOOTBOOST_ID * 1),
]

IS_BOOTBOOST_IDLIST = struct_S_IS_BOOTBOOST_IDLIST # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2982

enum_E_IS_BOOTBOOST_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_ENABLE = 65537 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_ENABLE_AND_WAIT = 65793 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_DISABLE = 65553 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_DISABLE_AND_WAIT = 65809 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_WAIT = 65792 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_GET_ENABLED = 536936481 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_ADD_ID = 269484033 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_SET_IDLIST = 269484037 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_REMOVE_ID = 269484049 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_CLEAR_IDLIST = 1048597 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_GET_IDLIST = 806354977 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD_GET_IDLIST_SIZE = 537919522 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

IS_BOOTBOOST_CMD = enum_E_IS_BOOTBOOST_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3078

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3094
if hasattr(_libs['ueye_api_64'], 'is_BootBoost'):
    is_BootBoost = _libs['ueye_api_64'].is_BootBoost
    is_BootBoost.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_BootBoost.restype = INT

enum_E_DEVICE_FEATURE_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_SUPPORTED_FEATURES = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_LINESCAN_MODE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LINESCAN_MODE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_LINESCAN_NUMBER = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LINESCAN_NUMBER = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_SHUTTER_MODE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_SHUTTER_MODE = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_PREFER_XS_HS_MODE = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_PREFER_XS_HS_MODE = 9 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_DEFAULT_PREFER_XS_HS_MODE = 10 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_DEFAULT = 11 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LOG_MODE = 12 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_LOG_MODE = 13 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_VALUE_DEFAULT = 14 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_VALUE_RANGE = 15 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_VALUE = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_LOG_MODE_MANUAL_VALUE = 17 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_GAIN_DEFAULT = 18 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_GAIN_RANGE = 19 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_GAIN = 20 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_LOG_MODE_MANUAL_GAIN = 21 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_MODE_DEFAULT = 22 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_MODE = 23 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_MODE = 24 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_POSITION_DEFAULT = 25 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_POSITION_RANGE = 26 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_POSITION = 27 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_POSITION = 28 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_FPN_CORRECTION_MODE_DEFAULT = 29 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_FPN_CORRECTION_MODE = 30 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_FPN_CORRECTION_MODE = 31 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_SENSOR_SOURCE_GAIN_RANGE = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_SENSOR_SOURCE_GAIN_DEFAULT = 33 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_SENSOR_SOURCE_GAIN = 34 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_SENSOR_SOURCE_GAIN = 35 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_BLACK_REFERENCE_MODE_DEFAULT = 36 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_BLACK_REFERENCE_MODE = 37 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_BLACK_REFERENCE_MODE = 38 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_ALLOW_RAW_WITH_LUT = 39 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_ALLOW_RAW_WITH_LUT = 40 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_SUPPORTED_SENSOR_BIT_DEPTHS = 41 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_SENSOR_BIT_DEPTH_DEFAULT = 42 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_SENSOR_BIT_DEPTH = 43 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_SENSOR_BIT_DEPTH = 44 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_TEMPERATURE = 45 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_JPEG_COMPRESSION = 46 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_JPEG_COMPRESSION = 47 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_JPEG_COMPRESSION_DEFAULT = 48 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_JPEG_COMPRESSION_RANGE = 49 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_NOISE_REDUCTION_MODE = 50 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_NOISE_REDUCTION_MODE = 51 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_NOISE_REDUCTION_MODE_DEFAULT = 52 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_TIMESTAMP_CONFIGURATION = 53 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_TIMESTAMP_CONFIGURATION = 54 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_DEFAULT = 55 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_NUMBER = 56 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_LIST = 57 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT = 58 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_HEIGHT = 59 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_ADDITIONAL_POSITION_DEFAULT = 60 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_ADDITIONAL_POSITION_RANGE = 61 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_ADDITIONAL_POSITION = 62 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_ADDITIONAL_POSITION = 63 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_SENSOR_TEMPERATURE_NUMERICAL_VALUE = 64 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_IMAGE_EFFECT = 65 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_IMAGE_EFFECT = 66 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_IMAGE_EFFECT_DEFAULT = 67 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_EXTENDED_PIXELCLOCK_RANGE_ENABLE_DEFAULT = 68 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_EXTENDED_PIXELCLOCK_RANGE_ENABLE = 69 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_EXTENDED_PIXELCLOCK_RANGE_ENABLE = 70 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_GET_SCOPE = 71 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_GET_PARAMS = 72 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_SET_PARAMS = 73 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_GET_MODE_DEFAULT = 74 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_GET_MODE = 75 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_SET_MODE = 76 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_I2C_TARGET = 77 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_WIDE_DYNAMIC_RANGE_MODE = 78 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_WIDE_DYNAMIC_RANGE_MODE = 79 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_WIDE_DYNAMIC_RANGE_MODE_DEFAULT = 80 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_SUPPORTED_BLACK_REFERENCE_MODES = 81 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_SET_LEVEL_CONTROLLED_TRIGGER_INPUT_MODE = 82 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LEVEL_CONTROLLED_TRIGGER_INPUT_MODE = 83 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_LEVEL_CONTROLLED_TRIGGER_INPUT_MODE_DEFAULT = 84 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_MODE_SUPPORTED_LINE_MODES = 85 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

DEVICE_FEATURE_CMD = enum_E_DEVICE_FEATURE_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3190

enum_E_DEVICE_FEATURE_MODE_CAPS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_SHUTTER_MODE_ROLLING = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_SHUTTER_MODE_GLOBAL = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_LINESCAN_MODE_FAST = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_LINESCAN_NUMBER = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_PREFER_XS_HS_MODE = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_LOG_MODE = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_SHUTTER_MODE_ROLLING_GLOBAL_START = 64 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_SHUTTER_MODE_GLOBAL_ALTERNATIVE_TIMING = 128 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_VERTICAL_AOI_MERGE = 256 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_FPN_CORRECTION = 512 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_SENSOR_SOURCE_GAIN = 1024 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_BLACK_REFERENCE = 2048 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_SENSOR_BIT_DEPTH = 4096 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_TEMPERATURE = 8192 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_JPEG_COMPRESSION = 16384 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_NOISE_REDUCTION = 32768 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_TIMESTAMP_CONFIGURATION = 65536 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_IMAGE_EFFECT = 131072 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_EXTENDED_PIXELCLOCK_RANGE = 262144 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_MULTI_INTEGRATION = 524288 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_WIDE_DYNAMIC_RANGE = 1048576 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

IS_DEVICE_FEATURE_CAP_LEVEL_CONTROLLED_TRIGGER = 2097152 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

DEVICE_FEATURE_MODE_CAPS = enum_E_DEVICE_FEATURE_MODE_CAPS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3223

enum_E_NOISE_REDUCTION_MODES = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3234

IS_NOISE_REDUCTION_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3234

IS_NOISE_REDUCTION_ADAPTIVE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3234

NOISE_REDUCTION_MODES = enum_E_NOISE_REDUCTION_MODES # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3234

enum_E_LOG_MODES = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3248

IS_LOG_MODE_FACTORY_DEFAULT = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3248

IS_LOG_MODE_OFF = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3248

IS_LOG_MODE_MANUAL = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3248

IS_LOG_MODE_AUTO = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3248

LOG_MODES = enum_E_LOG_MODES # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3248

enum_E_VERTICAL_AOI_MERGE_MODES = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3266

IS_VERTICAL_AOI_MERGE_MODE_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3266

IS_VERTICAL_AOI_MERGE_MODE_FREERUN = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3266

IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_SOFTWARE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3266

IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_FALLING_GPIO1 = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3266

IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_RISING_GPIO1 = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3266

IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_FALLING_GPIO2 = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3266

IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_RISING_GPIO2 = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3266

VERTICAL_AOI_MERGE_MODES = enum_E_VERTICAL_AOI_MERGE_MODES # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3266

enum_E_VERTICAL_AOI_MERGE_MODE_LINE_TRIGGER = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3280

IS_VERTICAL_AOI_MERGE_MODE_LINE_FREERUN = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3280

IS_VERTICAL_AOI_MERGE_MODE_LINE_SOFTWARE_TRIGGER = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3280

IS_VERTICAL_AOI_MERGE_MODE_LINE_GPIO_TRIGGER = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3280

VERTICAL_AOI_MERGE_MODE_LINE_TRIGGER = enum_E_VERTICAL_AOI_MERGE_MODE_LINE_TRIGGER # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3280

enum_E_LEVEL_CONTROLLED_TRIGGER_INPUT_MODES = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3293

IS_LEVEL_CONTROLLED_TRIGGER_INPUT_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3293

IS_LEVEL_CONTROLLED_TRIGGER_INPUT_ON = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3293

LEVEL_CONTROLLED_TRIGGER_INPUT_MODES = enum_E_LEVEL_CONTROLLED_TRIGGER_INPUT_MODES # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3293

enum_E_FPN_CORRECTION_MODES = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3306

IS_FPN_CORRECTION_MODE_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3306

IS_FPN_CORRECTION_MODE_HARDWARE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3306

FPN_CORRECTION_MODES = enum_E_FPN_CORRECTION_MODES # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3306

enum_E_BLACK_REFERENCE_MODES = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3320

IS_BLACK_REFERENCE_MODE_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3320

IS_BLACK_REFERENCE_MODE_COLUMNS_LEFT = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3320

IS_BLACK_REFERENCE_MODE_ROWS_TOP = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3320

BLACK_REFERENCE_MODES = enum_E_BLACK_REFERENCE_MODES # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3320

enum_E_SENSOR_BIT_DEPTH = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3335

IS_SENSOR_BIT_DEPTH_AUTO = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3335

IS_SENSOR_BIT_DEPTH_8_BIT = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3335

IS_SENSOR_BIT_DEPTH_10_BIT = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3335

IS_SENSOR_BIT_DEPTH_12_BIT = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3335

SENSOR_BIT_DEPTH = enum_E_SENSOR_BIT_DEPTH # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3335

enum_E_TIMESTAMP_CONFIGURATION_MODE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3347

IS_RESET_TIMESTAMP_ONCE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3347

TIMESTAMP_CONFIGURATION_MODE = enum_E_TIMESTAMP_CONFIGURATION_MODE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3347

enum_E_TIMESTAMP_CONFIGURATION_PIN = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3362

TIMESTAMP_CONFIGURATION_PIN_NONE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3362

TIMESTAMP_CONFIGURATION_PIN_TRIGGER = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3362

TIMESTAMP_CONFIGURATION_PIN_GPIO_1 = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3362

TIMESTAMP_CONFIGURATION_PIN_GPIO_2 = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3362

TIMESTAMP_CONFIGURATION_PIN = enum_E_TIMESTAMP_CONFIGURATION_PIN # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3362

enum_E_TIMESTAMP_CONFIGURATION_EDGE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3375

TIMESTAMP_CONFIGURATION_EDGE_FALLING = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3375

TIMESTAMP_CONFIGURATION_EDGE_RISING = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3375

TIMESTAMP_CONFIGURATION_EDGE = enum_E_TIMESTAMP_CONFIGURATION_EDGE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3375

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3384
class struct_S_IS_TIMESTAMP_CONFIGURATION(Structure):
    pass

struct_S_IS_TIMESTAMP_CONFIGURATION.__slots__ = [
    's32Mode',
    's32Pin',
    's32Edge',
]
struct_S_IS_TIMESTAMP_CONFIGURATION._fields_ = [
    ('s32Mode', INT),
    ('s32Pin', INT),
    ('s32Edge', INT),
]

IS_TIMESTAMP_CONFIGURATION = struct_S_IS_TIMESTAMP_CONFIGURATION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3384

enum_E_IMAGE_EFFECT_MODE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3400

IS_IMAGE_EFFECT_DISABLE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3400

IS_IMAGE_EFFECT_SEPIA = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3400

IS_IMAGE_EFFECT_MONOCHROME = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3400

IS_IMAGE_EFFECT_NEGATIVE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3400

IS_IMAGE_EFFECT_CROSSHAIRS = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3400

IMAGE_EFFECT_MODE = enum_E_IMAGE_EFFECT_MODE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3400

enum_S_IS_EXTENDED_PIXELCLOCK_RANGE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3413

EXTENDED_PIXELCLOCK_RANGE_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3413

EXTENDED_PIXELCLOCK_RANGE_ON = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3413

IS_EXTENDED_PIXELCLOCK_RANGE = enum_S_IS_EXTENDED_PIXELCLOCK_RANGE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3413

enum_E_IS_MULTI_INTEGRATION_MODE = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3428

MULTI_INTEGRATION_MODE_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3428

MULTI_INTEGRATION_MODE_SOFTWARE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3428

MULTI_INTEGRATION_MODE_GPIO1 = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3428

MULTI_INTEGRATION_MODE_GPIO2 = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3428

IS_MULTI_INTEGRATION_MODE = enum_E_IS_MULTI_INTEGRATION_MODE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3428

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3436
class struct_S_IS_MULTI_INTEGRATION_CYCLES(Structure):
    pass

struct_S_IS_MULTI_INTEGRATION_CYCLES.__slots__ = [
    'dblIntegration_ms',
    'dblPause_ms',
]
struct_S_IS_MULTI_INTEGRATION_CYCLES._fields_ = [
    ('dblIntegration_ms', c_double),
    ('dblPause_ms', c_double),
]

IS_MULTI_INTEGRATION_CYCLES = struct_S_IS_MULTI_INTEGRATION_CYCLES # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3436

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3456
class struct_S_IS_MULTI_INTEGRATION_SCOPE(Structure):
    pass

struct_S_IS_MULTI_INTEGRATION_SCOPE.__slots__ = [
    'dblMinIntegration_ms',
    'dblMaxIntegration_ms',
    'dblIntegrationGranularity_ms',
    'dblMinPause_ms',
    'dblMaxPause_ms',
    'dblPauseGranularity_ms',
    'dblMinCycle_ms',
    'dblMaxCycle_ms',
    'dblCycleGranularity_ms',
    'dblMinTriggerCycle_ms',
    'dblMinTriggerDuration_ms',
    'nMinNumberOfCycles',
    'nMaxNumberOfCycles',
    'm_bReserved',
]
struct_S_IS_MULTI_INTEGRATION_SCOPE._fields_ = [
    ('dblMinIntegration_ms', c_double),
    ('dblMaxIntegration_ms', c_double),
    ('dblIntegrationGranularity_ms', c_double),
    ('dblMinPause_ms', c_double),
    ('dblMaxPause_ms', c_double),
    ('dblPauseGranularity_ms', c_double),
    ('dblMinCycle_ms', c_double),
    ('dblMaxCycle_ms', c_double),
    ('dblCycleGranularity_ms', c_double),
    ('dblMinTriggerCycle_ms', c_double),
    ('dblMinTriggerDuration_ms', c_double),
    ('nMinNumberOfCycles', UINT),
    ('nMaxNumberOfCycles', UINT),
    ('m_bReserved', BYTE * 32),
]

IS_MULTI_INTEGRATION_SCOPE = struct_S_IS_MULTI_INTEGRATION_SCOPE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3456

enum_E_IS_I2C_TARGET = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3466

I2C_TARGET_DEFAULT = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3466

I2C_TARGET_SENSOR_1 = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3466

I2C_TARGET_SENSOR_2 = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3466

I2C_TARGET_LOGIC_BOARD = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3466

IS_I2C_TARGET = enum_E_IS_I2C_TARGET # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3466

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3478
if hasattr(_libs['ueye_api_64'], 'is_DeviceFeature'):
    is_DeviceFeature = _libs['ueye_api_64'].is_DeviceFeature
    is_DeviceFeature.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_DeviceFeature.restype = INT

enum_E_EXPOSURE_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_CAPS = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_EXPOSURE_DEFAULT = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE_MIN = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE_MAX = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE_INC = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_EXPOSURE = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_FINE_INCREMENT_RANGE_MIN = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_FINE_INCREMENT_RANGE_MAX = 9 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_FINE_INCREMENT_RANGE_INC = 10 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_FINE_INCREMENT_RANGE = 11 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_SET_EXPOSURE = 12 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_LONG_EXPOSURE_RANGE_MIN = 13 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_LONG_EXPOSURE_RANGE_MAX = 14 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_LONG_EXPOSURE_RANGE_INC = 15 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_LONG_EXPOSURE_RANGE = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_LONG_EXPOSURE_ENABLE = 17 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_SET_LONG_EXPOSURE_ENABLE = 18 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_DUAL_EXPOSURE_RATIO_DEFAULT = 19 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_DUAL_EXPOSURE_RATIO_RANGE = 20 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_GET_DUAL_EXPOSURE_RATIO = 21 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

IS_EXPOSURE_CMD_SET_DUAL_EXPOSURE_RATIO = 22 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

EXPOSURE_CMD = enum_E_EXPOSURE_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3511

enum_E_EXPOSURE_CAPS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3521

IS_EXPOSURE_CAP_EXPOSURE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3521

IS_EXPOSURE_CAP_FINE_INCREMENT = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3521

IS_EXPOSURE_CAP_LONG_EXPOSURE = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3521

IS_EXPOSURE_CAP_DUAL_EXPOSURE = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3521

EXPOSURE_CAPS = enum_E_EXPOSURE_CAPS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3521

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3533
if hasattr(_libs['ueye_api_64'], 'is_Exposure'):
    is_Exposure = _libs['ueye_api_64'].is_Exposure
    is_Exposure.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Exposure.restype = INT

enum_E_TRIGGER_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_GET_BURST_SIZE_SUPPORTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_GET_BURST_SIZE_RANGE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_GET_BURST_SIZE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_SET_BURST_SIZE = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_GET_FRAME_PRESCALER_SUPPORTED = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_GET_FRAME_PRESCALER_RANGE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_GET_FRAME_PRESCALER = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_SET_FRAME_PRESCALER = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_GET_LINE_PRESCALER_SUPPORTED = 9 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_GET_LINE_PRESCALER_RANGE = 10 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_GET_LINE_PRESCALER = 11 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

IS_TRIGGER_CMD_SET_LINE_PRESCALER = 12 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

TRIGGER_CMD = enum_E_TRIGGER_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3552

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3564
if hasattr(_libs['ueye_api_64'], 'is_Trigger'):
    is_Trigger = _libs['ueye_api_64'].is_Trigger
    is_Trigger.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Trigger.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3594
class struct_S_IS_DEVICE_INFO_HEARTBEAT(Structure):
    pass

struct_S_IS_DEVICE_INFO_HEARTBEAT.__slots__ = [
    'reserved_1',
    'dwRuntimeFirmwareVersion',
    'reserved_2',
    'wTemperature',
    'wLinkSpeed_Mb',
    'reserved_3',
    'wComportOffset',
    'reserved',
]
struct_S_IS_DEVICE_INFO_HEARTBEAT._fields_ = [
    ('reserved_1', BYTE * 24),
    ('dwRuntimeFirmwareVersion', DWORD),
    ('reserved_2', BYTE * 8),
    ('wTemperature', WORD),
    ('wLinkSpeed_Mb', WORD),
    ('reserved_3', BYTE * 6),
    ('wComportOffset', WORD),
    ('reserved', BYTE * 200),
]

IS_DEVICE_INFO_HEARTBEAT = struct_S_IS_DEVICE_INFO_HEARTBEAT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3594

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3610
class struct_S_IS_DEVICE_INFO_CONTROL(Structure):
    pass

struct_S_IS_DEVICE_INFO_CONTROL.__slots__ = [
    'dwDeviceId',
    'reserved',
]
struct_S_IS_DEVICE_INFO_CONTROL._fields_ = [
    ('dwDeviceId', DWORD),
    ('reserved', BYTE * 148),
]

IS_DEVICE_INFO_CONTROL = struct_S_IS_DEVICE_INFO_CONTROL # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3610

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3627
class struct_S_IS_DEVICE_INFO(Structure):
    pass

struct_S_IS_DEVICE_INFO.__slots__ = [
    'infoDevHeartbeat',
    'infoDevControl',
    'reserved',
]
struct_S_IS_DEVICE_INFO._fields_ = [
    ('infoDevHeartbeat', IS_DEVICE_INFO_HEARTBEAT),
    ('infoDevControl', IS_DEVICE_INFO_CONTROL),
    ('reserved', BYTE * 240),
]

IS_DEVICE_INFO = struct_S_IS_DEVICE_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3627

enum_E_IS_DEVICE_INFO_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3644

IS_DEVICE_INFO_CMD_GET_DEVICE_INFO = 33619969 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3644

IS_DEVICE_INFO_CMD = enum_E_IS_DEVICE_INFO_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3644

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3658
if hasattr(_libs['ueye_api_64'], 'is_DeviceInfo'):
    is_DeviceInfo = _libs['ueye_api_64'].is_DeviceInfo
    is_DeviceInfo.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_DeviceInfo.restype = INT

enum_E_IS_CALLBACK_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3681

IS_CALLBACK_CMD_INSTALL = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3681

IS_CALLBACK_CMD_UNINSTALL = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3681

IS_CALLBACK_CMD = enum_E_IS_CALLBACK_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3681

enum_E_IS_CALLBACK_EVENT = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3701

IS_CALLBACK_EV_IMGPOSTPROC_START = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3701

IS_CALLBACK_EVENT = enum_E_IS_CALLBACK_EVENT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3701

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3725
class struct_S_IS_CALLBACK_EVCTX_DATA_PROCESSING(Structure):
    pass

struct_S_IS_CALLBACK_EVCTX_DATA_PROCESSING.__slots__ = [
    'pSrcBuf',
    'cbSrcBuf',
    'pDestBuf',
    'cbDestBuf',
]
struct_S_IS_CALLBACK_EVCTX_DATA_PROCESSING._fields_ = [
    ('pSrcBuf', POINTER(None)),
    ('cbSrcBuf', UINT),
    ('pDestBuf', POINTER(None)),
    ('cbDestBuf', UINT),
]

IS_CALLBACK_EVCTX_DATA_PROCESSING = struct_S_IS_CALLBACK_EVCTX_DATA_PROCESSING # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3725

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3751
class struct_S_IS_CALLBACK_EVCTX_IMAGE_PROCESSING(Structure):
    pass

struct_S_IS_CALLBACK_EVCTX_IMAGE_PROCESSING.__slots__ = [
    'bufferInfo',
]
struct_S_IS_CALLBACK_EVCTX_IMAGE_PROCESSING._fields_ = [
    ('bufferInfo', IS_CALLBACK_EVCTX_DATA_PROCESSING),
]

IS_CALLBACK_EVCTX_IMAGE_PROCESSING = struct_S_IS_CALLBACK_EVCTX_IMAGE_PROCESSING # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3751

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3771
class struct_S_IS_CALLBACK_FDBK_IMAGE_PROCESSING(Structure):
    pass

struct_S_IS_CALLBACK_FDBK_IMAGE_PROCESSING.__slots__ = [
    'nDummy',
]
struct_S_IS_CALLBACK_FDBK_IMAGE_PROCESSING._fields_ = [
    ('nDummy', UINT),
]

IS_CALLBACK_FDBK_IMAGE_PROCESSING = struct_S_IS_CALLBACK_FDBK_IMAGE_PROCESSING # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3771

IS_CALLBACK_FUNC = CFUNCTYPE(UNCHECKED(INT), POINTER(None), POINTER(None), POINTER(None)) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3789

HIDS_CALLBACK = HIDS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3797

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3834
class struct_S_IS_CALLBACK_INSTALLATION_DATA(Structure):
    pass

struct_S_IS_CALLBACK_INSTALLATION_DATA.__slots__ = [
    'nEvent',
    'pfFunc',
    'pUserContext',
    'hCallback',
]
struct_S_IS_CALLBACK_INSTALLATION_DATA._fields_ = [
    ('nEvent', UINT),
    ('pfFunc', IS_CALLBACK_FUNC),
    ('pUserContext', POINTER(None)),
    ('hCallback', HIDS_CALLBACK),
]

IS_CALLBACK_INSTALLATION_DATA = struct_S_IS_CALLBACK_INSTALLATION_DATA # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3834

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3846
if hasattr(_libs['ueye_api_64'], 'is_Callback'):
    is_Callback = _libs['ueye_api_64'].is_Callback
    is_Callback.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Callback.restype = INT

enum_E_IS_OPTIMAL_CAMERA_TIMING_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3864

IS_OPTIMAL_CAMERA_TIMING_CMD_GET_PIXELCLOCK = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3864

IS_OPTIMAL_CAMERA_TIMING_CMD_GET_FRAMERATE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3864

IS_OPTIMAL_CAMERA_TIMING_CMD = enum_E_IS_OPTIMAL_CAMERA_TIMING_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3864

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3879
class struct_S_IS_OPTIMAL_CAMERA_TIMING(Structure):
    pass

struct_S_IS_OPTIMAL_CAMERA_TIMING.__slots__ = [
    's32Mode',
    's32TimeoutFineTuning',
    'ps32PixelClock',
    'pdFramerate',
]
struct_S_IS_OPTIMAL_CAMERA_TIMING._fields_ = [
    ('s32Mode', INT),
    ('s32TimeoutFineTuning', INT),
    ('ps32PixelClock', POINTER(INT)),
    ('pdFramerate', POINTER(c_double)),
]

IS_OPTIMAL_CAMERA_TIMING = struct_S_IS_OPTIMAL_CAMERA_TIMING # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3879

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3892
if hasattr(_libs['ueye_api_64'], 'is_OptimalCameraTiming'):
    is_OptimalCameraTiming = _libs['ueye_api_64'].is_OptimalCameraTiming
    is_OptimalCameraTiming.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_OptimalCameraTiming.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3905
class struct_anon_210(Structure):
    pass

struct_anon_210.__slots__ = [
    'by1',
    'by2',
    'by3',
    'by4',
]
struct_anon_210._fields_ = [
    ('by1', BYTE),
    ('by2', BYTE),
    ('by3', BYTE),
    ('by4', BYTE),
]

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3915
class union__UEYE_ETH_ADDR_IPV4(Union):
    pass

union__UEYE_ETH_ADDR_IPV4.__slots__ = [
    'by',
    'dwAddr',
]
union__UEYE_ETH_ADDR_IPV4._fields_ = [
    ('by', struct_anon_210),
    ('dwAddr', DWORD),
]

UEYE_ETH_ADDR_IPV4 = union__UEYE_ETH_ADDR_IPV4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3915

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3905
class struct_anon_211(Structure):
    pass

struct_anon_211.__slots__ = [
    'by1',
    'by2',
    'by3',
    'by4',
]
struct_anon_211._fields_ = [
    ('by1', BYTE),
    ('by2', BYTE),
    ('by3', BYTE),
    ('by4', BYTE),
]

PUEYE_ETH_ADDR_IPV4 = POINTER(union__UEYE_ETH_ADDR_IPV4) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3915

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3922
class struct__UEYE_ETH_ADDR_MAC(Structure):
    pass

struct__UEYE_ETH_ADDR_MAC.__slots__ = [
    'abyOctet',
]
struct__UEYE_ETH_ADDR_MAC._fields_ = [
    ('abyOctet', BYTE * 6),
]

UEYE_ETH_ADDR_MAC = struct__UEYE_ETH_ADDR_MAC # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3922

PUEYE_ETH_ADDR_MAC = POINTER(struct__UEYE_ETH_ADDR_MAC) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3922

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3932
class struct__UEYE_ETH_IP_CONFIGURATION(Structure):
    pass

struct__UEYE_ETH_IP_CONFIGURATION.__slots__ = [
    'ipAddress',
    'ipSubnetmask',
    'reserved',
]
struct__UEYE_ETH_IP_CONFIGURATION._fields_ = [
    ('ipAddress', UEYE_ETH_ADDR_IPV4),
    ('ipSubnetmask', UEYE_ETH_ADDR_IPV4),
    ('reserved', BYTE * 4),
]

UEYE_ETH_IP_CONFIGURATION = struct__UEYE_ETH_IP_CONFIGURATION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3932

PUEYE_ETH_IP_CONFIGURATION = POINTER(struct__UEYE_ETH_IP_CONFIGURATION) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3932

enum__UEYE_ETH_DEVICESTATUS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_READY_TO_OPERATE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_TESTING_IP_CURRENT = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_TESTING_IP_PERSISTENT = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_TESTING_IP_RANGE = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_INAPPLICABLE_IP_CURRENT = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_INAPPLICABLE_IP_PERSISTENT = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_INAPPLICABLE_IP_RANGE = 64 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_UNPAIRED = 256 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_PAIRING_IN_PROGRESS = 512 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_PAIRED = 1024 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_FORCE_100MBPS = 4096 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_NO_COMPORT = 8192 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_RECEIVING_FW_STARTER = 65536 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_RECEIVING_FW_RUNTIME = 131072 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_INAPPLICABLE_FW_RUNTIME = 262144 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_INAPPLICABLE_FW_STARTER = 524288 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_REBOOTING_FW_RUNTIME = 1048576 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_REBOOTING_FW_STARTER = 2097152 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_REBOOTING_FW_FAILSAFE = 4194304 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

IS_ETH_DEVSTATUS_RUNTIME_FW_ERR0 = 2147483648L # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

UEYE_ETH_DEVICESTATUS = enum__UEYE_ETH_DEVICESTATUS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3964

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4019
class struct__UEYE_ETH_DEVICE_INFO_HEARTBEAT(Structure):
    pass

struct__UEYE_ETH_DEVICE_INFO_HEARTBEAT.__slots__ = [
    'abySerialNumber',
    'byDeviceType',
    'byCameraID',
    'wSensorID',
    'wSizeImgMem_MB',
    'reserved_1',
    'dwVerStarterFirmware',
    'dwVerRuntimeFirmware',
    'dwStatus',
    'reserved_2',
    'wTemperature',
    'wLinkSpeed_Mb',
    'macDevice',
    'wComportOffset',
    'ipcfgPersistentIpCfg',
    'ipcfgCurrentIpCfg',
    'macPairedHost',
    'reserved_4',
    'ipPairedHostIp',
    'ipAutoCfgIpRangeBegin',
    'ipAutoCfgIpRangeEnd',
    'abyUserSpace',
    'reserved_5',
    'reserved_6',
]
struct__UEYE_ETH_DEVICE_INFO_HEARTBEAT._fields_ = [
    ('abySerialNumber', BYTE * 12),
    ('byDeviceType', BYTE),
    ('byCameraID', BYTE),
    ('wSensorID', WORD),
    ('wSizeImgMem_MB', WORD),
    ('reserved_1', BYTE * 2),
    ('dwVerStarterFirmware', DWORD),
    ('dwVerRuntimeFirmware', DWORD),
    ('dwStatus', DWORD),
    ('reserved_2', BYTE * 4),
    ('wTemperature', WORD),
    ('wLinkSpeed_Mb', WORD),
    ('macDevice', UEYE_ETH_ADDR_MAC),
    ('wComportOffset', WORD),
    ('ipcfgPersistentIpCfg', UEYE_ETH_IP_CONFIGURATION),
    ('ipcfgCurrentIpCfg', UEYE_ETH_IP_CONFIGURATION),
    ('macPairedHost', UEYE_ETH_ADDR_MAC),
    ('reserved_4', BYTE * 2),
    ('ipPairedHostIp', UEYE_ETH_ADDR_IPV4),
    ('ipAutoCfgIpRangeBegin', UEYE_ETH_ADDR_IPV4),
    ('ipAutoCfgIpRangeEnd', UEYE_ETH_ADDR_IPV4),
    ('abyUserSpace', BYTE * 8),
    ('reserved_5', BYTE * 84),
    ('reserved_6', BYTE * 64),
]

UEYE_ETH_DEVICE_INFO_HEARTBEAT = struct__UEYE_ETH_DEVICE_INFO_HEARTBEAT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4019

PUEYE_ETH_DEVICE_INFO_HEARTBEAT = POINTER(struct__UEYE_ETH_DEVICE_INFO_HEARTBEAT) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4019

enum__UEYE_ETH_CONTROLSTATUS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_AVAILABLE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_ACCESSIBLE1 = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_ACCESSIBLE2 = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_PERSISTENT_IP_USED = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_COMPATIBLE = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_ADAPTER_ON_DHCP = 64 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_ADAPTER_SETUP_OK = 128 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_UNPAIRING_IN_PROGRESS = 256 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_PAIRING_IN_PROGRESS = 512 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_PAIRED = 4096 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_OPENED = 16384 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_FW_UPLOAD_STARTER = 65536 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_FW_UPLOAD_RUNTIME = 131072 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_REBOOTING = 1048576 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_BOOTBOOST_ENABLED = 16777216 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_BOOTBOOST_ACTIVE = 33554432 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_INITIALIZED = 134217728 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_TO_BE_DELETED = 1073741824 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

IS_ETH_CTRLSTATUS_TO_BE_REMOVED = 2147483648L # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

UEYE_ETH_CONTROLSTATUS = enum__UEYE_ETH_CONTROLSTATUS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4051

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4065
class struct__UEYE_ETH_DEVICE_INFO_CONTROL(Structure):
    pass

struct__UEYE_ETH_DEVICE_INFO_CONTROL.__slots__ = [
    'dwDeviceID',
    'dwControlStatus',
    'reserved_1',
    'reserved_2',
]
struct__UEYE_ETH_DEVICE_INFO_CONTROL._fields_ = [
    ('dwDeviceID', DWORD),
    ('dwControlStatus', DWORD),
    ('reserved_1', BYTE * 80),
    ('reserved_2', BYTE * 64),
]

UEYE_ETH_DEVICE_INFO_CONTROL = struct__UEYE_ETH_DEVICE_INFO_CONTROL # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4065

PUEYE_ETH_DEVICE_INFO_CONTROL = POINTER(struct__UEYE_ETH_DEVICE_INFO_CONTROL) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4065

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4073
class struct__UEYE_ETH_ETHERNET_CONFIGURATION(Structure):
    pass

struct__UEYE_ETH_ETHERNET_CONFIGURATION.__slots__ = [
    'ipcfg',
    'mac',
]
struct__UEYE_ETH_ETHERNET_CONFIGURATION._fields_ = [
    ('ipcfg', UEYE_ETH_IP_CONFIGURATION),
    ('mac', UEYE_ETH_ADDR_MAC),
]

UEYE_ETH_ETHERNET_CONFIGURATION = struct__UEYE_ETH_ETHERNET_CONFIGURATION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4073

PUEYE_ETH_ETHERNET_CONFIGURATION = POINTER(struct__UEYE_ETH_ETHERNET_CONFIGURATION) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4073

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4083
class struct__UEYE_ETH_AUTOCFG_IP_SETUP(Structure):
    pass

struct__UEYE_ETH_AUTOCFG_IP_SETUP.__slots__ = [
    'ipAutoCfgIpRangeBegin',
    'ipAutoCfgIpRangeEnd',
    'reserved',
]
struct__UEYE_ETH_AUTOCFG_IP_SETUP._fields_ = [
    ('ipAutoCfgIpRangeBegin', UEYE_ETH_ADDR_IPV4),
    ('ipAutoCfgIpRangeEnd', UEYE_ETH_ADDR_IPV4),
    ('reserved', BYTE * 4),
]

UEYE_ETH_AUTOCFG_IP_SETUP = struct__UEYE_ETH_AUTOCFG_IP_SETUP # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4083

PUEYE_ETH_AUTOCFG_IP_SETUP = POINTER(struct__UEYE_ETH_AUTOCFG_IP_SETUP) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4083

enum__UEYE_ETH_PACKETFILTER_SETUP = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4094

IS_ETH_PCKTFLT_PASSALL = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4094

IS_ETH_PCKTFLT_BLOCKUEGET = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4094

IS_ETH_PCKTFLT_BLOCKALL = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4094

UEYE_ETH_PACKETFILTER_SETUP = enum__UEYE_ETH_PACKETFILTER_SETUP # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4094

enum__UEYE_ETH_LINKSPEED_SETUP = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4102

IS_ETH_LINKSPEED_100MB = 100 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4102

IS_ETH_LINKSPEED_1000MB = 1000 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4102

UEYE_ETH_LINKSPEED_SETUP = enum__UEYE_ETH_LINKSPEED_SETUP # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4102

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4131
class struct__UEYE_ETH_ADAPTER_INFO(Structure):
    pass

struct__UEYE_ETH_ADAPTER_INFO.__slots__ = [
    'dwAdapterID',
    'dwDeviceLinkspeed',
    'ethcfg',
    'reserved_2',
    'bIsEnabledDHCP',
    'autoCfgIp',
    'bIsValidAutoCfgIpRange',
    'dwCntDevicesKnown',
    'dwCntDevicesPaired',
    'wPacketFilter',
    'reserved_3',
    'reserved_4',
]
struct__UEYE_ETH_ADAPTER_INFO._fields_ = [
    ('dwAdapterID', DWORD),
    ('dwDeviceLinkspeed', DWORD),
    ('ethcfg', UEYE_ETH_ETHERNET_CONFIGURATION),
    ('reserved_2', BYTE * 2),
    ('bIsEnabledDHCP', BOOL),
    ('autoCfgIp', UEYE_ETH_AUTOCFG_IP_SETUP),
    ('bIsValidAutoCfgIpRange', BOOL),
    ('dwCntDevicesKnown', DWORD),
    ('dwCntDevicesPaired', DWORD),
    ('wPacketFilter', WORD),
    ('reserved_3', BYTE * 38),
    ('reserved_4', BYTE * 64),
]

UEYE_ETH_ADAPTER_INFO = struct__UEYE_ETH_ADAPTER_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4131

PUEYE_ETH_ADAPTER_INFO = POINTER(struct__UEYE_ETH_ADAPTER_INFO) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4131

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4143
class struct__UEYE_ETH_DRIVER_INFO(Structure):
    pass

struct__UEYE_ETH_DRIVER_INFO.__slots__ = [
    'dwMinVerStarterFirmware',
    'dwMaxVerStarterFirmware',
    'reserved_1',
    'reserved_2',
]
struct__UEYE_ETH_DRIVER_INFO._fields_ = [
    ('dwMinVerStarterFirmware', DWORD),
    ('dwMaxVerStarterFirmware', DWORD),
    ('reserved_1', BYTE * 8),
    ('reserved_2', BYTE * 64),
]

UEYE_ETH_DRIVER_INFO = struct__UEYE_ETH_DRIVER_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4143

PUEYE_ETH_DRIVER_INFO = POINTER(struct__UEYE_ETH_DRIVER_INFO) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4143

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4158
class struct__UEYE_ETH_DEVICE_INFO(Structure):
    pass

struct__UEYE_ETH_DEVICE_INFO.__slots__ = [
    'infoDevHeartbeat',
    'infoDevControl',
    'infoAdapter',
    'infoDriver',
]
struct__UEYE_ETH_DEVICE_INFO._fields_ = [
    ('infoDevHeartbeat', UEYE_ETH_DEVICE_INFO_HEARTBEAT),
    ('infoDevControl', UEYE_ETH_DEVICE_INFO_CONTROL),
    ('infoAdapter', UEYE_ETH_ADAPTER_INFO),
    ('infoDriver', UEYE_ETH_DRIVER_INFO),
]

UEYE_ETH_DEVICE_INFO = struct__UEYE_ETH_DEVICE_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4158

PUEYE_ETH_DEVICE_INFO = POINTER(struct__UEYE_ETH_DEVICE_INFO) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4158

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4165
class struct__UEYE_COMPORT_CONFIGURATION(Structure):
    pass

struct__UEYE_COMPORT_CONFIGURATION.__slots__ = [
    'wComportNumber',
]
struct__UEYE_COMPORT_CONFIGURATION._fields_ = [
    ('wComportNumber', WORD),
]

UEYE_COMPORT_CONFIGURATION = struct__UEYE_COMPORT_CONFIGURATION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4165

PUEYE_COMPORT_CONFIGURATION = POINTER(struct__UEYE_COMPORT_CONFIGURATION) # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4165

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4170
if hasattr(_libs['ueye_api_64'], 'is_SetStarterFirmware'):
    is_SetStarterFirmware = _libs['ueye_api_64'].is_SetStarterFirmware
    is_SetStarterFirmware.argtypes = [HIDS, POINTER(CHAR), UINT]
    is_SetStarterFirmware.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4171
if hasattr(_libs['ueye_api_64'], 'is_SetPacketFilter'):
    is_SetPacketFilter = _libs['ueye_api_64'].is_SetPacketFilter
    is_SetPacketFilter.argtypes = [INT, UINT]
    is_SetPacketFilter.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4172
if hasattr(_libs['ueye_api_64'], 'is_GetComportNumber'):
    is_GetComportNumber = _libs['ueye_api_64'].is_GetComportNumber
    is_GetComportNumber.argtypes = [HIDS, POINTER(UINT)]
    is_GetComportNumber.restype = INT

enum_E_IPCONFIG_CAPABILITY_FLAGS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4189

IPCONFIG_CAP_PERSISTENT_IP_SUPPORTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4189

IPCONFIG_CAP_AUTOCONFIG_IP_SUPPORTED = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4189

IPCONFIG_CAPABILITY_FLAGS = enum_E_IPCONFIG_CAPABILITY_FLAGS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4189

enum_E_IPCONFIG_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4260

IPCONFIG_CMD_QUERY_CAPABILITIES = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4260

IPCONFIG_CMD_SET_PERSISTENT_IP = 16842752 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4260

IPCONFIG_CMD_SET_AUTOCONFIG_IP = 17039360 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4260

IPCONFIG_CMD_SET_AUTOCONFIG_IP_BYDEVICE = 17039616 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4260

IPCONFIG_CMD_RESERVED1 = 17301504 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4260

IPCONFIG_CMD_GET_PERSISTENT_IP = 33619968 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4260

IPCONFIG_CMD_GET_AUTOCONFIG_IP = 33816576 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4260

IPCONFIG_CMD_GET_AUTOCONFIG_IP_BYDEVICE = 33816832 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4260

IPCONFIG_CMD = enum_E_IPCONFIG_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4260

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4274
if hasattr(_libs['ueye_api_64'], 'is_IpConfig'):
    is_IpConfig = _libs['ueye_api_64'].is_IpConfig
    is_IpConfig.argtypes = [INT, UEYE_ETH_ADDR_MAC, UINT, POINTER(None), UINT]
    is_IpConfig.restype = INT

enum_E_CONFIGURATION_SEL = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_CPU_IDLE_STATES_BIT_AC_VALUE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_CPU_IDLE_STATES_BIT_DC_VALUE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_IPO_NOT_ALLOWED = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_IPO_ALLOWED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_OPEN_MP_DISABLE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_OPEN_MP_ENABLE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_INITIAL_PARAMETERSET_NONE = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_INITIAL_PARAMETERSET_1 = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_INITIAL_PARAMETERSET_2 = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_ETH_CONFIGURATION_MODE_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_ETH_CONFIGURATION_MODE_ON = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_TRUSTED_PAIRING_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

IS_CONFIG_TRUSTED_PAIRING_ON = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

CONFIGURATION_SEL = enum_E_CONFIGURATION_SEL # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4301

enum_E_CONFIGURATION_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_CMD_GET_CAPABILITIES = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_CPU_IDLE_STATES_CMD_GET_ENABLE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_CPU_IDLE_STATES_CMD_SET_DISABLE_ON_OPEN = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_CPU_IDLE_STATES_CMD_GET_DISABLE_ON_OPEN = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_OPEN_MP_CMD_GET_ENABLE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_OPEN_MP_CMD_SET_ENABLE = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_OPEN_MP_CMD_GET_ENABLE_DEFAULT = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_INITIAL_PARAMETERSET_CMD_SET = 9 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_INITIAL_PARAMETERSET_CMD_GET = 10 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_ETH_CONFIGURATION_MODE_CMD_SET_ENABLE = 11 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_ETH_CONFIGURATION_MODE_CMD_GET_ENABLE = 12 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_IPO_CMD_GET_ALLOWED = 13 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_IPO_CMD_SET_ALLOWED = 14 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_CMD_TRUSTED_PAIRING_SET = 15 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_CMD_TRUSTED_PAIRING_GET = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

IS_CONFIG_CMD_TRUSTED_PAIRING_GET_DEFAULT = 17 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

CONFIGURATION_CMD = enum_E_CONFIGURATION_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4331

enum_E_CONFIGURATION_CAPS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4344

IS_CONFIG_CPU_IDLE_STATES_CAP_SUPPORTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4344

IS_CONFIG_OPEN_MP_CAP_SUPPORTED = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4344

IS_CONFIG_INITIAL_PARAMETERSET_CAP_SUPPORTED = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4344

IS_CONFIG_IPO_CAP_SUPPORTED = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4344

IS_CONFIG_TRUSTED_PAIRING_CAP_SUPPORTED = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4344

CONFIGURATION_CAPS = enum_E_CONFIGURATION_CAPS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4344

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4353
if hasattr(_libs['ueye_api_64'], 'is_Configuration'):
    is_Configuration = _libs['ueye_api_64'].is_Configuration
    is_Configuration.argtypes = [UINT, POINTER(None), UINT]
    is_Configuration.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4363
class struct_S_IO_FLASH_PARAMS(Structure):
    pass

struct_S_IO_FLASH_PARAMS.__slots__ = [
    's32Delay',
    'u32Duration',
]
struct_S_IO_FLASH_PARAMS._fields_ = [
    ('s32Delay', INT),
    ('u32Duration', UINT),
]

IO_FLASH_PARAMS = struct_S_IO_FLASH_PARAMS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4363

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4373
class struct_S_IO_PWM_PARAMS(Structure):
    pass

struct_S_IO_PWM_PARAMS.__slots__ = [
    'dblFrequency_Hz',
    'dblDutyCycle',
]
struct_S_IO_PWM_PARAMS._fields_ = [
    ('dblFrequency_Hz', c_double),
    ('dblDutyCycle', c_double),
]

IO_PWM_PARAMS = struct_S_IO_PWM_PARAMS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4373

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4387
class struct_S_IO_GPIO_CONFIGURATION(Structure):
    pass

struct_S_IO_GPIO_CONFIGURATION.__slots__ = [
    'u32Gpio',
    'u32Caps',
    'u32Configuration',
    'u32State',
    'u32Reserved',
]
struct_S_IO_GPIO_CONFIGURATION._fields_ = [
    ('u32Gpio', UINT),
    ('u32Caps', UINT),
    ('u32Configuration', UINT),
    ('u32State', UINT),
    ('u32Reserved', UINT * 12),
]

IO_GPIO_CONFIGURATION = struct_S_IO_GPIO_CONFIGURATION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4387

enum_E_IO_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_GPIOS_GET_SUPPORTED = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_GPIOS_GET_SUPPORTED_INPUTS = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_GPIOS_GET_SUPPORTED_OUTPUTS = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_GPIOS_GET_DIRECTION = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_GPIOS_SET_DIRECTION = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_GPIOS_GET_STATE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_GPIOS_SET_STATE = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_LED_GET_STATE = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_LED_SET_STATE = 9 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_LED_TOGGLE_STATE = 10 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_GET_GLOBAL_PARAMS = 11 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_APPLY_GLOBAL_PARAMS = 12 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_GET_SUPPORTED_GPIOS = 13 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_GET_PARAMS_MIN = 14 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_GET_PARAMS_MAX = 15 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_GET_PARAMS_INC = 16 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_GET_PARAMS = 17 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_SET_PARAMS = 18 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_GET_MODE = 19 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_SET_MODE = 20 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_PWM_GET_SUPPORTED_GPIOS = 21 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_PWM_GET_PARAMS_MIN = 22 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_PWM_GET_PARAMS_MAX = 23 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_PWM_GET_PARAMS_INC = 24 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_PWM_GET_PARAMS = 25 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_PWM_SET_PARAMS = 26 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_PWM_GET_MODE = 27 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_PWM_SET_MODE = 28 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_GPIOS_GET_CONFIGURATION = 29 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_GPIOS_SET_CONFIGURATION = 30 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_GET_GPIO_PARAMS_MIN = 31 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_SET_GPIO_PARAMS = 32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_GET_AUTO_FREERUN_DEFAULT = 33 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_GET_AUTO_FREERUN = 34 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IS_IO_CMD_FLASH_SET_AUTO_FREERUN = 35 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

IO_CMD = enum_E_IO_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4474

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4484
if hasattr(_libs['ueye_api_64'], 'is_IO'):
    is_IO = _libs['ueye_api_64'].is_IO
    is_IO.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_IO.restype = INT

enum_E_AUTOPARAMETER_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4501

IS_AWB_CMD_GET_SUPPORTED_TYPES = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4501

IS_AWB_CMD_GET_TYPE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4501

IS_AWB_CMD_SET_TYPE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4501

IS_AWB_CMD_GET_ENABLE = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4501

IS_AWB_CMD_SET_ENABLE = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4501

IS_AWB_CMD_GET_SUPPORTED_RGB_COLOR_MODELS = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4501

IS_AWB_CMD_GET_RGB_COLOR_MODEL = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4501

IS_AWB_CMD_SET_RGB_COLOR_MODEL = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4501

AUTOPARAMETER_CMD = enum_E_AUTOPARAMETER_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4501

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4522
if hasattr(_libs['ueye_api_64'], 'is_AutoParameter'):
    is_AutoParameter = _libs['ueye_api_64'].is_AutoParameter
    is_AutoParameter.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_AutoParameter.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4538
class struct_anon_212(Structure):
    pass

struct_anon_212.__slots__ = [
    'pSourceBuffer',
    'pDestBuffer',
    'nDestPixelFormat',
    'nDestPixelConverter',
    'nDestGamma',
    'nDestEdgeEnhancement',
    'nDestColorCorrectionMode',
    'nDestSaturationU',
    'nDestSaturationV',
    'reserved',
]
struct_anon_212._fields_ = [
    ('pSourceBuffer', String),
    ('pDestBuffer', String),
    ('nDestPixelFormat', INT),
    ('nDestPixelConverter', INT),
    ('nDestGamma', INT),
    ('nDestEdgeEnhancement', INT),
    ('nDestColorCorrectionMode', INT),
    ('nDestSaturationU', INT),
    ('nDestSaturationV', INT),
    ('reserved', BYTE * 32),
]

BUFFER_CONVERSION_PARAMS = struct_anon_212 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4538

enum_E_CONVERT_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4548

IS_CONVERT_CMD_APPLY_PARAMS_AND_CONVERT_BUFFER = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4548

CONVERT_CMD = enum_E_CONVERT_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4548

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4559
if hasattr(_libs['ueye_api_64'], 'is_Convert'):
    is_Convert = _libs['ueye_api_64'].is_Convert
    is_Convert.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Convert.restype = INT

enum_E_PARAMETERSET_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4574

IS_PARAMETERSET_CMD_LOAD_EEPROM = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4574

IS_PARAMETERSET_CMD_LOAD_FILE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4574

IS_PARAMETERSET_CMD_SAVE_EEPROM = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4574

IS_PARAMETERSET_CMD_SAVE_FILE = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4574

IS_PARAMETERSET_CMD_GET_NUMBER_SUPPORTED = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4574

IS_PARAMETERSET_CMD_GET_HW_PARAMETERSET_AVAILABLE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4574

IS_PARAMETERSET_CMD_ERASE_HW_PARAMETERSET = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4574

PARAMETERSET_CMD = enum_E_PARAMETERSET_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4574

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4584
if hasattr(_libs['ueye_api_64'], 'is_ParameterSet'):
    is_ParameterSet = _libs['ueye_api_64'].is_ParameterSet
    is_ParameterSet.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_ParameterSet.restype = INT

enum_E_EDGE_ENHANCEMENT_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4597

IS_EDGE_ENHANCEMENT_CMD_GET_RANGE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4597

IS_EDGE_ENHANCEMENT_CMD_GET_DEFAULT = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4597

IS_EDGE_ENHANCEMENT_CMD_GET = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4597

IS_EDGE_ENHANCEMENT_CMD_SET = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4597

EDGE_ENHANCEMENT_CMD = enum_E_EDGE_ENHANCEMENT_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4597

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4608
if hasattr(_libs['ueye_api_64'], 'is_EdgeEnhancement'):
    is_EdgeEnhancement = _libs['ueye_api_64'].is_EdgeEnhancement
    is_EdgeEnhancement.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_EdgeEnhancement.restype = INT

enum_E_PIXELCLOCK_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4623

IS_PIXELCLOCK_CMD_GET_NUMBER = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4623

IS_PIXELCLOCK_CMD_GET_LIST = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4623

IS_PIXELCLOCK_CMD_GET_RANGE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4623

IS_PIXELCLOCK_CMD_GET_DEFAULT = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4623

IS_PIXELCLOCK_CMD_GET = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4623

IS_PIXELCLOCK_CMD_SET = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4623

PIXELCLOCK_CMD = enum_E_PIXELCLOCK_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4623

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4634
if hasattr(_libs['ueye_api_64'], 'is_PixelClock'):
    is_PixelClock = _libs['ueye_api_64'].is_PixelClock
    is_PixelClock.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_PixelClock.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4647
class struct_anon_213(Structure):
    pass

struct_anon_213.__slots__ = [
    'pwchFileName',
    'nFileType',
    'nQuality',
    'ppcImageMem',
    'pnImageID',
    'reserved',
]
struct_anon_213._fields_ = [
    ('pwchFileName', POINTER(c_wchar)),
    ('nFileType', UINT),
    ('nQuality', UINT),
    ('ppcImageMem', POINTER(POINTER(c_char))),
    ('pnImageID', POINTER(UINT)),
    ('reserved', BYTE * 32),
]

IMAGE_FILE_PARAMS = struct_anon_213 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4647

enum_E_IMAGE_FILE_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4660

IS_IMAGE_FILE_CMD_LOAD = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4660

IS_IMAGE_FILE_CMD_SAVE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4660

IMAGE_FILE_CMD = enum_E_IMAGE_FILE_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4660

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4671
if hasattr(_libs['ueye_api_64'], 'is_ImageFile'):
    is_ImageFile = _libs['ueye_api_64'].is_ImageFile
    is_ImageFile.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_ImageFile.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4683
class struct_S_IS_RANGE_S32(Structure):
    pass

struct_S_IS_RANGE_S32.__slots__ = [
    's32Min',
    's32Max',
    's32Inc',
]
struct_S_IS_RANGE_S32._fields_ = [
    ('s32Min', INT),
    ('s32Max', INT),
    ('s32Inc', INT),
]

IS_RANGE_S32 = struct_S_IS_RANGE_S32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4683

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4694
class struct_S_IS_RANGE_F64(Structure):
    pass

struct_S_IS_RANGE_F64.__slots__ = [
    'f64Min',
    'f64Max',
    'f64Inc',
]
struct_S_IS_RANGE_F64._fields_ = [
    ('f64Min', c_double),
    ('f64Max', c_double),
    ('f64Inc', c_double),
]

IS_RANGE_F64 = struct_S_IS_RANGE_F64 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4694

enum_E_BLACKLEVEL_MODES = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4704

IS_AUTO_BLACKLEVEL_OFF = 0 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4704

IS_AUTO_BLACKLEVEL_ON = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4704

BLACKLEVEL_MODES = enum_E_BLACKLEVEL_MODES # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4704

enum_E_BLACKLEVEL_CAPS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4715

IS_BLACKLEVEL_CAP_SET_AUTO_BLACKLEVEL = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4715

IS_BLACKLEVEL_CAP_SET_OFFSET = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4715

BLACKLEVEL_CAPS = enum_E_BLACKLEVEL_CAPS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4715

enum_E_BLACKLEVEL_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4731

IS_BLACKLEVEL_CMD_GET_CAPS = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4731

IS_BLACKLEVEL_CMD_GET_MODE_DEFAULT = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4731

IS_BLACKLEVEL_CMD_GET_MODE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4731

IS_BLACKLEVEL_CMD_SET_MODE = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4731

IS_BLACKLEVEL_CMD_GET_OFFSET_DEFAULT = 5 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4731

IS_BLACKLEVEL_CMD_GET_OFFSET_RANGE = 6 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4731

IS_BLACKLEVEL_CMD_GET_OFFSET = 7 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4731

IS_BLACKLEVEL_CMD_SET_OFFSET = 8 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4731

BLACKLEVEL_CMD = enum_E_BLACKLEVEL_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4731

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4741
if hasattr(_libs['ueye_api_64'], 'is_Blacklevel'):
    is_Blacklevel = _libs['ueye_api_64'].is_Blacklevel
    is_Blacklevel.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Blacklevel.restype = INT

enum_E_IMGBUF_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4754

IS_IMGBUF_DEVMEM_CMD_GET_AVAILABLE_ITERATIONS = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4754

IS_IMGBUF_DEVMEM_CMD_GET_ITERATION_INFO = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4754

IS_IMGBUF_DEVMEM_CMD_TRANSFER_IMAGE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4754

IS_IMGBUF_DEVMEM_CMD_RELEASE_ITERATIONS = 4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4754

IMGBUF_CMD = enum_E_IMGBUF_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4754

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4765
class struct_S_ID_RANGE(Structure):
    pass

struct_S_ID_RANGE.__slots__ = [
    's32First',
    's32Last',
]
struct_S_ID_RANGE._fields_ = [
    ('s32First', INT),
    ('s32Last', INT),
]

ID_RANGE = struct_S_ID_RANGE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4765

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4777
class struct_S_IMGBUF_ITERATION_INFO(Structure):
    pass

struct_S_IMGBUF_ITERATION_INFO.__slots__ = [
    'u32IterationID',
    'rangeImageID',
    'bReserved',
]
struct_S_IMGBUF_ITERATION_INFO._fields_ = [
    ('u32IterationID', UINT),
    ('rangeImageID', ID_RANGE),
    ('bReserved', BYTE * 52),
]

IMGBUF_ITERATION_INFO = struct_S_IMGBUF_ITERATION_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4777

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4788
class struct_S_IMGBUF_ITEM(Structure):
    pass

struct_S_IMGBUF_ITEM.__slots__ = [
    'u32IterationID',
    's32ImageID',
]
struct_S_IMGBUF_ITEM._fields_ = [
    ('u32IterationID', UINT),
    ('s32ImageID', INT),
]

IMGBUF_ITEM = struct_S_IMGBUF_ITEM # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4788

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4799
if hasattr(_libs['ueye_api_64'], 'is_ImageBuffer'):
    is_ImageBuffer = _libs['ueye_api_64'].is_ImageBuffer
    is_ImageBuffer.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_ImageBuffer.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4811
class struct_S_MEASURE_SHARPNESS_AOI_INFO(Structure):
    pass

struct_S_MEASURE_SHARPNESS_AOI_INFO.__slots__ = [
    'u32NumberAOI',
    'u32SharpnessValue',
    'rcAOI',
]
struct_S_MEASURE_SHARPNESS_AOI_INFO._fields_ = [
    ('u32NumberAOI', UINT),
    ('u32SharpnessValue', UINT),
    ('rcAOI', IS_RECT),
]

MEASURE_SHARPNESS_AOI_INFO = struct_S_MEASURE_SHARPNESS_AOI_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4811

enum_E_MEASURE_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4822

IS_MEASURE_CMD_SHARPNESS_AOI_SET = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4822

IS_MEASURE_CMD_SHARPNESS_AOI_INQUIRE = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4822

IS_MEASURE_CMD_SHARPNESS_AOI_SET_PRESET = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4822

MEASURE_CMD = enum_E_MEASURE_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4822

enum_E_MEASURE_SHARPNESS_AOI_PRESETS = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4831

IS_MEASURE_SHARPNESS_AOI_PRESET_1 = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4831

MEASURE_SHARPNESS_AOI_PRESETS = enum_E_MEASURE_SHARPNESS_AOI_PRESETS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4831

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4841
if hasattr(_libs['ueye_api_64'], 'is_Measure'):
    is_Measure = _libs['ueye_api_64'].is_Measure
    is_Measure.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Measure.restype = INT

IS_LUT_PRESET = INT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4866

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4876
class struct_anon_214(Structure):
    pass

struct_anon_214.__slots__ = [
    'dblValues',
    'bAllChannelsAreEqual',
]
struct_anon_214._fields_ = [
    ('dblValues', (c_double * 64) * 3),
    ('bAllChannelsAreEqual', BOOL),
]

IS_LUT_CONFIGURATION_64 = struct_anon_214 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4876

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4886
class struct_anon_215(Structure):
    pass

struct_anon_215.__slots__ = [
    'predefinedLutID',
    'lutConfiguration',
]
struct_anon_215._fields_ = [
    ('predefinedLutID', IS_LUT_PRESET),
    ('lutConfiguration', IS_LUT_CONFIGURATION_64),
]

IS_LUT_CONFIGURATION_PRESET_64 = struct_anon_215 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4886

IS_LUT_ENABLED_STATE = INT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4926

IS_LUT_MODE = INT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4927

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4946
class struct_anon_216(Structure):
    pass

struct_anon_216.__slots__ = [
    'bLUTEnabled',
    'nLUTStateID',
    'nLUTModeID',
    'nLUTBits',
]
struct_anon_216._fields_ = [
    ('bLUTEnabled', BOOL),
    ('nLUTStateID', INT),
    ('nLUTModeID', INT),
    ('nLUTBits', INT),
]

IS_LUT_STATE = struct_anon_216 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4946

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4964
class struct_anon_217(Structure):
    pass

struct_anon_217.__slots__ = [
    'bSupportLUTHardware',
    'bSupportLUTSoftware',
    'nBitsHardware',
    'nBitsSoftware',
    'nChannelsHardware',
    'nChannelsSoftware',
]
struct_anon_217._fields_ = [
    ('bSupportLUTHardware', BOOL),
    ('bSupportLUTSoftware', BOOL),
    ('nBitsHardware', INT),
    ('nBitsSoftware', INT),
    ('nChannelsHardware', INT),
    ('nChannelsSoftware', INT),
]

IS_LUT_SUPPORT_INFO = struct_anon_217 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4964

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4974
if hasattr(_libs['ueye_api_64'], 'is_LUT'):
    is_LUT = _libs['ueye_api_64'].is_LUT
    is_LUT.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_LUT.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4995
if hasattr(_libs['ueye_api_64'], 'is_Gamma'):
    is_Gamma = _libs['ueye_api_64'].is_Gamma
    is_Gamma.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Gamma.restype = INT

enum_E_IS_MEMORY_CMD = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5004

IS_MEMORY_GET_SIZE = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5004

IS_MEMORY_READ = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5004

IS_MEMORY_WRITE = 3 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5004

IS_MEMORY_CMD = enum_E_IS_MEMORY_CMD # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5004

enum_E_IS_MEMORY_DESCRIPTION = c_int # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5012

IS_MEMORY_USER_1 = 1 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5012

IS_MEMORY_USER_2 = 2 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5012

IS_MEMORY_DESCRIPTION = enum_E_IS_MEMORY_DESCRIPTION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5012

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5022
class struct_anon_218(Structure):
    pass

struct_anon_218.__slots__ = [
    'u32Description',
    'u32Offset',
    'pu8Data',
    'u32SizeOfData',
]
struct_anon_218._fields_ = [
    ('u32Description', UINT),
    ('u32Offset', UINT),
    ('pu8Data', POINTER(c_ubyte)),
    ('u32SizeOfData', UINT),
]

IS_MEMORY_ACCESS = struct_anon_218 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5022

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5030
class struct_anon_219(Structure):
    pass

struct_anon_219.__slots__ = [
    'u32Description',
    'u32SizeBytes',
]
struct_anon_219._fields_ = [
    ('u32Description', UINT),
    ('u32SizeBytes', UINT),
]

IS_MEMORY_SIZE = struct_anon_219 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5030

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5042
if hasattr(_libs['ueye_api_64'], 'is_Memory'):
    is_Memory = _libs['ueye_api_64'].is_Memory
    is_Memory.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Memory.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5053
class struct_anon_220(Structure):
    pass

struct_anon_220.__slots__ = [
    'nPosX',
    'nPosY',
    'nWidth',
    'nHeight',
    'nStatus',
]
struct_anon_220._fields_ = [
    ('nPosX', UINT),
    ('nPosY', UINT),
    ('nWidth', UINT),
    ('nHeight', UINT),
    ('nStatus', UINT),
]

IS_MULTI_AOI_DESCRIPTOR = struct_anon_220 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5053

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5061
class struct_anon_221(Structure):
    pass

struct_anon_221.__slots__ = [
    'nNumberOfAOIs',
    'pMultiAOIList',
]
struct_anon_221._fields_ = [
    ('nNumberOfAOIs', UINT),
    ('pMultiAOIList', POINTER(IS_MULTI_AOI_DESCRIPTOR)),
]

IS_MULTI_AOI_CONTAINER = struct_anon_221 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5061

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5070
class struct_anon_222(Structure):
    pass

struct_anon_222.__slots__ = [
    'ipCamera',
    'ipMulticast',
    'u32CameraId',
    'u32ErrorHandlingMode',
]
struct_anon_222._fields_ = [
    ('ipCamera', UEYE_ETH_ADDR_IPV4),
    ('ipMulticast', UEYE_ETH_ADDR_IPV4),
    ('u32CameraId', UINT),
    ('u32ErrorHandlingMode', UINT),
]

IS_PMC_READONLYDEVICEDESCRIPTOR = struct_anon_222 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5070

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5113
if hasattr(_libs['ueye_api_64'], 'is_Multicast'):
    is_Multicast = _libs['ueye_api_64'].is_Multicast
    is_Multicast.argtypes = [HIDS, UINT, POINTER(None), UINT]
    is_Multicast.restype = INT

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 32
def UEYE_VERSION(major, minor, build):
    return (((major << 24) + (minor << 16)) + build)

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 36
try:
    UEYE_VERSION_CODE = (UEYE_VERSION (4, 60, 0))
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 46
try:
    DRIVER_DLL_NAME = 'ueye_api_64.dll'
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 55
try:
    IS_COLORMODE_INVALID = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 56
try:
    IS_COLORMODE_MONOCHROME = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 57
try:
    IS_COLORMODE_BAYER = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 58
try:
    IS_COLORMODE_CBYCRY = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 59
try:
    IS_COLORMODE_JPEG = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 64
try:
    IS_SENSOR_INVALID = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 67
try:
    IS_SENSOR_UI141X_M = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 68
try:
    IS_SENSOR_UI141X_C = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 69
try:
    IS_SENSOR_UI144X_M = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 70
try:
    IS_SENSOR_UI144X_C = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 72
try:
    IS_SENSOR_UI154X_M = 48
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 73
try:
    IS_SENSOR_UI154X_C = 49
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 74
try:
    IS_SENSOR_UI145X_C = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 76
try:
    IS_SENSOR_UI146X_C = 10
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 77
try:
    IS_SENSOR_UI148X_M = 11
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 78
try:
    IS_SENSOR_UI148X_C = 12
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 80
try:
    IS_SENSOR_UI121X_M = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 81
try:
    IS_SENSOR_UI121X_C = 17
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 82
try:
    IS_SENSOR_UI122X_M = 18
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 83
try:
    IS_SENSOR_UI122X_C = 19
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 85
try:
    IS_SENSOR_UI164X_C = 21
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 87
try:
    IS_SENSOR_UI155X_C = 23
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 89
try:
    IS_SENSOR_UI1223_M = 24
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 90
try:
    IS_SENSOR_UI1223_C = 25
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 92
try:
    IS_SENSOR_UI149X_M = 62
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 93
try:
    IS_SENSOR_UI149X_C = 63
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 95
try:
    IS_SENSOR_UI1225_M = 34
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 96
try:
    IS_SENSOR_UI1225_C = 35
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 98
try:
    IS_SENSOR_UI1645_C = 37
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 99
try:
    IS_SENSOR_UI1555_C = 39
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 100
try:
    IS_SENSOR_UI1545_M = 40
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 101
try:
    IS_SENSOR_UI1545_C = 41
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 102
try:
    IS_SENSOR_UI1455_C = 43
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 103
try:
    IS_SENSOR_UI1465_C = 45
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 104
try:
    IS_SENSOR_UI1485_M = 46
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 105
try:
    IS_SENSOR_UI1485_C = 47
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 106
try:
    IS_SENSOR_UI1495_M = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 107
try:
    IS_SENSOR_UI1495_C = 65
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 109
try:
    IS_SENSOR_UI112X_M = 74
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 110
try:
    IS_SENSOR_UI112X_C = 75
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 112
try:
    IS_SENSOR_UI1008_M = 76
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 113
try:
    IS_SENSOR_UI1008_C = 77
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 115
try:
    IS_SENSOR_UIF005_M = 118
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 116
try:
    IS_SENSOR_UIF005_C = 119
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 118
try:
    IS_SENSOR_UI1005_M = 522
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 119
try:
    IS_SENSOR_UI1005_C = 523
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 121
try:
    IS_SENSOR_UI1240_M = 80
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 122
try:
    IS_SENSOR_UI1240_C = 81
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 123
try:
    IS_SENSOR_UI1240_NIR = 98
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 125
try:
    IS_SENSOR_UI1240LE_M = 84
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 126
try:
    IS_SENSOR_UI1240LE_C = 85
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 127
try:
    IS_SENSOR_UI1240LE_NIR = 100
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 129
try:
    IS_SENSOR_UI1240ML_M = 102
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 130
try:
    IS_SENSOR_UI1240ML_C = 103
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 131
try:
    IS_SENSOR_UI1240ML_NIR = 512
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 133
try:
    IS_SENSOR_UI1243_M_SMI = 120
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 134
try:
    IS_SENSOR_UI1243_C_SMI = 121
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 136
try:
    IS_SENSOR_UI1543_M = 50
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 137
try:
    IS_SENSOR_UI1543_C = 51
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 139
try:
    IS_SENSOR_UI1544_M = 58
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 140
try:
    IS_SENSOR_UI1544_C = 59
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 141
try:
    IS_SENSOR_UI1543_M_WO = 60
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 142
try:
    IS_SENSOR_UI1543_C_WO = 61
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 143
try:
    IS_SENSOR_UI1453_C = 53
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 144
try:
    IS_SENSOR_UI1463_C = 55
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 145
try:
    IS_SENSOR_UI1483_M = 56
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 146
try:
    IS_SENSOR_UI1483_C = 57
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 147
try:
    IS_SENSOR_UI1493_M = 78
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 148
try:
    IS_SENSOR_UI1493_C = 79
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 150
try:
    IS_SENSOR_UI1463_M_WO = 68
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 151
try:
    IS_SENSOR_UI1463_C_WO = 69
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 153
try:
    IS_SENSOR_UI1553_C_WN = 71
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 154
try:
    IS_SENSOR_UI1483_M_WO = 72
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 155
try:
    IS_SENSOR_UI1483_C_WO = 73
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 157
try:
    IS_SENSOR_UI1580_M = 90
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 158
try:
    IS_SENSOR_UI1580_C = 91
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 159
try:
    IS_SENSOR_UI1580LE_M = 96
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 160
try:
    IS_SENSOR_UI1580LE_C = 97
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 162
try:
    IS_SENSOR_UI1360M = 104
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 163
try:
    IS_SENSOR_UI1360C = 105
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 164
try:
    IS_SENSOR_UI1360NIR = 530
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 166
try:
    IS_SENSOR_UI1370M = 106
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 167
try:
    IS_SENSOR_UI1370C = 107
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 168
try:
    IS_SENSOR_UI1370NIR = 532
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 170
try:
    IS_SENSOR_UI1250_M = 108
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 171
try:
    IS_SENSOR_UI1250_C = 109
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 172
try:
    IS_SENSOR_UI1250_NIR = 110
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 174
try:
    IS_SENSOR_UI1250LE_M = 112
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 175
try:
    IS_SENSOR_UI1250LE_C = 113
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 176
try:
    IS_SENSOR_UI1250LE_NIR = 114
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 178
try:
    IS_SENSOR_UI1250ML_M = 116
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 179
try:
    IS_SENSOR_UI1250ML_C = 117
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 180
try:
    IS_SENSOR_UI1250ML_NIR = 514
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 182
try:
    IS_SENSOR_XS = 523
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 184
try:
    IS_SENSOR_UI1493_M_AR = 516
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 185
try:
    IS_SENSOR_UI1493_C_AR = 517
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 187
try:
    IS_SENSOR_UI1060_M = 538
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 188
try:
    IS_SENSOR_UI1060_C = 539
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 190
try:
    IS_SENSOR_UI1013XC = 541
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 194
try:
    IS_SENSOR_UI223X_M = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 195
try:
    IS_SENSOR_UI223X_C = 129
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 197
try:
    IS_SENSOR_UI241X_M = 130
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 198
try:
    IS_SENSOR_UI241X_C = 131
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 200
try:
    IS_SENSOR_UI234X_M = 132
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 201
try:
    IS_SENSOR_UI234X_C = 133
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 203
try:
    IS_SENSOR_UI221X_M = 136
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 204
try:
    IS_SENSOR_UI221X_C = 137
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 206
try:
    IS_SENSOR_UI231X_M = 144
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 207
try:
    IS_SENSOR_UI231X_C = 145
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 209
try:
    IS_SENSOR_UI222X_M = 146
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 210
try:
    IS_SENSOR_UI222X_C = 147
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 212
try:
    IS_SENSOR_UI224X_M = 150
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 213
try:
    IS_SENSOR_UI224X_C = 151
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 215
try:
    IS_SENSOR_UI225X_M = 152
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 216
try:
    IS_SENSOR_UI225X_C = 153
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 218
try:
    IS_SENSOR_UI214X_M = 154
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 219
try:
    IS_SENSOR_UI214X_C = 155
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 221
try:
    IS_SENSOR_UI228X_M = 156
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 222
try:
    IS_SENSOR_UI228X_C = 157
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 224
try:
    IS_SENSOR_UI241X_M_R2 = 386
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 225
try:
    IS_SENSOR_UI251X_M = 386
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 226
try:
    IS_SENSOR_UI241X_C_R2 = 387
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 227
try:
    IS_SENSOR_UI251X_C = 387
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 229
try:
    IS_SENSOR_UI2130_M = 414
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 230
try:
    IS_SENSOR_UI2130_C = 415
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 232
try:
    IS_SENSOR_PASSIVE_MULTICAST = 3840
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 236
try:
    IS_NO_SUCCESS = (-1)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 237
try:
    IS_SUCCESS = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 238
try:
    IS_INVALID_CAMERA_HANDLE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 239
try:
    IS_INVALID_HANDLE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 241
try:
    IS_IO_REQUEST_FAILED = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 242
try:
    IS_CANT_OPEN_DEVICE = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 243
try:
    IS_CANT_CLOSE_DEVICE = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 244
try:
    IS_CANT_SETUP_MEMORY = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 245
try:
    IS_NO_HWND_FOR_ERROR_REPORT = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 246
try:
    IS_ERROR_MESSAGE_NOT_CREATED = 7
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 247
try:
    IS_ERROR_STRING_NOT_FOUND = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 248
try:
    IS_HOOK_NOT_CREATED = 9
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 249
try:
    IS_TIMER_NOT_CREATED = 10
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 250
try:
    IS_CANT_OPEN_REGISTRY = 11
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 251
try:
    IS_CANT_READ_REGISTRY = 12
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 252
try:
    IS_CANT_VALIDATE_BOARD = 13
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 253
try:
    IS_CANT_GIVE_BOARD_ACCESS = 14
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 254
try:
    IS_NO_IMAGE_MEM_ALLOCATED = 15
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 255
try:
    IS_CANT_CLEANUP_MEMORY = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 256
try:
    IS_CANT_COMMUNICATE_WITH_DRIVER = 17
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 257
try:
    IS_FUNCTION_NOT_SUPPORTED_YET = 18
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 258
try:
    IS_OPERATING_SYSTEM_NOT_SUPPORTED = 19
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 260
try:
    IS_INVALID_VIDEO_IN = 20
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 261
try:
    IS_INVALID_IMG_SIZE = 21
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 262
try:
    IS_INVALID_ADDRESS = 22
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 263
try:
    IS_INVALID_VIDEO_MODE = 23
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 264
try:
    IS_INVALID_AGC_MODE = 24
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 265
try:
    IS_INVALID_GAMMA_MODE = 25
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 266
try:
    IS_INVALID_SYNC_LEVEL = 26
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 267
try:
    IS_INVALID_CBARS_MODE = 27
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 268
try:
    IS_INVALID_COLOR_MODE = 28
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 269
try:
    IS_INVALID_SCALE_FACTOR = 29
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 270
try:
    IS_INVALID_IMAGE_SIZE = 30
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 271
try:
    IS_INVALID_IMAGE_POS = 31
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 272
try:
    IS_INVALID_CAPTURE_MODE = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 273
try:
    IS_INVALID_RISC_PROGRAM = 33
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 274
try:
    IS_INVALID_BRIGHTNESS = 34
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 275
try:
    IS_INVALID_CONTRAST = 35
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 276
try:
    IS_INVALID_SATURATION_U = 36
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 277
try:
    IS_INVALID_SATURATION_V = 37
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 278
try:
    IS_INVALID_HUE = 38
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 279
try:
    IS_INVALID_HOR_FILTER_STEP = 39
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 280
try:
    IS_INVALID_VERT_FILTER_STEP = 40
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 281
try:
    IS_INVALID_EEPROM_READ_ADDRESS = 41
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 282
try:
    IS_INVALID_EEPROM_WRITE_ADDRESS = 42
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 283
try:
    IS_INVALID_EEPROM_READ_LENGTH = 43
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 284
try:
    IS_INVALID_EEPROM_WRITE_LENGTH = 44
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 285
try:
    IS_INVALID_BOARD_INFO_POINTER = 45
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 286
try:
    IS_INVALID_DISPLAY_MODE = 46
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 287
try:
    IS_INVALID_ERR_REP_MODE = 47
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 288
try:
    IS_INVALID_BITS_PIXEL = 48
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 289
try:
    IS_INVALID_MEMORY_POINTER = 49
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 291
try:
    IS_FILE_WRITE_OPEN_ERROR = 50
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 292
try:
    IS_FILE_READ_OPEN_ERROR = 51
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 293
try:
    IS_FILE_READ_INVALID_BMP_ID = 52
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 294
try:
    IS_FILE_READ_INVALID_BMP_SIZE = 53
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 295
try:
    IS_FILE_READ_INVALID_BIT_COUNT = 54
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 296
try:
    IS_WRONG_KERNEL_VERSION = 55
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 298
try:
    IS_RISC_INVALID_XLENGTH = 60
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 299
try:
    IS_RISC_INVALID_YLENGTH = 61
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 300
try:
    IS_RISC_EXCEED_IMG_SIZE = 62
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 303
try:
    IS_DD_MAIN_FAILED = 70
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 304
try:
    IS_DD_PRIMSURFACE_FAILED = 71
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 305
try:
    IS_DD_SCRN_SIZE_NOT_SUPPORTED = 72
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 306
try:
    IS_DD_CLIPPER_FAILED = 73
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 307
try:
    IS_DD_CLIPPER_HWND_FAILED = 74
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 308
try:
    IS_DD_CLIPPER_CONNECT_FAILED = 75
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 309
try:
    IS_DD_BACKSURFACE_FAILED = 76
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 310
try:
    IS_DD_BACKSURFACE_IN_SYSMEM = 77
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 311
try:
    IS_DD_MDL_MALLOC_ERR = 78
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 312
try:
    IS_DD_MDL_SIZE_ERR = 79
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 313
try:
    IS_DD_CLIP_NO_CHANGE = 80
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 314
try:
    IS_DD_PRIMMEM_NULL = 81
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 315
try:
    IS_DD_BACKMEM_NULL = 82
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 316
try:
    IS_DD_BACKOVLMEM_NULL = 83
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 317
try:
    IS_DD_OVERLAYSURFACE_FAILED = 84
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 318
try:
    IS_DD_OVERLAYSURFACE_IN_SYSMEM = 85
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 319
try:
    IS_DD_OVERLAY_NOT_ALLOWED = 86
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 320
try:
    IS_DD_OVERLAY_COLKEY_ERR = 87
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 321
try:
    IS_DD_OVERLAY_NOT_ENABLED = 88
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 322
try:
    IS_DD_GET_DC_ERROR = 89
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 323
try:
    IS_DD_DDRAW_DLL_NOT_LOADED = 90
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 324
try:
    IS_DD_THREAD_NOT_CREATED = 91
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 325
try:
    IS_DD_CANT_GET_CAPS = 92
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 326
try:
    IS_DD_NO_OVERLAYSURFACE = 93
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 327
try:
    IS_DD_NO_OVERLAYSTRETCH = 94
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 328
try:
    IS_DD_CANT_CREATE_OVERLAYSURFACE = 95
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 329
try:
    IS_DD_CANT_UPDATE_OVERLAYSURFACE = 96
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 330
try:
    IS_DD_INVALID_STRETCH = 97
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 332
try:
    IS_EV_INVALID_EVENT_NUMBER = 100
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 333
try:
    IS_INVALID_MODE = 101
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 334
try:
    IS_CANT_FIND_FALCHOOK = 102
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 335
try:
    IS_CANT_FIND_HOOK = 102
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 336
try:
    IS_CANT_GET_HOOK_PROC_ADDR = 103
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 337
try:
    IS_CANT_CHAIN_HOOK_PROC = 104
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 338
try:
    IS_CANT_SETUP_WND_PROC = 105
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 339
try:
    IS_HWND_NULL = 106
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 340
try:
    IS_INVALID_UPDATE_MODE = 107
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 341
try:
    IS_NO_ACTIVE_IMG_MEM = 108
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 342
try:
    IS_CANT_INIT_EVENT = 109
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 343
try:
    IS_FUNC_NOT_AVAIL_IN_OS = 110
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 344
try:
    IS_CAMERA_NOT_CONNECTED = 111
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 345
try:
    IS_SEQUENCE_LIST_EMPTY = 112
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 346
try:
    IS_CANT_ADD_TO_SEQUENCE = 113
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 347
try:
    IS_LOW_OF_SEQUENCE_RISC_MEM = 114
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 348
try:
    IS_IMGMEM2FREE_USED_IN_SEQ = 115
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 349
try:
    IS_IMGMEM_NOT_IN_SEQUENCE_LIST = 116
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 350
try:
    IS_SEQUENCE_BUF_ALREADY_LOCKED = 117
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 351
try:
    IS_INVALID_DEVICE_ID = 118
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 352
try:
    IS_INVALID_BOARD_ID = 119
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 353
try:
    IS_ALL_DEVICES_BUSY = 120
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 354
try:
    IS_HOOK_BUSY = 121
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 355
try:
    IS_TIMED_OUT = 122
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 356
try:
    IS_NULL_POINTER = 123
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 357
try:
    IS_WRONG_HOOK_VERSION = 124
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 358
try:
    IS_INVALID_PARAMETER = 125
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 359
try:
    IS_NOT_ALLOWED = 126
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 360
try:
    IS_OUT_OF_MEMORY = 127
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 361
try:
    IS_INVALID_WHILE_LIVE = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 362
try:
    IS_ACCESS_VIOLATION = 129
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 363
try:
    IS_UNKNOWN_ROP_EFFECT = 130
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 364
try:
    IS_INVALID_RENDER_MODE = 131
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 365
try:
    IS_INVALID_THREAD_CONTEXT = 132
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 366
try:
    IS_NO_HARDWARE_INSTALLED = 133
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 367
try:
    IS_INVALID_WATCHDOG_TIME = 134
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 368
try:
    IS_INVALID_WATCHDOG_MODE = 135
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 369
try:
    IS_INVALID_PASSTHROUGH_IN = 136
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 370
try:
    IS_ERROR_SETTING_PASSTHROUGH_IN = 137
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 371
try:
    IS_FAILURE_ON_SETTING_WATCHDOG = 138
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 372
try:
    IS_NO_USB20 = 139
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 373
try:
    IS_CAPTURE_RUNNING = 140
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 375
try:
    IS_MEMORY_BOARD_ACTIVATED = 141
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 376
try:
    IS_MEMORY_BOARD_DEACTIVATED = 142
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 377
try:
    IS_NO_MEMORY_BOARD_CONNECTED = 143
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 378
try:
    IS_TOO_LESS_MEMORY = 144
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 379
try:
    IS_IMAGE_NOT_PRESENT = 145
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 380
try:
    IS_MEMORY_MODE_RUNNING = 146
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 381
try:
    IS_MEMORYBOARD_DISABLED = 147
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 383
try:
    IS_TRIGGER_ACTIVATED = 148
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 384
try:
    IS_WRONG_KEY = 150
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 385
try:
    IS_CRC_ERROR = 151
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 386
try:
    IS_NOT_YET_RELEASED = 152
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 387
try:
    IS_NOT_CALIBRATED = 153
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 388
try:
    IS_WAITING_FOR_KERNEL = 154
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 389
try:
    IS_NOT_SUPPORTED = 155
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 390
try:
    IS_TRIGGER_NOT_ACTIVATED = 156
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 391
try:
    IS_OPERATION_ABORTED = 157
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 392
try:
    IS_BAD_STRUCTURE_SIZE = 158
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 393
try:
    IS_INVALID_BUFFER_SIZE = 159
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 394
try:
    IS_INVALID_PIXEL_CLOCK = 160
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 395
try:
    IS_INVALID_EXPOSURE_TIME = 161
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 396
try:
    IS_AUTO_EXPOSURE_RUNNING = 162
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 397
try:
    IS_CANNOT_CREATE_BB_SURF = 163
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 398
try:
    IS_CANNOT_CREATE_BB_MIX = 164
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 399
try:
    IS_BB_OVLMEM_NULL = 165
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 400
try:
    IS_CANNOT_CREATE_BB_OVL = 166
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 401
try:
    IS_NOT_SUPP_IN_OVL_SURF_MODE = 167
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 402
try:
    IS_INVALID_SURFACE = 168
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 403
try:
    IS_SURFACE_LOST = 169
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 404
try:
    IS_RELEASE_BB_OVL_DC = 170
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 405
try:
    IS_BB_TIMER_NOT_CREATED = 171
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 406
try:
    IS_BB_OVL_NOT_EN = 172
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 407
try:
    IS_ONLY_IN_BB_MODE = 173
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 408
try:
    IS_INVALID_COLOR_FORMAT = 174
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 409
try:
    IS_INVALID_WB_BINNING_MODE = 175
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 410
try:
    IS_INVALID_I2C_DEVICE_ADDRESS = 176
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 411
try:
    IS_COULD_NOT_CONVERT = 177
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 412
try:
    IS_TRANSFER_ERROR = 178
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 413
try:
    IS_PARAMETER_SET_NOT_PRESENT = 179
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 414
try:
    IS_INVALID_CAMERA_TYPE = 180
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 415
try:
    IS_INVALID_HOST_IP_HIBYTE = 181
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 416
try:
    IS_CM_NOT_SUPP_IN_CURR_DISPLAYMODE = 182
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 417
try:
    IS_NO_IR_FILTER = 183
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 418
try:
    IS_STARTER_FW_UPLOAD_NEEDED = 184
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 420
try:
    IS_DR_LIBRARY_NOT_FOUND = 185
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 421
try:
    IS_DR_DEVICE_OUT_OF_MEMORY = 186
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 422
try:
    IS_DR_CANNOT_CREATE_SURFACE = 187
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 423
try:
    IS_DR_CANNOT_CREATE_VERTEX_BUFFER = 188
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 424
try:
    IS_DR_CANNOT_CREATE_TEXTURE = 189
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 425
try:
    IS_DR_CANNOT_LOCK_OVERLAY_SURFACE = 190
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 426
try:
    IS_DR_CANNOT_UNLOCK_OVERLAY_SURFACE = 191
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 427
try:
    IS_DR_CANNOT_GET_OVERLAY_DC = 192
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 428
try:
    IS_DR_CANNOT_RELEASE_OVERLAY_DC = 193
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 429
try:
    IS_DR_DEVICE_CAPS_INSUFFICIENT = 194
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 430
try:
    IS_INCOMPATIBLE_SETTING = 195
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 431
try:
    IS_DR_NOT_ALLOWED_WHILE_DC_IS_ACTIVE = 196
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 432
try:
    IS_DEVICE_ALREADY_PAIRED = 197
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 433
try:
    IS_SUBNETMASK_MISMATCH = 198
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 434
try:
    IS_SUBNET_MISMATCH = 199
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 435
try:
    IS_INVALID_IP_CONFIGURATION = 200
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 436
try:
    IS_DEVICE_NOT_COMPATIBLE = 201
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 437
try:
    IS_NETWORK_FRAME_SIZE_INCOMPATIBLE = 202
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 438
try:
    IS_NETWORK_CONFIGURATION_INVALID = 203
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 439
try:
    IS_ERROR_CPU_IDLE_STATES_CONFIGURATION = 204
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 440
try:
    IS_DEVICE_BUSY = 205
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 441
try:
    IS_SENSOR_INITIALIZATION_FAILED = 206
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 447
try:
    IS_OFF = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 448
try:
    IS_ON = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 449
try:
    IS_IGNORE_PARAMETER = (-1)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 455
try:
    IS_USE_DEVICE_ID = 32768L
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 456
try:
    IS_ALLOW_STARTER_FW_UPLOAD = 65536L
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 462
try:
    IS_GET_AUTO_EXIT_ENABLED = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 463
try:
    IS_DISABLE_AUTO_EXIT = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 464
try:
    IS_ENABLE_AUTO_EXIT = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 470
try:
    IS_GET_LIVE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 472
try:
    IS_WAIT = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 473
try:
    IS_DONT_WAIT = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 474
try:
    IS_FORCE_VIDEO_STOP = 16384
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 475
try:
    IS_FORCE_VIDEO_START = 16384
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 476
try:
    IS_USE_NEXT_MEM = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 482
try:
    IS_VIDEO_NOT_FINISH = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 483
try:
    IS_VIDEO_FINISH = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 489
try:
    IS_GET_RENDER_MODE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 491
try:
    IS_RENDER_DISABLED = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 492
try:
    IS_RENDER_NORMAL = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 493
try:
    IS_RENDER_FIT_TO_WINDOW = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 494
try:
    IS_RENDER_DOWNSCALE_1_2 = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 495
try:
    IS_RENDER_MIRROR_UPDOWN = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 497
try:
    IS_RENDER_PLANAR_COLOR_RED = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 498
try:
    IS_RENDER_PLANAR_COLOR_GREEN = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 499
try:
    IS_RENDER_PLANAR_COLOR_BLUE = 512
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 501
try:
    IS_RENDER_PLANAR_MONO_RED = 1024
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 502
try:
    IS_RENDER_PLANAR_MONO_GREEN = 2048
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 503
try:
    IS_RENDER_PLANAR_MONO_BLUE = 4096
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 505
try:
    IS_RENDER_ROTATE_90 = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 506
try:
    IS_RENDER_ROTATE_180 = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 507
try:
    IS_RENDER_ROTATE_270 = 8192
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 509
try:
    IS_USE_AS_DC_STRUCTURE = 16384
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 510
try:
    IS_USE_AS_DC_HANDLE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 516
try:
    IS_GET_EXTERNALTRIGGER = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 517
try:
    IS_GET_TRIGGER_STATUS = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 518
try:
    IS_GET_TRIGGER_MASK = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 519
try:
    IS_GET_TRIGGER_INPUTS = 32771
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 520
try:
    IS_GET_SUPPORTED_TRIGGER_MODE = 32772
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 521
try:
    IS_GET_TRIGGER_COUNTER = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 523
try:
    IS_SET_TRIGGER_MASK = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 524
try:
    IS_SET_TRIGGER_CONTINUOUS = 4096
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 525
try:
    IS_SET_TRIGGER_OFF = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 526
try:
    IS_SET_TRIGGER_HI_LO = (IS_SET_TRIGGER_CONTINUOUS | 1)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 527
try:
    IS_SET_TRIGGER_LO_HI = (IS_SET_TRIGGER_CONTINUOUS | 2)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 528
try:
    IS_SET_TRIGGER_SOFTWARE = (IS_SET_TRIGGER_CONTINUOUS | 8)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 529
try:
    IS_SET_TRIGGER_HI_LO_SYNC = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 530
try:
    IS_SET_TRIGGER_LO_HI_SYNC = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 531
try:
    IS_SET_TRIGGER_PRE_HI_LO = (IS_SET_TRIGGER_CONTINUOUS | 64)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 532
try:
    IS_SET_TRIGGER_PRE_LO_HI = (IS_SET_TRIGGER_CONTINUOUS | 128)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 534
try:
    IS_GET_TRIGGER_DELAY = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 535
try:
    IS_GET_MIN_TRIGGER_DELAY = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 536
try:
    IS_GET_MAX_TRIGGER_DELAY = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 537
try:
    IS_GET_TRIGGER_DELAY_GRANULARITY = 32771
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 545
try:
    IS_GET_PIXEL_CLOCK = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 546
try:
    IS_GET_DEFAULT_PIXEL_CLK = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 547
try:
    IS_GET_PIXEL_CLOCK_INC = 32773
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 550
try:
    IS_GET_FRAMERATE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 551
try:
    IS_GET_DEFAULT_FRAMERATE = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 557
try:
    IS_GET_MASTER_GAIN = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 558
try:
    IS_GET_RED_GAIN = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 559
try:
    IS_GET_GREEN_GAIN = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 560
try:
    IS_GET_BLUE_GAIN = 32771
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 561
try:
    IS_GET_DEFAULT_MASTER = 32772
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 562
try:
    IS_GET_DEFAULT_RED = 32773
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 563
try:
    IS_GET_DEFAULT_GREEN = 32774
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 564
try:
    IS_GET_DEFAULT_BLUE = 32775
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 565
try:
    IS_GET_GAINBOOST = 32776
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 566
try:
    IS_SET_GAINBOOST_ON = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 567
try:
    IS_SET_GAINBOOST_OFF = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 568
try:
    IS_GET_SUPPORTED_GAINBOOST = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 569
try:
    IS_MIN_GAIN = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 570
try:
    IS_MAX_GAIN = 100
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 576
try:
    IS_GET_MASTER_GAIN_FACTOR = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 577
try:
    IS_GET_RED_GAIN_FACTOR = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 578
try:
    IS_GET_GREEN_GAIN_FACTOR = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 579
try:
    IS_GET_BLUE_GAIN_FACTOR = 32771
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 580
try:
    IS_SET_MASTER_GAIN_FACTOR = 32772
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 581
try:
    IS_SET_RED_GAIN_FACTOR = 32773
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 582
try:
    IS_SET_GREEN_GAIN_FACTOR = 32774
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 583
try:
    IS_SET_BLUE_GAIN_FACTOR = 32775
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 584
try:
    IS_GET_DEFAULT_MASTER_GAIN_FACTOR = 32776
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 585
try:
    IS_GET_DEFAULT_RED_GAIN_FACTOR = 32777
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 586
try:
    IS_GET_DEFAULT_GREEN_GAIN_FACTOR = 32778
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 587
try:
    IS_GET_DEFAULT_BLUE_GAIN_FACTOR = 32779
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 588
try:
    IS_INQUIRE_MASTER_GAIN_FACTOR = 32780
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 589
try:
    IS_INQUIRE_RED_GAIN_FACTOR = 32781
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 590
try:
    IS_INQUIRE_GREEN_GAIN_FACTOR = 32782
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 591
try:
    IS_INQUIRE_BLUE_GAIN_FACTOR = 32783
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 597
try:
    IS_SET_GLOBAL_SHUTTER_ON = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 598
try:
    IS_SET_GLOBAL_SHUTTER_OFF = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 599
try:
    IS_GET_GLOBAL_SHUTTER = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 600
try:
    IS_GET_SUPPORTED_GLOBAL_SHUTTER = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 606
try:
    IS_GET_BL_COMPENSATION = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 607
try:
    IS_GET_BL_OFFSET = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 608
try:
    IS_GET_BL_DEFAULT_MODE = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 609
try:
    IS_GET_BL_DEFAULT_OFFSET = 32771
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 610
try:
    IS_GET_BL_SUPPORTED_MODE = 32772
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 612
try:
    IS_BL_COMPENSATION_DISABLE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 613
try:
    IS_BL_COMPENSATION_ENABLE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 614
try:
    IS_BL_COMPENSATION_OFFSET = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 616
try:
    IS_MIN_BL_OFFSET = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 617
try:
    IS_MAX_BL_OFFSET = 255
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 623
try:
    IS_GET_HW_GAMMA = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 624
try:
    IS_GET_HW_SUPPORTED_GAMMA = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 625
try:
    IS_SET_HW_GAMMA_OFF = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 626
try:
    IS_SET_HW_GAMMA_ON = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 634
try:
    IS_GET_SATURATION_U = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 635
try:
    IS_MIN_SATURATION_U = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 636
try:
    IS_MAX_SATURATION_U = 200
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 637
try:
    IS_DEFAULT_SATURATION_U = 100
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 638
try:
    IS_GET_SATURATION_V = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 639
try:
    IS_MIN_SATURATION_V = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 640
try:
    IS_MAX_SATURATION_V = 200
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 641
try:
    IS_DEFAULT_SATURATION_V = 100
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 649
try:
    IS_AOI_IMAGE_SET_AOI = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 650
try:
    IS_AOI_IMAGE_GET_AOI = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 651
try:
    IS_AOI_IMAGE_SET_POS = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 652
try:
    IS_AOI_IMAGE_GET_POS = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 653
try:
    IS_AOI_IMAGE_SET_SIZE = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 654
try:
    IS_AOI_IMAGE_GET_SIZE = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 655
try:
    IS_AOI_IMAGE_GET_POS_MIN = 7
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 656
try:
    IS_AOI_IMAGE_GET_SIZE_MIN = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 657
try:
    IS_AOI_IMAGE_GET_POS_MAX = 9
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 658
try:
    IS_AOI_IMAGE_GET_SIZE_MAX = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 659
try:
    IS_AOI_IMAGE_GET_POS_INC = 17
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 660
try:
    IS_AOI_IMAGE_GET_SIZE_INC = 18
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 661
try:
    IS_AOI_IMAGE_GET_POS_X_ABS = 19
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 662
try:
    IS_AOI_IMAGE_GET_POS_Y_ABS = 20
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 663
try:
    IS_AOI_IMAGE_GET_ORIGINAL_AOI = 21
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 666
try:
    IS_AOI_IMAGE_POS_ABSOLUTE = 268435456
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 669
try:
    IS_AOI_IMAGE_SET_POS_FAST = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 670
try:
    IS_AOI_IMAGE_GET_POS_FAST_SUPPORTED = 33
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 673
try:
    IS_AOI_AUTO_BRIGHTNESS_SET_AOI = 48
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 674
try:
    IS_AOI_AUTO_BRIGHTNESS_GET_AOI = 49
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 675
try:
    IS_AOI_AUTO_WHITEBALANCE_SET_AOI = 50
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 676
try:
    IS_AOI_AUTO_WHITEBALANCE_GET_AOI = 51
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 679
try:
    IS_AOI_MULTI_GET_SUPPORTED_MODES = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 680
try:
    IS_AOI_MULTI_SET_AOI = 512
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 681
try:
    IS_AOI_MULTI_GET_AOI = 1024
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 682
try:
    IS_AOI_MULTI_DISABLE_AOI = 2048
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 683
try:
    IS_AOI_MULTI_MODE_X_Y_AXES = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 684
try:
    IS_AOI_MULTI_MODE_Y_AXES = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 685
try:
    IS_AOI_MULTI_MODE_GET_MAX_NUMBER = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 686
try:
    IS_AOI_MULTI_MODE_GET_DEFAULT = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 687
try:
    IS_AOI_MULTI_MODE_ONLY_VERIFY_AOIS = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 688
try:
    IS_AOI_MULTI_MODE_GET_MINIMUM_SIZE = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 689
try:
    IS_AOI_MULTI_MODE_GET_ENABLED = 7
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 691
try:
    IS_AOI_MULTI_STATUS_SETBYUSER = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 692
try:
    IS_AOI_MULTI_STATUS_COMPLEMENT = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 693
try:
    IS_AOI_MULTI_STATUS_VALID = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 694
try:
    IS_AOI_MULTI_STATUS_CONFLICT = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 695
try:
    IS_AOI_MULTI_STATUS_ERROR = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 696
try:
    IS_AOI_MULTI_STATUS_UNUSED = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 699
try:
    IS_AOI_SEQUENCE_GET_SUPPORTED = 80
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 700
try:
    IS_AOI_SEQUENCE_SET_PARAMS = 81
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 701
try:
    IS_AOI_SEQUENCE_GET_PARAMS = 82
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 702
try:
    IS_AOI_SEQUENCE_SET_ENABLE = 83
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 703
try:
    IS_AOI_SEQUENCE_GET_ENABLE = 84
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 705
try:
    IS_AOI_SEQUENCE_INDEX_AOI_1 = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 706
try:
    IS_AOI_SEQUENCE_INDEX_AOI_2 = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 707
try:
    IS_AOI_SEQUENCE_INDEX_AOI_3 = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 708
try:
    IS_AOI_SEQUENCE_INDEX_AOI_4 = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 714
try:
    IS_GET_ROP_EFFECT = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 715
try:
    IS_GET_SUPPORTED_ROP_EFFECT = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 717
try:
    IS_SET_ROP_NONE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 718
try:
    IS_SET_ROP_MIRROR_UPDOWN = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 719
try:
    IS_SET_ROP_MIRROR_UPDOWN_ODD = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 720
try:
    IS_SET_ROP_MIRROR_UPDOWN_EVEN = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 721
try:
    IS_SET_ROP_MIRROR_LEFTRIGHT = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 727
try:
    IS_GET_SUBSAMPLING = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 728
try:
    IS_GET_SUPPORTED_SUBSAMPLING = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 729
try:
    IS_GET_SUBSAMPLING_TYPE = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 730
try:
    IS_GET_SUBSAMPLING_FACTOR_HORIZONTAL = 32772
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 731
try:
    IS_GET_SUBSAMPLING_FACTOR_VERTICAL = 32776
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 733
try:
    IS_SUBSAMPLING_DISABLE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 735
try:
    IS_SUBSAMPLING_2X_VERTICAL = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 736
try:
    IS_SUBSAMPLING_2X_HORIZONTAL = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 737
try:
    IS_SUBSAMPLING_4X_VERTICAL = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 738
try:
    IS_SUBSAMPLING_4X_HORIZONTAL = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 739
try:
    IS_SUBSAMPLING_3X_VERTICAL = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 740
try:
    IS_SUBSAMPLING_3X_HORIZONTAL = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 741
try:
    IS_SUBSAMPLING_5X_VERTICAL = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 742
try:
    IS_SUBSAMPLING_5X_HORIZONTAL = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 743
try:
    IS_SUBSAMPLING_6X_VERTICAL = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 744
try:
    IS_SUBSAMPLING_6X_HORIZONTAL = 512
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 745
try:
    IS_SUBSAMPLING_8X_VERTICAL = 1024
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 746
try:
    IS_SUBSAMPLING_8X_HORIZONTAL = 2048
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 747
try:
    IS_SUBSAMPLING_16X_VERTICAL = 4096
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 748
try:
    IS_SUBSAMPLING_16X_HORIZONTAL = 8192
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 750
try:
    IS_SUBSAMPLING_COLOR = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 751
try:
    IS_SUBSAMPLING_MONO = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 753
try:
    IS_SUBSAMPLING_MASK_VERTICAL = ((((((IS_SUBSAMPLING_2X_VERTICAL | IS_SUBSAMPLING_4X_VERTICAL) | IS_SUBSAMPLING_3X_VERTICAL) | IS_SUBSAMPLING_5X_VERTICAL) | IS_SUBSAMPLING_6X_VERTICAL) | IS_SUBSAMPLING_8X_VERTICAL) | IS_SUBSAMPLING_16X_VERTICAL)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 754
try:
    IS_SUBSAMPLING_MASK_HORIZONTAL = ((((((IS_SUBSAMPLING_2X_HORIZONTAL | IS_SUBSAMPLING_4X_HORIZONTAL) | IS_SUBSAMPLING_3X_HORIZONTAL) | IS_SUBSAMPLING_5X_HORIZONTAL) | IS_SUBSAMPLING_6X_HORIZONTAL) | IS_SUBSAMPLING_8X_HORIZONTAL) | IS_SUBSAMPLING_16X_HORIZONTAL)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 760
try:
    IS_GET_BINNING = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 761
try:
    IS_GET_SUPPORTED_BINNING = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 762
try:
    IS_GET_BINNING_TYPE = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 763
try:
    IS_GET_BINNING_FACTOR_HORIZONTAL = 32772
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 764
try:
    IS_GET_BINNING_FACTOR_VERTICAL = 32776
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 766
try:
    IS_BINNING_DISABLE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 768
try:
    IS_BINNING_2X_VERTICAL = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 769
try:
    IS_BINNING_2X_HORIZONTAL = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 770
try:
    IS_BINNING_4X_VERTICAL = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 771
try:
    IS_BINNING_4X_HORIZONTAL = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 772
try:
    IS_BINNING_3X_VERTICAL = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 773
try:
    IS_BINNING_3X_HORIZONTAL = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 774
try:
    IS_BINNING_5X_VERTICAL = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 775
try:
    IS_BINNING_5X_HORIZONTAL = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 776
try:
    IS_BINNING_6X_VERTICAL = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 777
try:
    IS_BINNING_6X_HORIZONTAL = 512
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 778
try:
    IS_BINNING_8X_VERTICAL = 1024
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 779
try:
    IS_BINNING_8X_HORIZONTAL = 2048
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 780
try:
    IS_BINNING_16X_VERTICAL = 4096
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 781
try:
    IS_BINNING_16X_HORIZONTAL = 8192
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 783
try:
    IS_BINNING_COLOR = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 784
try:
    IS_BINNING_MONO = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 786
try:
    IS_BINNING_MASK_VERTICAL = ((((((IS_BINNING_2X_VERTICAL | IS_BINNING_3X_VERTICAL) | IS_BINNING_4X_VERTICAL) | IS_BINNING_5X_VERTICAL) | IS_BINNING_6X_VERTICAL) | IS_BINNING_8X_VERTICAL) | IS_BINNING_16X_VERTICAL)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 787
try:
    IS_BINNING_MASK_HORIZONTAL = ((((((IS_BINNING_2X_HORIZONTAL | IS_BINNING_3X_HORIZONTAL) | IS_BINNING_4X_HORIZONTAL) | IS_BINNING_5X_HORIZONTAL) | IS_BINNING_6X_HORIZONTAL) | IS_BINNING_8X_HORIZONTAL) | IS_BINNING_16X_HORIZONTAL)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 793
try:
    IS_SET_ENABLE_AUTO_GAIN = 34816
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 794
try:
    IS_GET_ENABLE_AUTO_GAIN = 34817
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 795
try:
    IS_SET_ENABLE_AUTO_SHUTTER = 34818
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 796
try:
    IS_GET_ENABLE_AUTO_SHUTTER = 34819
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 797
try:
    IS_SET_ENABLE_AUTO_WHITEBALANCE = 34820
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 798
try:
    IS_GET_ENABLE_AUTO_WHITEBALANCE = 34821
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 799
try:
    IS_SET_ENABLE_AUTO_FRAMERATE = 34822
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 800
try:
    IS_GET_ENABLE_AUTO_FRAMERATE = 34823
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 801
try:
    IS_SET_ENABLE_AUTO_SENSOR_GAIN = 34824
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 802
try:
    IS_GET_ENABLE_AUTO_SENSOR_GAIN = 34825
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 803
try:
    IS_SET_ENABLE_AUTO_SENSOR_SHUTTER = 34832
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 804
try:
    IS_GET_ENABLE_AUTO_SENSOR_SHUTTER = 34833
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 805
try:
    IS_SET_ENABLE_AUTO_SENSOR_GAIN_SHUTTER = 34834
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 806
try:
    IS_GET_ENABLE_AUTO_SENSOR_GAIN_SHUTTER = 34835
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 807
try:
    IS_SET_ENABLE_AUTO_SENSOR_FRAMERATE = 34836
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 808
try:
    IS_GET_ENABLE_AUTO_SENSOR_FRAMERATE = 34837
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 809
try:
    IS_SET_ENABLE_AUTO_SENSOR_WHITEBALANCE = 34838
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 810
try:
    IS_GET_ENABLE_AUTO_SENSOR_WHITEBALANCE = 34839
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 812
try:
    IS_SET_AUTO_REFERENCE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 813
try:
    IS_GET_AUTO_REFERENCE = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 814
try:
    IS_SET_AUTO_GAIN_MAX = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 815
try:
    IS_GET_AUTO_GAIN_MAX = 32771
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 816
try:
    IS_SET_AUTO_SHUTTER_MAX = 32772
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 817
try:
    IS_GET_AUTO_SHUTTER_MAX = 32773
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 818
try:
    IS_SET_AUTO_SPEED = 32774
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 819
try:
    IS_GET_AUTO_SPEED = 32775
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 820
try:
    IS_SET_AUTO_WB_OFFSET = 32776
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 821
try:
    IS_GET_AUTO_WB_OFFSET = 32777
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 822
try:
    IS_SET_AUTO_WB_GAIN_RANGE = 32778
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 823
try:
    IS_GET_AUTO_WB_GAIN_RANGE = 32779
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 824
try:
    IS_SET_AUTO_WB_SPEED = 32780
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 825
try:
    IS_GET_AUTO_WB_SPEED = 32781
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 826
try:
    IS_SET_AUTO_WB_ONCE = 32782
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 827
try:
    IS_GET_AUTO_WB_ONCE = 32783
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 828
try:
    IS_SET_AUTO_BRIGHTNESS_ONCE = 32784
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 829
try:
    IS_GET_AUTO_BRIGHTNESS_ONCE = 32785
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 830
try:
    IS_SET_AUTO_HYSTERESIS = 32786
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 831
try:
    IS_GET_AUTO_HYSTERESIS = 32787
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 832
try:
    IS_GET_AUTO_HYSTERESIS_RANGE = 32788
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 833
try:
    IS_SET_AUTO_WB_HYSTERESIS = 32789
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 834
try:
    IS_GET_AUTO_WB_HYSTERESIS = 32790
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 835
try:
    IS_GET_AUTO_WB_HYSTERESIS_RANGE = 32791
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 836
try:
    IS_SET_AUTO_SKIPFRAMES = 32792
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 837
try:
    IS_GET_AUTO_SKIPFRAMES = 32793
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 838
try:
    IS_GET_AUTO_SKIPFRAMES_RANGE = 32794
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 839
try:
    IS_SET_AUTO_WB_SKIPFRAMES = 32795
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 840
try:
    IS_GET_AUTO_WB_SKIPFRAMES = 32796
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 841
try:
    IS_GET_AUTO_WB_SKIPFRAMES_RANGE = 32797
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 842
try:
    IS_SET_SENS_AUTO_SHUTTER_PHOTOM = 32798
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 843
try:
    IS_SET_SENS_AUTO_GAIN_PHOTOM = 32799
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 844
try:
    IS_GET_SENS_AUTO_SHUTTER_PHOTOM = 32800
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 845
try:
    IS_GET_SENS_AUTO_GAIN_PHOTOM = 32801
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 846
try:
    IS_GET_SENS_AUTO_SHUTTER_PHOTOM_DEF = 32802
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 847
try:
    IS_GET_SENS_AUTO_GAIN_PHOTOM_DEF = 32803
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 848
try:
    IS_SET_SENS_AUTO_CONTRAST_CORRECTION = 32804
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 849
try:
    IS_GET_SENS_AUTO_CONTRAST_CORRECTION = 32805
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 850
try:
    IS_GET_SENS_AUTO_CONTRAST_CORRECTION_RANGE = 32806
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 851
try:
    IS_GET_SENS_AUTO_CONTRAST_CORRECTION_INC = 32807
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 852
try:
    IS_GET_SENS_AUTO_CONTRAST_CORRECTION_DEF = 32808
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 853
try:
    IS_SET_SENS_AUTO_CONTRAST_FDT_AOI_ENABLE = 32809
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 854
try:
    IS_GET_SENS_AUTO_CONTRAST_FDT_AOI_ENABLE = 32816
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 855
try:
    IS_SET_SENS_AUTO_BACKLIGHT_COMP = 32817
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 856
try:
    IS_GET_SENS_AUTO_BACKLIGHT_COMP = 32818
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 857
try:
    IS_GET_SENS_AUTO_BACKLIGHT_COMP_RANGE = 32819
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 858
try:
    IS_GET_SENS_AUTO_BACKLIGHT_COMP_INC = 32820
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 859
try:
    IS_GET_SENS_AUTO_BACKLIGHT_COMP_DEF = 32821
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 860
try:
    IS_SET_ANTI_FLICKER_MODE = 32822
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 861
try:
    IS_GET_ANTI_FLICKER_MODE = 32823
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 862
try:
    IS_GET_ANTI_FLICKER_MODE_DEF = 32824
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 863
try:
    IS_GET_AUTO_REFERENCE_DEF = 32825
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 864
try:
    IS_GET_AUTO_WB_OFFSET_DEF = 32826
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 865
try:
    IS_GET_AUTO_WB_OFFSET_MIN = 32827
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 866
try:
    IS_GET_AUTO_WB_OFFSET_MAX = 32828
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 871
try:
    IS_MIN_AUTO_BRIGHT_REFERENCE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 872
try:
    IS_MAX_AUTO_BRIGHT_REFERENCE = 255
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 873
try:
    IS_DEFAULT_AUTO_BRIGHT_REFERENCE = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 874
try:
    IS_MIN_AUTO_SPEED = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 875
try:
    IS_MAX_AUTO_SPEED = 100
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 876
try:
    IS_DEFAULT_AUTO_SPEED = 50
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 878
try:
    IS_DEFAULT_AUTO_WB_OFFSET = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 879
try:
    IS_MIN_AUTO_WB_OFFSET = (-50)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 880
try:
    IS_MAX_AUTO_WB_OFFSET = 50
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 881
try:
    IS_DEFAULT_AUTO_WB_SPEED = 50
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 882
try:
    IS_MIN_AUTO_WB_SPEED = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 883
try:
    IS_MAX_AUTO_WB_SPEED = 100
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 884
try:
    IS_MIN_AUTO_WB_REFERENCE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 885
try:
    IS_MAX_AUTO_WB_REFERENCE = 255
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 891
try:
    IS_SET_AUTO_BRIGHT_AOI = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 892
try:
    IS_GET_AUTO_BRIGHT_AOI = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 893
try:
    IS_SET_IMAGE_AOI = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 894
try:
    IS_GET_IMAGE_AOI = 32771
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 895
try:
    IS_SET_AUTO_WB_AOI = 32772
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 896
try:
    IS_GET_AUTO_WB_AOI = 32773
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 904
try:
    IS_GET_COLOR_MODE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 907
try:
    IS_CM_FORMAT_PLANAR = 8192
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 908
try:
    IS_CM_FORMAT_MASK = 8192
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 911
try:
    IS_CM_ORDER_BGR = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 912
try:
    IS_CM_ORDER_RGB = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 913
try:
    IS_CM_ORDER_MASK = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 916
try:
    IS_CM_PREFER_PACKED_SOURCE_FORMAT = 16384
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 923
try:
    IS_CM_SENSOR_RAW8 = 11
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 926
try:
    IS_CM_SENSOR_RAW10 = 33
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 929
try:
    IS_CM_SENSOR_RAW12 = 27
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 932
try:
    IS_CM_SENSOR_RAW16 = 29
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 935
try:
    IS_CM_MONO8 = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 938
try:
    IS_CM_MONO10 = 34
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 941
try:
    IS_CM_MONO12 = 26
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 944
try:
    IS_CM_MONO16 = 28
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 947
try:
    IS_CM_BGR5_PACKED = (3 | IS_CM_ORDER_BGR)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 950
try:
    IS_CM_BGR565_PACKED = (2 | IS_CM_ORDER_BGR)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 953
try:
    IS_CM_RGB8_PACKED = (1 | IS_CM_ORDER_RGB)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 954
try:
    IS_CM_BGR8_PACKED = (1 | IS_CM_ORDER_BGR)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 957
try:
    IS_CM_RGBA8_PACKED = (0 | IS_CM_ORDER_RGB)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 958
try:
    IS_CM_BGRA8_PACKED = (0 | IS_CM_ORDER_BGR)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 961
try:
    IS_CM_RGBY8_PACKED = (24 | IS_CM_ORDER_RGB)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 962
try:
    IS_CM_BGRY8_PACKED = (24 | IS_CM_ORDER_BGR)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 965
try:
    IS_CM_RGB10_PACKED = (25 | IS_CM_ORDER_RGB)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 966
try:
    IS_CM_BGR10_PACKED = (25 | IS_CM_ORDER_BGR)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 969
try:
    IS_CM_RGB10_UNPACKED = (35 | IS_CM_ORDER_RGB)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 970
try:
    IS_CM_BGR10_UNPACKED = (35 | IS_CM_ORDER_BGR)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 973
try:
    IS_CM_RGB12_UNPACKED = (30 | IS_CM_ORDER_RGB)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 974
try:
    IS_CM_BGR12_UNPACKED = (30 | IS_CM_ORDER_BGR)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 977
try:
    IS_CM_RGBA12_UNPACKED = (31 | IS_CM_ORDER_RGB)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 978
try:
    IS_CM_BGRA12_UNPACKED = (31 | IS_CM_ORDER_BGR)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 980
try:
    IS_CM_JPEG = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 983
try:
    IS_CM_UYVY_PACKED = 12
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 984
try:
    IS_CM_UYVY_MONO_PACKED = 13
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 985
try:
    IS_CM_UYVY_BAYER_PACKED = 14
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 988
try:
    IS_CM_CBYCRY_PACKED = 23
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 991
try:
    IS_CM_RGB8_PLANAR = ((1 | IS_CM_ORDER_RGB) | IS_CM_FORMAT_PLANAR)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 996
try:
    IS_CM_ALL_POSSIBLE = 65535
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 997
try:
    IS_CM_MODE_MASK = 127
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1003
try:
    IS_HOTPIXEL_DISABLE_CORRECTION = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1004
try:
    IS_HOTPIXEL_ENABLE_SENSOR_CORRECTION = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1005
try:
    IS_HOTPIXEL_ENABLE_CAMERA_CORRECTION = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1006
try:
    IS_HOTPIXEL_ENABLE_SOFTWARE_USER_CORRECTION = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1007
try:
    IS_HOTPIXEL_DISABLE_SENSOR_CORRECTION = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1009
try:
    IS_HOTPIXEL_GET_CORRECTION_MODE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1010
try:
    IS_HOTPIXEL_GET_SUPPORTED_CORRECTION_MODES = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1012
try:
    IS_HOTPIXEL_GET_SOFTWARE_USER_LIST_EXISTS = 33024
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1013
try:
    IS_HOTPIXEL_GET_SOFTWARE_USER_LIST_NUMBER = 33025
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1014
try:
    IS_HOTPIXEL_GET_SOFTWARE_USER_LIST = 33026
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1015
try:
    IS_HOTPIXEL_SET_SOFTWARE_USER_LIST = 33027
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1016
try:
    IS_HOTPIXEL_SAVE_SOFTWARE_USER_LIST = 33028
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1017
try:
    IS_HOTPIXEL_LOAD_SOFTWARE_USER_LIST = 33029
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1019
try:
    IS_HOTPIXEL_GET_CAMERA_FACTORY_LIST_EXISTS = 33030
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1020
try:
    IS_HOTPIXEL_GET_CAMERA_FACTORY_LIST_NUMBER = 33031
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1021
try:
    IS_HOTPIXEL_GET_CAMERA_FACTORY_LIST = 33032
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1023
try:
    IS_HOTPIXEL_GET_CAMERA_USER_LIST_EXISTS = 33033
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1024
try:
    IS_HOTPIXEL_GET_CAMERA_USER_LIST_NUMBER = 33034
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1025
try:
    IS_HOTPIXEL_GET_CAMERA_USER_LIST = 33035
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1026
try:
    IS_HOTPIXEL_SET_CAMERA_USER_LIST = 33036
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1027
try:
    IS_HOTPIXEL_GET_CAMERA_USER_LIST_MAX_NUMBER = 33037
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1028
try:
    IS_HOTPIXEL_DELETE_CAMERA_USER_LIST = 33038
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1030
try:
    IS_HOTPIXEL_GET_MERGED_CAMERA_LIST_NUMBER = 33039
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1031
try:
    IS_HOTPIXEL_GET_MERGED_CAMERA_LIST = 33040
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1033
try:
    IS_HOTPIXEL_SAVE_SOFTWARE_USER_LIST_UNICODE = 33041
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1034
try:
    IS_HOTPIXEL_LOAD_SOFTWARE_USER_LIST_UNICODE = 33042
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1039
try:
    IS_GET_CCOR_MODE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1040
try:
    IS_GET_SUPPORTED_CCOR_MODE = 32769
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1041
try:
    IS_GET_DEFAULT_CCOR_MODE = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1042
try:
    IS_GET_CCOR_FACTOR = 32771
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1043
try:
    IS_GET_CCOR_FACTOR_MIN = 32772
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1044
try:
    IS_GET_CCOR_FACTOR_MAX = 32773
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1045
try:
    IS_GET_CCOR_FACTOR_DEFAULT = 32774
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1047
try:
    IS_CCOR_DISABLE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1048
try:
    IS_CCOR_ENABLE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1049
try:
    IS_CCOR_ENABLE_NORMAL = IS_CCOR_ENABLE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1050
try:
    IS_CCOR_ENABLE_BG40_ENHANCED = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1051
try:
    IS_CCOR_ENABLE_HQ_ENHANCED = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1052
try:
    IS_CCOR_SET_IR_AUTOMATIC = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1053
try:
    IS_CCOR_FACTOR = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1055
try:
    IS_CCOR_ENABLE_MASK = ((IS_CCOR_ENABLE_NORMAL | IS_CCOR_ENABLE_BG40_ENHANCED) | IS_CCOR_ENABLE_HQ_ENHANCED)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1061
try:
    IS_GET_BAYER_CV_MODE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1063
try:
    IS_SET_BAYER_CV_NORMAL = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1064
try:
    IS_SET_BAYER_CV_BETTER = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1065
try:
    IS_SET_BAYER_CV_BEST = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1071
try:
    IS_CONV_MODE_NONE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1072
try:
    IS_CONV_MODE_SOFTWARE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1073
try:
    IS_CONV_MODE_SOFTWARE_3X3 = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1074
try:
    IS_CONV_MODE_SOFTWARE_5X5 = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1075
try:
    IS_CONV_MODE_HARDWARE_3X3 = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1076
try:
    IS_CONV_MODE_OPENCL_3X3 = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1077
try:
    IS_CONV_MODE_OPENCL_5X5 = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1079
try:
    IS_CONV_MODE_JPEG = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1086
try:
    IS_GET_EDGE_ENHANCEMENT = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1088
try:
    IS_EDGE_EN_DISABLE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1089
try:
    IS_EDGE_EN_STRONG = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1090
try:
    IS_EDGE_EN_WEAK = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1096
try:
    IS_GET_WB_MODE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1098
try:
    IS_SET_WB_DISABLE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1099
try:
    IS_SET_WB_USER = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1100
try:
    IS_SET_WB_AUTO_ENABLE = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1101
try:
    IS_SET_WB_AUTO_ENABLE_ONCE = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1103
try:
    IS_SET_WB_DAYLIGHT_65 = 257
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1104
try:
    IS_SET_WB_COOL_WHITE = 258
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1105
try:
    IS_SET_WB_U30 = 259
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1106
try:
    IS_SET_WB_ILLUMINANT_A = 260
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1107
try:
    IS_SET_WB_HORIZON = 261
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1113
try:
    IS_EEPROM_MIN_USER_ADDRESS = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1114
try:
    IS_EEPROM_MAX_USER_ADDRESS = 63
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1115
try:
    IS_EEPROM_MAX_USER_SPACE = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1121
try:
    IS_GET_ERR_REP_MODE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1122
try:
    IS_ENABLE_ERR_REP = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1123
try:
    IS_DISABLE_ERR_REP = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1129
try:
    IS_GET_DISPLAY_MODE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1131
try:
    IS_SET_DM_DIB = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1132
try:
    IS_SET_DM_DIRECT3D = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1133
try:
    IS_SET_DM_OPENGL = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1135
try:
    IS_SET_DM_MONO = 2048
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1136
try:
    IS_SET_DM_BAYER = 4096
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1137
try:
    IS_SET_DM_YCBCR = 16384
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1143
try:
    DR_GET_OVERLAY_DC = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1144
try:
    DR_GET_MAX_OVERLAY_SIZE = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1145
try:
    DR_GET_OVERLAY_KEY_COLOR = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1146
try:
    DR_RELEASE_OVERLAY_DC = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1147
try:
    DR_SHOW_OVERLAY = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1148
try:
    DR_HIDE_OVERLAY = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1149
try:
    DR_SET_OVERLAY_SIZE = 7
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1150
try:
    DR_SET_OVERLAY_POSITION = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1151
try:
    DR_SET_OVERLAY_KEY_COLOR = 9
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1152
try:
    DR_SET_HWND = 10
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1153
try:
    DR_ENABLE_SCALING = 11
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1154
try:
    DR_DISABLE_SCALING = 12
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1155
try:
    DR_CLEAR_OVERLAY = 13
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1156
try:
    DR_ENABLE_SEMI_TRANSPARENT_OVERLAY = 14
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1157
try:
    DR_DISABLE_SEMI_TRANSPARENT_OVERLAY = 15
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1158
try:
    DR_CHECK_COMPATIBILITY = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1159
try:
    DR_SET_VSYNC_OFF = 17
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1160
try:
    DR_SET_VSYNC_AUTO = 18
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1161
try:
    DR_SET_USER_SYNC = 19
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1162
try:
    DR_GET_USER_SYNC_POSITION_RANGE = 20
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1163
try:
    DR_LOAD_OVERLAY_FROM_FILE = 21
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1164
try:
    DR_STEAL_NEXT_FRAME = 22
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1165
try:
    DR_SET_STEAL_FORMAT = 23
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1166
try:
    DR_GET_STEAL_FORMAT = 24
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1167
try:
    DR_ENABLE_IMAGE_SCALING = 25
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1168
try:
    DR_GET_OVERLAY_SIZE = 26
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1169
try:
    DR_CHECK_COLOR_MODE_SUPPORT = 27
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1170
try:
    DR_GET_OVERLAY_DATA = 28
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1171
try:
    DR_UPDATE_OVERLAY_DATA = 29
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1172
try:
    DR_GET_SUPPORTED = 30
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1177
try:
    IS_SAVE_USE_ACTUAL_IMAGE_SIZE = 65536
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1183
try:
    IS_RENUM_BY_CAMERA = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1184
try:
    IS_RENUM_BY_HOST = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1190
try:
    IS_SET_EVENT_ODD = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1191
try:
    IS_SET_EVENT_EVEN = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1192
try:
    IS_SET_EVENT_FRAME = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1193
try:
    IS_SET_EVENT_EXTTRIG = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1194
try:
    IS_SET_EVENT_VSYNC = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1195
try:
    IS_SET_EVENT_SEQ = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1196
try:
    IS_SET_EVENT_STEAL = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1197
try:
    IS_SET_EVENT_VPRES = 7
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1198
try:
    IS_SET_EVENT_CAPTURE_STATUS = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1199
try:
    IS_SET_EVENT_TRANSFER_FAILED = IS_SET_EVENT_CAPTURE_STATUS
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1200
try:
    IS_SET_EVENT_DEVICE_RECONNECTED = 9
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1201
try:
    IS_SET_EVENT_MEMORY_MODE_FINISH = 10
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1202
try:
    IS_SET_EVENT_FRAME_RECEIVED = 11
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1203
try:
    IS_SET_EVENT_WB_FINISHED = 12
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1204
try:
    IS_SET_EVENT_AUTOBRIGHTNESS_FINISHED = 13
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1205
try:
    IS_SET_EVENT_OVERLAY_DATA_LOST = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1206
try:
    IS_SET_EVENT_CAMERA_MEMORY = 17
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1207
try:
    IS_SET_EVENT_CONNECTIONSPEED_CHANGED = 18
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1208
try:
    IS_SET_EVENT_AUTOFOCUS_FINISHED = 19
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1209
try:
    IS_SET_EVENT_FIRST_PACKET_RECEIVED = 20
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1210
try:
    IS_SET_EVENT_PMC_IMAGE_PARAMS_CHANGED = 21
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1211
try:
    IS_SET_EVENT_DEVICE_PLUGGED_IN = 22
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1212
try:
    IS_SET_EVENT_DEVICE_UNPLUGGED = 23
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1215
try:
    IS_SET_EVENT_REMOVE = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1216
try:
    IS_SET_EVENT_REMOVAL = 129
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1217
try:
    IS_SET_EVENT_NEW_DEVICE = 130
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1218
try:
    IS_SET_EVENT_STATUS_CHANGED = 131
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1224
try:
    IS_UEYE_MESSAGE = (WM_USER + 256)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1225
try:
    IS_FRAME = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1226
try:
    IS_SEQUENCE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1227
try:
    IS_TRIGGER = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1228
try:
    IS_CAPTURE_STATUS = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1229
try:
    IS_TRANSFER_FAILED = IS_CAPTURE_STATUS
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1230
try:
    IS_DEVICE_RECONNECTED = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1231
try:
    IS_MEMORY_MODE_FINISH = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1232
try:
    IS_FRAME_RECEIVED = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1233
try:
    IS_GENERIC_ERROR = 7
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1234
try:
    IS_STEAL_VIDEO = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1235
try:
    IS_WB_FINISHED = 9
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1236
try:
    IS_AUTOBRIGHTNESS_FINISHED = 10
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1237
try:
    IS_OVERLAY_DATA_LOST = 11
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1238
try:
    IS_CAMERA_MEMORY = 12
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1239
try:
    IS_CONNECTIONSPEED_CHANGED = 13
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1240
try:
    IS_AUTOFOCUS_FINISHED = 14
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1241
try:
    IS_FIRST_PACKET_RECEIVED = 15
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1242
try:
    IS_PMC_IMAGE_PARAMS_CHANGED = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1243
try:
    IS_DEVICE_PLUGGED_IN = 17
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1244
try:
    IS_DEVICE_UNPLUGGED = 18
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1246
try:
    IS_DEVICE_REMOVED = 4096
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1247
try:
    IS_DEVICE_REMOVAL = 4097
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1248
try:
    IS_NEW_DEVICE = 4098
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1249
try:
    IS_DEVICE_STATUS_CHANGED = 4099
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1255
try:
    IS_GET_CAMERA_ID = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1261
try:
    IS_GET_STATUS = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1263
try:
    IS_EXT_TRIGGER_EVENT_CNT = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1264
try:
    IS_FIFO_OVR_CNT = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1265
try:
    IS_SEQUENCE_CNT = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1266
try:
    IS_LAST_FRAME_FIFO_OVR = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1267
try:
    IS_SEQUENCE_SIZE = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1268
try:
    IS_VIDEO_PRESENT = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1269
try:
    IS_STEAL_FINISHED = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1270
try:
    IS_STORE_FILE_PATH = 7
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1271
try:
    IS_LUMA_BANDWIDTH_FILTER = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1272
try:
    IS_BOARD_REVISION = 9
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1273
try:
    IS_MIRROR_BITMAP_UPDOWN = 10
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1274
try:
    IS_BUS_OVR_CNT = 11
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1275
try:
    IS_STEAL_ERROR_CNT = 12
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1276
try:
    IS_LOW_COLOR_REMOVAL = 13
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1277
try:
    IS_CHROMA_COMB_FILTER = 14
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1278
try:
    IS_CHROMA_AGC = 15
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1279
try:
    IS_WATCHDOG_ON_BOARD = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1280
try:
    IS_PASSTHROUGH_ON_BOARD = 17
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1281
try:
    IS_EXTERNAL_VREF_MODE = 18
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1282
try:
    IS_WAIT_TIMEOUT = 19
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1283
try:
    IS_TRIGGER_MISSED = 20
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1284
try:
    IS_LAST_CAPTURE_ERROR = 21
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1285
try:
    IS_PARAMETER_SET_1 = 22
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1286
try:
    IS_PARAMETER_SET_2 = 23
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1287
try:
    IS_STANDBY = 24
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1288
try:
    IS_STANDBY_SUPPORTED = 25
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1289
try:
    IS_QUEUED_IMAGE_EVENT_CNT = 26
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1290
try:
    IS_PARAMETER_EXT = 27
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1296
try:
    IS_INTERFACE_TYPE_USB = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1297
try:
    IS_INTERFACE_TYPE_USB3 = 96
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1298
try:
    IS_INTERFACE_TYPE_ETH = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1299
try:
    IS_INTERFACE_TYPE_PMC = 240
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1305
try:
    IS_BOARD_TYPE_UEYE_USB = (IS_INTERFACE_TYPE_USB + 0)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1306
try:
    IS_BOARD_TYPE_UEYE_USB_SE = IS_BOARD_TYPE_UEYE_USB
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1307
try:
    IS_BOARD_TYPE_UEYE_USB_RE = IS_BOARD_TYPE_UEYE_USB
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1308
try:
    IS_BOARD_TYPE_UEYE_USB_ME = (IS_INTERFACE_TYPE_USB + 1)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1309
try:
    IS_BOARD_TYPE_UEYE_USB_LE = (IS_INTERFACE_TYPE_USB + 2)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1310
try:
    IS_BOARD_TYPE_UEYE_USB_XS = (IS_INTERFACE_TYPE_USB + 3)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1311
try:
    IS_BOARD_TYPE_UEYE_USB_ML = (IS_INTERFACE_TYPE_USB + 5)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1313
try:
    IS_BOARD_TYPE_UEYE_USB3_LE = (IS_INTERFACE_TYPE_USB3 + 2)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1314
try:
    IS_BOARD_TYPE_UEYE_USB3_XC = (IS_INTERFACE_TYPE_USB3 + 3)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1315
try:
    IS_BOARD_TYPE_UEYE_USB3_CP = (IS_INTERFACE_TYPE_USB3 + 4)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1316
try:
    IS_BOARD_TYPE_UEYE_USB3_ML = (IS_INTERFACE_TYPE_USB3 + 5)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1318
try:
    IS_BOARD_TYPE_UEYE_ETH = IS_INTERFACE_TYPE_ETH
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1319
try:
    IS_BOARD_TYPE_UEYE_ETH_HE = IS_BOARD_TYPE_UEYE_ETH
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1320
try:
    IS_BOARD_TYPE_UEYE_ETH_SE = (IS_INTERFACE_TYPE_ETH + 1)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1321
try:
    IS_BOARD_TYPE_UEYE_ETH_RE = IS_BOARD_TYPE_UEYE_ETH_SE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1322
try:
    IS_BOARD_TYPE_UEYE_ETH_LE = (IS_INTERFACE_TYPE_ETH + 2)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1323
try:
    IS_BOARD_TYPE_UEYE_ETH_CP = (IS_INTERFACE_TYPE_ETH + 4)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1324
try:
    IS_BOARD_TYPE_UEYE_ETH_SEP = (IS_INTERFACE_TYPE_ETH + 6)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1325
try:
    IS_BOARD_TYPE_UEYE_ETH_REP = IS_BOARD_TYPE_UEYE_ETH_SEP
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1326
try:
    IS_BOARD_TYPE_UEYE_ETH_LEET = (IS_INTERFACE_TYPE_ETH + 7)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1327
try:
    IS_BOARD_TYPE_UEYE_ETH_TE = (IS_INTERFACE_TYPE_ETH + 8)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1332
try:
    IS_CAMERA_TYPE_UEYE_USB = IS_BOARD_TYPE_UEYE_USB_SE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1333
try:
    IS_CAMERA_TYPE_UEYE_USB_SE = IS_BOARD_TYPE_UEYE_USB_SE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1334
try:
    IS_CAMERA_TYPE_UEYE_USB_RE = IS_BOARD_TYPE_UEYE_USB_RE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1335
try:
    IS_CAMERA_TYPE_UEYE_USB_ME = IS_BOARD_TYPE_UEYE_USB_ME
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1336
try:
    IS_CAMERA_TYPE_UEYE_USB_LE = IS_BOARD_TYPE_UEYE_USB_LE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1337
try:
    IS_CAMERA_TYPE_UEYE_USB_ML = IS_BOARD_TYPE_UEYE_USB_ML
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1339
try:
    IS_CAMERA_TYPE_UEYE_USB3_LE = IS_BOARD_TYPE_UEYE_USB3_LE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1340
try:
    IS_CAMERA_TYPE_UEYE_USB3_XC = IS_BOARD_TYPE_UEYE_USB3_XC
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1341
try:
    IS_CAMERA_TYPE_UEYE_USB3_CP = IS_BOARD_TYPE_UEYE_USB3_CP
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1342
try:
    IS_CAMERA_TYPE_UEYE_USB3_ML = IS_BOARD_TYPE_UEYE_USB3_ML
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1344
try:
    IS_CAMERA_TYPE_UEYE_ETH = IS_BOARD_TYPE_UEYE_ETH_HE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1345
try:
    IS_CAMERA_TYPE_UEYE_ETH_HE = IS_BOARD_TYPE_UEYE_ETH_HE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1346
try:
    IS_CAMERA_TYPE_UEYE_ETH_SE = IS_BOARD_TYPE_UEYE_ETH_SE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1347
try:
    IS_CAMERA_TYPE_UEYE_ETH_RE = IS_BOARD_TYPE_UEYE_ETH_RE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1348
try:
    IS_CAMERA_TYPE_UEYE_ETH_LE = IS_BOARD_TYPE_UEYE_ETH_LE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1349
try:
    IS_CAMERA_TYPE_UEYE_ETH_CP = IS_BOARD_TYPE_UEYE_ETH_CP
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1350
try:
    IS_CAMERA_TYPE_UEYE_ETH_SEP = IS_BOARD_TYPE_UEYE_ETH_SEP
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1351
try:
    IS_CAMERA_TYPE_UEYE_ETH_REP = IS_BOARD_TYPE_UEYE_ETH_REP
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1352
try:
    IS_CAMERA_TYPE_UEYE_ETH_LEET = IS_BOARD_TYPE_UEYE_ETH_LEET
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1353
try:
    IS_CAMERA_TYPE_UEYE_ETH_TE = IS_BOARD_TYPE_UEYE_ETH_TE
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1354
try:
    IS_CAMERA_TYPE_UEYE_PMC = (IS_INTERFACE_TYPE_PMC + 1)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1360
try:
    IS_OS_UNDETERMINED = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1361
try:
    IS_OS_WIN95 = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1362
try:
    IS_OS_WINNT40 = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1363
try:
    IS_OS_WIN98 = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1364
try:
    IS_OS_WIN2000 = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1365
try:
    IS_OS_WINXP = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1366
try:
    IS_OS_WINME = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1367
try:
    IS_OS_WINNET = 7
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1368
try:
    IS_OS_WINSERVER2003 = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1369
try:
    IS_OS_WINVISTA = 9
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1370
try:
    IS_OS_LINUX24 = 10
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1371
try:
    IS_OS_LINUX26 = 11
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1372
try:
    IS_OS_WIN7 = 12
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1373
try:
    IS_OS_WIN8 = 13
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1374
try:
    IS_OS_WIN8SERVER = 14
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1375
try:
    IS_OS_GREATER_THAN_WIN8 = 15
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1381
try:
    IS_USB_10 = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1382
try:
    IS_USB_11 = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1383
try:
    IS_USB_20 = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1384
try:
    IS_USB_30 = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1385
try:
    IS_ETHERNET_10 = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1386
try:
    IS_ETHERNET_100 = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1387
try:
    IS_ETHERNET_1000 = 512
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1388
try:
    IS_ETHERNET_10000 = 1024
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1390
try:
    IS_USB_LOW_SPEED = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1391
try:
    IS_USB_FULL_SPEED = 12
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1392
try:
    IS_USB_HIGH_SPEED = 480
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1393
try:
    IS_USB_SUPER_SPEED = 4000
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1394
try:
    IS_ETHERNET_10Base = 10
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1395
try:
    IS_ETHERNET_100Base = 100
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1396
try:
    IS_ETHERNET_1000Base = 1000
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1397
try:
    IS_ETHERNET_10GBase = 10000
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1403
try:
    IS_HDR_NOT_SUPPORTED = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1404
try:
    IS_HDR_KNEEPOINTS = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1405
try:
    IS_DISABLE_HDR = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1406
try:
    IS_ENABLE_HDR = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1412
try:
    IS_TEST_IMAGE_NONE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1413
try:
    IS_TEST_IMAGE_WHITE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1414
try:
    IS_TEST_IMAGE_BLACK = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1415
try:
    IS_TEST_IMAGE_HORIZONTAL_GREYSCALE = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1416
try:
    IS_TEST_IMAGE_VERTICAL_GREYSCALE = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1417
try:
    IS_TEST_IMAGE_DIAGONAL_GREYSCALE = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1418
try:
    IS_TEST_IMAGE_WEDGE_GRAY = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1419
try:
    IS_TEST_IMAGE_WEDGE_COLOR = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1420
try:
    IS_TEST_IMAGE_ANIMATED_WEDGE_GRAY = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1422
try:
    IS_TEST_IMAGE_ANIMATED_WEDGE_COLOR = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1423
try:
    IS_TEST_IMAGE_MONO_BARS = 512
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1424
try:
    IS_TEST_IMAGE_COLOR_BARS1 = 1024
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1425
try:
    IS_TEST_IMAGE_COLOR_BARS2 = 2048
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1426
try:
    IS_TEST_IMAGE_GREYSCALE1 = 4096
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1427
try:
    IS_TEST_IMAGE_GREY_AND_COLOR_BARS = 8192
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1428
try:
    IS_TEST_IMAGE_MOVING_GREY_AND_COLOR_BARS = 16384
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1429
try:
    IS_TEST_IMAGE_ANIMATED_LINE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1431
try:
    IS_TEST_IMAGE_ALTERNATE_PATTERN = 65536
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1432
try:
    IS_TEST_IMAGE_VARIABLE_GREY = 131072
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1433
try:
    IS_TEST_IMAGE_MONOCHROME_HORIZONTAL_BARS = 262144
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1434
try:
    IS_TEST_IMAGE_MONOCHROME_VERTICAL_BARS = 524288
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1435
try:
    IS_TEST_IMAGE_CURSOR_H = 1048576
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1436
try:
    IS_TEST_IMAGE_CURSOR_V = 2097152
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1437
try:
    IS_TEST_IMAGE_COLDPIXEL_GRID = 4194304
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1438
try:
    IS_TEST_IMAGE_HOTPIXEL_GRID = 8388608
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1440
try:
    IS_TEST_IMAGE_VARIABLE_RED_PART = 16777216
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1441
try:
    IS_TEST_IMAGE_VARIABLE_GREEN_PART = 33554432
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1442
try:
    IS_TEST_IMAGE_VARIABLE_BLUE_PART = 67108864
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1443
try:
    IS_TEST_IMAGE_SHADING_IMAGE = 134217728
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1444
try:
    IS_TEST_IMAGE_WEDGE_GRAY_SENSOR = 268435456
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1445
try:
    IS_TEST_IMAGE_ANIMATED_WEDGE_GRAY_SENSOR = 536870912
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1446
try:
    IS_TEST_IMAGE_RAMPING_PATTERN = 1073741824
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1447
try:
    IS_TEST_IMAGE_CHESS_PATTERN = 2147483648L
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1453
try:
    IS_ENABLE_SENSOR_SCALER = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1454
try:
    IS_ENABLE_ANTI_ALIASING = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1460
try:
    IS_TRIGGER_TIMEOUT = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1466
try:
    IS_BEST_PCLK_RUN_ONCE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1472
try:
    IS_LOCK_LAST_BUFFER = 32770
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1473
try:
    IS_GET_ALLOC_ID_OF_THIS_BUF = 32772
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1474
try:
    IS_GET_ALLOC_ID_OF_LAST_BUF = 32776
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1475
try:
    IS_USE_ALLOC_ID = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1476
try:
    IS_USE_CURRENT_IMG_SIZE = 49152
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1481
try:
    IS_GET_D3D_MEM = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1487
try:
    IS_IMG_BMP = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1488
try:
    IS_IMG_JPG = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1489
try:
    IS_IMG_PNG = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1490
try:
    IS_IMG_RAW = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1491
try:
    IS_IMG_TIF = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1500
try:
    IS_I2C_16_BIT_REGISTER = 268435456
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1501
try:
    IS_I2C_0_BIT_REGISTER = 536870912
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1504
try:
    IS_I2C_DONT_WAIT = 8388608
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1510
try:
    IS_GET_GAMMA_MODE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1511
try:
    IS_SET_GAMMA_OFF = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1512
try:
    IS_SET_GAMMA_ON = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1518
try:
    IS_GET_CAPTURE_MODE = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1520
try:
    IS_SET_CM_ODD = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1521
try:
    IS_SET_CM_EVEN = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1522
try:
    IS_SET_CM_FRAME = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1523
try:
    IS_SET_CM_NONINTERLACED = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1524
try:
    IS_SET_CM_NEXT_FRAME = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1525
try:
    IS_SET_CM_NEXT_FIELD = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1526
try:
    IS_SET_CM_BOTHFIELDS = ((IS_SET_CM_ODD | IS_SET_CM_EVEN) | IS_SET_CM_NONINTERLACED)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1527
try:
    IS_SET_CM_FRAME_STEREO = 8196
except:
    pass

# /mingw/include\\winuser.h: 1553
try:
    WM_USER = 1024
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1767
try:
    IS_INVALID_HIDS = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1768
try:
    IS_INVALID_HCAM = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1769
try:
    IS_INVALID_HFALC = 0
except:
    pass

FALCINFO = BOARDINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1775

PFALCINFO = PBOARDINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1776

CAMINFO = BOARDINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1777

PCAMINFO = PBOARDINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1778

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1927
try:
    FIRMWARE_DOWNLOAD_NOT_SUPPORTED = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1928
try:
    INTERFACE_SPEED_NOT_SUPPORTED = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1929
try:
    INVALID_SENSOR_DETECTED = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1930
try:
    AUTHORIZATION_FAILED = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1931
try:
    DEVSTS_INCLUDED_STARTER_FIRMWARE_INCOMPATIBLE = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1935
def IS_CAMERA_AVAILABLE(_s_):
    return (((((_s_ & FIRMWARE_DOWNLOAD_NOT_SUPPORTED) == 0) and ((_s_ & INTERFACE_SPEED_NOT_SUPPORTED) == 0)) and ((_s_ & INVALID_SENSOR_DETECTED) == 0)) and ((_s_ & AUTHORIZATION_FAILED) == 0))

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1944
try:
    AC_SHUTTER = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1945
try:
    AC_GAIN = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1946
try:
    AC_WHITEBAL = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1947
try:
    AC_WB_RED_CHANNEL = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1948
try:
    AC_WB_GREEN_CHANNEL = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1949
try:
    AC_WB_BLUE_CHANNEL = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1950
try:
    AC_FRAMERATE = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1951
try:
    AC_SENSOR_SHUTTER = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1952
try:
    AC_SENSOR_GAIN = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1953
try:
    AC_SENSOR_GAIN_SHUTTER = 512
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1954
try:
    AC_SENSOR_FRAMERATE = 1024
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1955
try:
    AC_SENSOR_WB = 2048
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1956
try:
    AC_SENSOR_AUTO_REFERENCE = 4096
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1957
try:
    AC_SENSOR_AUTO_SPEED = 8192
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1958
try:
    AC_SENSOR_AUTO_HYSTERESIS = 16384
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1959
try:
    AC_SENSOR_AUTO_SKIPFRAMES = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1960
try:
    AC_SENSOR_AUTO_CONTRAST_CORRECTION = 65536
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1961
try:
    AC_SENSOR_AUTO_CONTRAST_FDT_AOI = 131072
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1962
try:
    AC_SENSOR_AUTO_BACKLIGHT_COMP = 262144
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1964
try:
    ACS_ADJUSTING = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1965
try:
    ACS_FINISHED = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1966
try:
    ACS_DISABLED = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2955
try:
    IS_BOOTBOOST_ID_MIN = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2956
try:
    IS_BOOTBOOST_ID_MAX = 254
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2957
try:
    IS_BOOTBOOST_ID_NONE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2958
try:
    IS_BOOTBOOST_ID_ALL = 255
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2967
try:
    IS_BOOTBOOST_DEFAULT_WAIT_TIMEOUT_SEC = 60
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2985
try:
    IS_BOOTBOOST_IDLIST_HEADERSIZE = sizeof(DWORD)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2987
try:
    IS_BOOTBOOST_IDLIST_ELEMENTSIZE = sizeof(IS_BOOTBOOST_ID)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4393
try:
    IO_LED_STATE_1 = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4394
try:
    IO_LED_STATE_2 = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4396
try:
    IO_FLASH_MODE_OFF = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4397
try:
    IO_FLASH_MODE_TRIGGER_LO_ACTIVE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4398
try:
    IO_FLASH_MODE_TRIGGER_HI_ACTIVE = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4399
try:
    IO_FLASH_MODE_CONSTANT_HIGH = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4400
try:
    IO_FLASH_MODE_CONSTANT_LOW = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4401
try:
    IO_FLASH_MODE_FREERUN_LO_ACTIVE = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4402
try:
    IO_FLASH_MODE_FREERUN_HI_ACTIVE = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4404
try:
    IS_FLASH_MODE_PWM = 32768
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4405
try:
    IO_FLASH_MODE_GPIO_1 = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4406
try:
    IO_FLASH_MODE_GPIO_2 = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4407
try:
    IO_FLASH_MODE_GPIO_3 = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4408
try:
    IO_FLASH_MODE_GPIO_4 = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4409
try:
    IO_FLASH_MODE_GPIO_5 = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4410
try:
    IO_FLASH_MODE_GPIO_6 = 512
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4412
try:
    IO_FLASH_GPIO_PORT_MASK = (((((IO_FLASH_MODE_GPIO_1 | IO_FLASH_MODE_GPIO_2) | IO_FLASH_MODE_GPIO_3) | IO_FLASH_MODE_GPIO_4) | IO_FLASH_MODE_GPIO_5) | IO_FLASH_MODE_GPIO_6)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4414
try:
    IO_GPIO_1 = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4415
try:
    IO_GPIO_2 = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4416
try:
    IO_GPIO_3 = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4417
try:
    IO_GPIO_4 = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4418
try:
    IO_GPIO_5 = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4419
try:
    IO_GPIO_6 = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4421
try:
    IS_GPIO_INPUT = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4422
try:
    IS_GPIO_OUTPUT = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4423
try:
    IS_GPIO_FLASH = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4424
try:
    IS_GPIO_PWM = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4425
try:
    IS_GPIO_COMPORT_RX = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4426
try:
    IS_GPIO_COMPORT_TX = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4427
try:
    IS_GPIO_MULTI_INTEGRATION_MODE = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4428
try:
    IS_GPIO_TRIGGER = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4430
try:
    IS_FLASH_AUTO_FREERUN_OFF = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4431
try:
    IS_FLASH_AUTO_FREERUN_ON = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4507
try:
    IS_AWB_GREYWORLD = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4508
try:
    IS_AWB_COLOR_TEMPERATURE = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4510
try:
    IS_AUTOPARAMETER_DISABLE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4511
try:
    IS_AUTOPARAMETER_ENABLE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4512
try:
    IS_AUTOPARAMETER_ENABLE_RUNONCE = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4847
try:
    IS_LUT_64 = 64
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4848
try:
    IS_LUT_128 = 128
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4850
try:
    IS_LUT_PRESET_ID_IDENTITY = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4851
try:
    IS_LUT_PRESET_ID_NEGATIVE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4852
try:
    IS_LUT_PRESET_ID_GLOW1 = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4853
try:
    IS_LUT_PRESET_ID_GLOW2 = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4854
try:
    IS_LUT_PRESET_ID_ASTRO1 = 4
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4855
try:
    IS_LUT_PRESET_ID_RAINBOW1 = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4856
try:
    IS_LUT_PRESET_ID_MAP1 = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4857
try:
    IS_LUT_PRESET_ID_HOT = 7
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4858
try:
    IS_LUT_PRESET_ID_SEPIC = 8
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4859
try:
    IS_LUT_PRESET_ID_ONLY_RED = 9
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4860
try:
    IS_LUT_PRESET_ID_ONLY_GREEN = 10
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4861
try:
    IS_LUT_PRESET_ID_ONLY_BLUE = 11
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4862
try:
    IS_LUT_PRESET_ID_DIGITAL_GAIN_2X = 12
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4863
try:
    IS_LUT_PRESET_ID_DIGITAL_GAIN_4X = 13
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4864
try:
    IS_LUT_PRESET_ID_DIGITAL_GAIN_8X = 14
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4891
try:
    IS_LUT_CMD_SET_ENABLED = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4892
try:
    IS_LUT_CMD_SET_MODE = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4893
try:
    IS_LUT_CMD_GET_STATE = 5
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4894
try:
    IS_LUT_CMD_GET_SUPPORT_INFO = 6
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4895
try:
    IS_LUT_CMD_SET_USER_LUT = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4896
try:
    IS_LUT_CMD_GET_USER_LUT = 17
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4897
try:
    IS_LUT_CMD_GET_COMPLETE_LUT = 18
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4898
try:
    IS_LUT_CMD_GET_PRESET_LUT = 19
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4899
try:
    IS_LUT_CMD_LOAD_FILE = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4900
try:
    IS_LUT_CMD_SAVE_FILE = 257
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4905
try:
    IS_LUT_STATE_ID_FLAG_HARDWARE = 16
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4906
try:
    IS_LUT_STATE_ID_FLAG_SOFTWARE = 32
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4907
try:
    IS_LUT_STATE_ID_FLAG_GAMMA = 256
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4908
try:
    IS_LUT_STATE_ID_FLAG_LUT = 512
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4910
try:
    IS_LUT_STATE_ID_INACTIVE = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4911
try:
    IS_LUT_STATE_ID_NOT_SUPPORTED = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4912
try:
    IS_LUT_STATE_ID_HARDWARE_LUT = (IS_LUT_STATE_ID_FLAG_HARDWARE | IS_LUT_STATE_ID_FLAG_LUT)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4913
try:
    IS_LUT_STATE_ID_HARDWARE_GAMMA = (IS_LUT_STATE_ID_FLAG_HARDWARE | IS_LUT_STATE_ID_FLAG_GAMMA)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4914
try:
    IS_LUT_STATE_ID_HARDWARE_LUTANDGAMMA = ((IS_LUT_STATE_ID_FLAG_HARDWARE | IS_LUT_STATE_ID_FLAG_LUT) | IS_LUT_STATE_ID_FLAG_GAMMA)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4915
try:
    IS_LUT_STATE_ID_SOFTWARE_LUT = (IS_LUT_STATE_ID_FLAG_SOFTWARE | IS_LUT_STATE_ID_FLAG_LUT)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4916
try:
    IS_LUT_STATE_ID_SOFTWARE_GAMMA = (IS_LUT_STATE_ID_FLAG_SOFTWARE | IS_LUT_STATE_ID_FLAG_GAMMA)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4917
try:
    IS_LUT_STATE_ID_SOFTWARE_LUTANDGAMMA = ((IS_LUT_STATE_ID_FLAG_SOFTWARE | IS_LUT_STATE_ID_FLAG_LUT) | IS_LUT_STATE_ID_FLAG_GAMMA)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4919
try:
    IS_LUT_MODE_ID_DEFAULT = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4920
try:
    IS_LUT_MODE_ID_FORCE_HARDWARE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4921
try:
    IS_LUT_MODE_ID_FORCE_SOFTWARE = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4923
try:
    IS_LUT_DISABLED = 0
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4924
try:
    IS_LUT_ENABLED = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4980
try:
    IS_GAMMA_CMD_SET = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4981
try:
    IS_GAMMA_CMD_GET_DEFAULT = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4982
try:
    IS_GAMMA_CMD_GET = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4984
try:
    IS_GAMMA_VALUE_MIN = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4985
try:
    IS_GAMMA_VALUE_MAX = 1000
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5072
try:
    IS_MC_CMD_FLAG_ACTIVE = 4096
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5073
try:
    IS_MC_CMD_FLAG_PASSIVE = 8192
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5076
try:
    IS_PMC_CMD_INITIALIZE = (1 | IS_MC_CMD_FLAG_PASSIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5077
try:
    IS_PMC_CMD_DEINITIALIZE = (2 | IS_MC_CMD_FLAG_PASSIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5079
try:
    IS_PMC_CMD_ADDMCDEVICE = (3 | IS_MC_CMD_FLAG_PASSIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5080
try:
    IS_PMC_CMD_REMOVEMCDEVICE = (4 | IS_MC_CMD_FLAG_PASSIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5081
try:
    IS_PMC_CMD_STOREDEVICES = (5 | IS_MC_CMD_FLAG_PASSIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5082
try:
    IS_PMC_CMD_LOADDEVICES = (6 | IS_MC_CMD_FLAG_PASSIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5084
try:
    IS_PMC_CMD_SYSTEM_SET_ENABLE = (7 | IS_MC_CMD_FLAG_PASSIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5085
try:
    IS_PMC_CMD_SYSTEM_GET_ENABLE = (8 | IS_MC_CMD_FLAG_PASSIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5087
try:
    IS_PMC_CMD_REMOVEALLMCDEVICES = (9 | IS_MC_CMD_FLAG_PASSIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5090
try:
    IS_AMC_CMD_SET_MC_IP = (16 | IS_MC_CMD_FLAG_ACTIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5091
try:
    IS_AMC_CMD_GET_MC_IP = (17 | IS_MC_CMD_FLAG_ACTIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5092
try:
    IS_AMC_CMD_SET_MC_ENABLED = (18 | IS_MC_CMD_FLAG_ACTIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5093
try:
    IS_AMC_CMD_GET_MC_ENABLED = (19 | IS_MC_CMD_FLAG_ACTIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5094
try:
    IS_AMC_CMD_GET_MC_SUPPORTED = (20 | IS_MC_CMD_FLAG_ACTIVE)
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5096
try:
    IS_AMC_SUPPORTED_FLAG_DEVICE = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5097
try:
    IS_AMC_SUPPORTED_FLAG_FIRMWARE = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5099
try:
    IS_PMC_ERRORHANDLING_REJECT_IMAGES = 1
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5100
try:
    IS_PMC_ERRORHANDLING_IGNORE_MISSING_PARTS = 2
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5101
try:
    IS_PMC_ERRORHANDLING_MERGE_IMAGES_RELEASE_ON_COMPLETE = 3
except:
    pass

# E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 5102
try:
    IS_PMC_ERRORHANDLING_MERGE_IMAGES_RELEASE_ON_RECEIVED_IMGLEN = 4
except:
    pass

_SENSORINFO = struct__SENSORINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1807

_REVISIONINFO = struct__REVISIONINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1841

_UEYE_CAPTURE_STATUS_INFO = struct__UEYE_CAPTURE_STATUS_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1872

_UEYE_CAMERA_INFO = struct__UEYE_CAMERA_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1902

_UEYE_CAMERA_LIST = struct__UEYE_CAMERA_LIST # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1921

_AUTO_BRIGHT_STATUS = struct__AUTO_BRIGHT_STATUS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1975

_AUTO_WB_CHANNNEL_STATUS = struct__AUTO_WB_CHANNNEL_STATUS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1984

_AUTO_WB_STATUS = struct__AUTO_WB_STATUS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 1992

_UEYE_AUTO_INFO = struct__UEYE_AUTO_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2050

_DC_INFO = struct__DC_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2058

_KNEEPOINT = struct__KNEEPOINT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2225

_KNEEPOINTARRAY = struct__KNEEPOINTARRAY # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2232

_KNEEPOINTINFO = struct__KNEEPOINTINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2245

_SENSORSCALERINFO = struct__SENSORSCALERINFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2294

_UEYETIME = struct__UEYETIME # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2310

S_IMAGE_FORMAT_INFO = struct_S_IMAGE_FORMAT_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2384

S_IMAGE_FORMAT_LIST = struct_S_IMAGE_FORMAT_LIST # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2393

_OPENGL_DISPLAY = struct__OPENGL_DISPLAY # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2763

S_RANGE_OF_VALUES_U32 = struct_S_RANGE_OF_VALUES_U32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2825

S_IS_BOOTBOOST_IDLIST = struct_S_IS_BOOTBOOST_IDLIST # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 2982

S_IS_TIMESTAMP_CONFIGURATION = struct_S_IS_TIMESTAMP_CONFIGURATION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3384

S_IS_MULTI_INTEGRATION_CYCLES = struct_S_IS_MULTI_INTEGRATION_CYCLES # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3436

S_IS_MULTI_INTEGRATION_SCOPE = struct_S_IS_MULTI_INTEGRATION_SCOPE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3456

S_IS_DEVICE_INFO_HEARTBEAT = struct_S_IS_DEVICE_INFO_HEARTBEAT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3594

S_IS_DEVICE_INFO_CONTROL = struct_S_IS_DEVICE_INFO_CONTROL # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3610

S_IS_DEVICE_INFO = struct_S_IS_DEVICE_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3627

S_IS_CALLBACK_EVCTX_DATA_PROCESSING = struct_S_IS_CALLBACK_EVCTX_DATA_PROCESSING # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3725

S_IS_CALLBACK_EVCTX_IMAGE_PROCESSING = struct_S_IS_CALLBACK_EVCTX_IMAGE_PROCESSING # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3751

S_IS_CALLBACK_FDBK_IMAGE_PROCESSING = struct_S_IS_CALLBACK_FDBK_IMAGE_PROCESSING # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3771

S_IS_CALLBACK_INSTALLATION_DATA = struct_S_IS_CALLBACK_INSTALLATION_DATA # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3834

S_IS_OPTIMAL_CAMERA_TIMING = struct_S_IS_OPTIMAL_CAMERA_TIMING # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3879

_UEYE_ETH_ADDR_IPV4 = union__UEYE_ETH_ADDR_IPV4 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3915

_UEYE_ETH_ADDR_MAC = struct__UEYE_ETH_ADDR_MAC # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3922

_UEYE_ETH_IP_CONFIGURATION = struct__UEYE_ETH_IP_CONFIGURATION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 3932

_UEYE_ETH_DEVICE_INFO_HEARTBEAT = struct__UEYE_ETH_DEVICE_INFO_HEARTBEAT # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4019

_UEYE_ETH_DEVICE_INFO_CONTROL = struct__UEYE_ETH_DEVICE_INFO_CONTROL # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4065

_UEYE_ETH_ETHERNET_CONFIGURATION = struct__UEYE_ETH_ETHERNET_CONFIGURATION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4073

_UEYE_ETH_AUTOCFG_IP_SETUP = struct__UEYE_ETH_AUTOCFG_IP_SETUP # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4083

_UEYE_ETH_ADAPTER_INFO = struct__UEYE_ETH_ADAPTER_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4131

_UEYE_ETH_DRIVER_INFO = struct__UEYE_ETH_DRIVER_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4143

_UEYE_ETH_DEVICE_INFO = struct__UEYE_ETH_DEVICE_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4158

_UEYE_COMPORT_CONFIGURATION = struct__UEYE_COMPORT_CONFIGURATION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4165

S_IO_FLASH_PARAMS = struct_S_IO_FLASH_PARAMS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4363

S_IO_PWM_PARAMS = struct_S_IO_PWM_PARAMS # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4373

S_IO_GPIO_CONFIGURATION = struct_S_IO_GPIO_CONFIGURATION # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4387

S_IS_RANGE_S32 = struct_S_IS_RANGE_S32 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4683

S_IS_RANGE_F64 = struct_S_IS_RANGE_F64 # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4694

S_ID_RANGE = struct_S_ID_RANGE # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4765

S_IMGBUF_ITERATION_INFO = struct_S_IMGBUF_ITERATION_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4777

S_IMGBUF_ITEM = struct_S_IMGBUF_ITEM # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4788

S_MEASURE_SHARPNESS_AOI_INFO = struct_S_MEASURE_SHARPNESS_AOI_INFO # E:\\pi\\129_Burton_Trunk\\04_Software\\Workspaces\\BurtonInstrument\\workspace\\src\\ImageCapture\\CameraDriver\\uEye.h: 4811

# No inserted files

