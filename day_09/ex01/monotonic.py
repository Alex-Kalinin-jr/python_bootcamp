import ctypes
import sys


CLOCK_MONOTONIC = 4


if sys.platform.startswith('linux'):
    libc = ctypes.CDLL("libc.so.6")
elif sys.platform.startswith('darwin'):
    libc = ctypes.CDLL("libc.dylib")
else:
    raise NotImplementedError("Clock not supported on this platform")

clock_gettime = libc.clock_gettime


class timespec(ctypes.Structure):
    _fields_ = [
        ('tv_sec', ctypes.c_longlong),
        ('tv_nsec', ctypes.c_long)
    ]

    def __sub__(self, other):
        result = timespec()
        result.tv_sec = self.tv_sec - other.tv_sec
        result.tv_nsec = self.tv_nsec - other.tv_nsec
        if result.tv_nsec < 0:
            result.tv_sec -= 1
            result.tv_nsec += 1000000000
        return result

    def __sum__(self, other):
        result = timespec()
        result.tv_sec = self.tv_sec + other.tv_sec
        result.tv_nsec = self.tv_nsec + other.tv_nsec
        if result.tv_nsec >= 1000000000:
            result.tv_sec += 1
            result.tv_nsec -= 1000000000
        return result

def monotonic():
    result = timespec()
    clock_gettime(CLOCK_MONOTONIC, ctypes.byref(result))
    return result.tv_sec + (result.tv_nsec / 1000000000.0)