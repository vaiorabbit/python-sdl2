# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
from .api import SDL2_GFX_API_NAMES, SDL2_GFX_API_ARGS_MAP, SDL2_GFX_API_RETVAL_MAP

# Define/Macro

# Enum

# Typedef

# Struct

class FPSmanager(ctypes.Structure):
    _fields_ = [
        ("framecount", ctypes.c_uint),
        ("rateticks", ctypes.c_float),
        ("baseticks", ctypes.c_uint),
        ("lastticks", ctypes.c_uint),
        ("rate", ctypes.c_uint),
    ]

# Function
def setup_symbols():
    SDL2_GFX_API_NAMES.append('SDL_initFramerate')
    SDL2_GFX_API_ARGS_MAP['SDL_initFramerate'] = [ctypes.c_void_p]
    SDL2_GFX_API_RETVAL_MAP['SDL_initFramerate'] = None

    SDL2_GFX_API_NAMES.append('SDL_setFramerate')
    SDL2_GFX_API_ARGS_MAP['SDL_setFramerate'] = [ctypes.c_void_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_setFramerate'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_getFramerate')
    SDL2_GFX_API_ARGS_MAP['SDL_getFramerate'] = [ctypes.c_void_p]
    SDL2_GFX_API_RETVAL_MAP['SDL_getFramerate'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_getFramecount')
    SDL2_GFX_API_ARGS_MAP['SDL_getFramecount'] = [ctypes.c_void_p]
    SDL2_GFX_API_RETVAL_MAP['SDL_getFramecount'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_framerateDelay')
    SDL2_GFX_API_ARGS_MAP['SDL_framerateDelay'] = [ctypes.c_void_p]
    SDL2_GFX_API_RETVAL_MAP['SDL_framerateDelay'] = ctypes.c_uint


