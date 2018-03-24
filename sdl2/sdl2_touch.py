# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro

# Enum

# Typedef
SDL_TouchID = ctypes.c_longlong
SDL_FingerID = ctypes.c_longlong

# Struct

class SDL_Finger(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_longlong),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("pressure", ctypes.c_float),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetNumTouchDevices')
    SDL2_API_ARGS_MAP['SDL_GetNumTouchDevices'] = None
    SDL2_API_RETVAL_MAP['SDL_GetNumTouchDevices'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetTouchDevice')
    SDL2_API_ARGS_MAP['SDL_GetTouchDevice'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetTouchDevice'] = ctypes.c_longlong

    SDL2_API_NAMES.append('SDL_GetNumTouchFingers')
    SDL2_API_ARGS_MAP['SDL_GetNumTouchFingers'] = [ctypes.c_longlong]
    SDL2_API_RETVAL_MAP['SDL_GetNumTouchFingers'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetTouchFinger')
    SDL2_API_ARGS_MAP['SDL_GetTouchFinger'] = [ctypes.c_longlong, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetTouchFinger'] = ctypes.c_void_p


