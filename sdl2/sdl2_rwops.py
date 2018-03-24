# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
import os

# Define/Macro
SDL_RWOPS_UNKNOWN = 0
SDL_RWOPS_WINFILE = 1
SDL_RWOPS_STDFILE = 2
SDL_RWOPS_JNIFILE = 3
SDL_RWOPS_MEMORY = 4
SDL_RWOPS_MEMORY_RO = 5

# Enum

# Typedef

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_RWFromFile')
    SDL2_API_ARGS_MAP['SDL_RWFromFile'] = [ctypes.c_char_p, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_RWFromFile'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_RWFromFP')
    SDL2_API_ARGS_MAP['SDL_RWFromFP'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RWFromFP'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_RWFromMem')
    SDL2_API_ARGS_MAP['SDL_RWFromMem'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RWFromMem'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_RWFromConstMem')
    SDL2_API_ARGS_MAP['SDL_RWFromConstMem'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RWFromConstMem'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_AllocRW')
    SDL2_API_ARGS_MAP['SDL_AllocRW'] = None
    SDL2_API_RETVAL_MAP['SDL_AllocRW'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_FreeRW')
    SDL2_API_ARGS_MAP['SDL_FreeRW'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_FreeRW'] = None

    SDL2_API_NAMES.append('SDL_LoadFile_RW')
    SDL2_API_ARGS_MAP['SDL_LoadFile_RW'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_LoadFile_RW'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_ReadU8')
    SDL2_API_ARGS_MAP['SDL_ReadU8'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ReadU8'] = ctypes.c_uint8

    SDL2_API_NAMES.append('SDL_ReadLE16')
    SDL2_API_ARGS_MAP['SDL_ReadLE16'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ReadLE16'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_ReadBE16')
    SDL2_API_ARGS_MAP['SDL_ReadBE16'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ReadBE16'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_ReadLE32')
    SDL2_API_ARGS_MAP['SDL_ReadLE32'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ReadLE32'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_ReadBE32')
    SDL2_API_ARGS_MAP['SDL_ReadBE32'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ReadBE32'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_ReadLE64')
    SDL2_API_ARGS_MAP['SDL_ReadLE64'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ReadLE64'] = ctypes.c_ulonglong

    SDL2_API_NAMES.append('SDL_ReadBE64')
    SDL2_API_ARGS_MAP['SDL_ReadBE64'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ReadBE64'] = ctypes.c_ulonglong

    SDL2_API_NAMES.append('SDL_WriteU8')
    SDL2_API_ARGS_MAP['SDL_WriteU8'] = [ctypes.c_void_p, ctypes.c_uint8]
    SDL2_API_RETVAL_MAP['SDL_WriteU8'] = ctypes.c_size_t

    SDL2_API_NAMES.append('SDL_WriteLE16')
    SDL2_API_ARGS_MAP['SDL_WriteLE16'] = [ctypes.c_void_p, ctypes.c_ushort]
    SDL2_API_RETVAL_MAP['SDL_WriteLE16'] = ctypes.c_size_t

    SDL2_API_NAMES.append('SDL_WriteBE16')
    SDL2_API_ARGS_MAP['SDL_WriteBE16'] = [ctypes.c_void_p, ctypes.c_ushort]
    SDL2_API_RETVAL_MAP['SDL_WriteBE16'] = ctypes.c_size_t

    SDL2_API_NAMES.append('SDL_WriteLE32')
    SDL2_API_ARGS_MAP['SDL_WriteLE32'] = [ctypes.c_void_p, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_WriteLE32'] = ctypes.c_size_t

    SDL2_API_NAMES.append('SDL_WriteBE32')
    SDL2_API_ARGS_MAP['SDL_WriteBE32'] = [ctypes.c_void_p, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_WriteBE32'] = ctypes.c_size_t

    SDL2_API_NAMES.append('SDL_WriteLE64')
    SDL2_API_ARGS_MAP['SDL_WriteLE64'] = [ctypes.c_void_p, ctypes.c_ulonglong]
    SDL2_API_RETVAL_MAP['SDL_WriteLE64'] = ctypes.c_size_t

    SDL2_API_NAMES.append('SDL_WriteBE64')
    SDL2_API_ARGS_MAP['SDL_WriteBE64'] = [ctypes.c_void_p, ctypes.c_ulonglong]
    SDL2_API_RETVAL_MAP['SDL_WriteBE64'] = ctypes.c_size_t


class _SDL_RWops_mem(ctypes.Structure):
    _fields_ = [
        ("base", ctypes.POINTER(ctypes.c_uint8)),
        ("here", ctypes.POINTER(ctypes.c_uint8)),
        ("stop", ctypes.POINTER(ctypes.c_uint8)),
    ]

class _SDL_RWops_unknown(ctypes.Structure):
    _fields_ = [
        ("data1", ctypes.c_void_p),
        ("data2", ctypes.c_void_p),
    ]

class _SDL_RWops_windowsio_buffer(ctypes.Structure):
    _fields_ = [
        ("data", ctypes.c_void_p),
        ("size", ctypes.c_size_t),
        ("left", ctypes.c_size_t),
    ]

class _SDL_RWops_windowsio(ctypes.Structure):
    _fields_ = [
        ("append", ctypes.c_int),
        ("h", ctypes.c_void_p),
        ("buffer", _SDL_RWops_windowsio_buffer),
    ]

class _Default_SDL_RWops_hidden(ctypes.Union):
    _anonymous_ = ('mem', 'unknown')
    _fields_ = [
        ("mem", _SDL_RWops_mem),
        ("unknown", _SDL_RWops_unknown),
    ]

class _Win32_SDL_RWops_hidden(ctypes.Union):
    _anonymous_ = ('mem', 'unknown', 'windowsio')
    _fields_ = [
        ("mem", _SDL_RWops_mem),
        ("unknown", _SDL_RWops_unknown),
        ("windowsio", _SDL_RWops_windowsio),
    ]

class _Default_SDL_RWops(ctypes.Structure):
    _fields_ = [
        ("size", ctypes.c_void_p),
        ("seek", ctypes.c_void_p),
        ("read", ctypes.c_void_p),
        ("write", ctypes.c_void_p),
        ("close", ctypes.c_void_p),
        ("type", ctypes.c_uint),
        ("hidden", _Default_SDL_RWops_hidden),
    ]

class _Win32_SDL_RWops(ctypes.Structure):
    _fields_ = [
        ("size", ctypes.c_void_p),
        ("seek", ctypes.c_void_p),
        ("read", ctypes.c_void_p),
        ("write", ctypes.c_void_p),
        ("close", ctypes.c_void_p),
        ("type", ctypes.c_uint),
        ("hidden", _Win32_SDL_RWops_hidden),
    ]

SDL_RWops = _Win32_SDL_RWops if os.name == "nt" else _Default_SDL_RWops

