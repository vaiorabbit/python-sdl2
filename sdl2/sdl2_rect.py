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

# Struct

class SDL_Point(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
    ]

class SDL_Rect(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_PointInRect')
    SDL2_API_ARGS_MAP['SDL_PointInRect'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_PointInRect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RectEmpty')
    SDL2_API_ARGS_MAP['SDL_RectEmpty'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RectEmpty'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RectEquals')
    SDL2_API_ARGS_MAP['SDL_RectEquals'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RectEquals'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasIntersection')
    SDL2_API_ARGS_MAP['SDL_HasIntersection'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HasIntersection'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_IntersectRect')
    SDL2_API_ARGS_MAP['SDL_IntersectRect'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_IntersectRect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_UnionRect')
    SDL2_API_ARGS_MAP['SDL_UnionRect'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_UnionRect'] = None

    SDL2_API_NAMES.append('SDL_EnclosePoints')
    SDL2_API_ARGS_MAP['SDL_EnclosePoints'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_EnclosePoints'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_IntersectRectAndLine')
    SDL2_API_ARGS_MAP['SDL_IntersectRectAndLine'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_IntersectRectAndLine'] = ctypes.c_int


