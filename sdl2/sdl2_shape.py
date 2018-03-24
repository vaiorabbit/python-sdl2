# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
from .sdl2_pixels import SDL_Color

# Define/Macro
SDL_NONSHAPEABLE_WINDOW = -1
SDL_INVALID_SHAPE_ARGUMENT = -2
SDL_WINDOW_LACKS_SHAPE = -3

# Enum
ShapeModeDefault = 0
ShapeModeBinarizeAlpha = 1
ShapeModeReverseBinarizeAlpha = 2
ShapeModeColorKey = 3

# Typedef
WindowShapeMode = ctypes.c_int

# Struct

class SDL_WindowShapeParams(ctypes.Union):
    _fields_ = [
        ("binarizationCutoff", ctypes.c_uint8),
        ("colorKey", SDL_Color),
    ]

class SDL_WindowShapeMode(ctypes.Structure):
    _fields_ = [
        ("mode", ctypes.c_int),
        ("parameters", SDL_WindowShapeParams),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_CreateShapedWindow')
    SDL2_API_ARGS_MAP['SDL_CreateShapedWindow'] = [ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_CreateShapedWindow'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_IsShapedWindow')
    SDL2_API_ARGS_MAP['SDL_IsShapedWindow'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_IsShapedWindow'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetWindowShape')
    SDL2_API_ARGS_MAP['SDL_SetWindowShape'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetWindowShape'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetShapedWindowMode')
    SDL2_API_ARGS_MAP['SDL_GetShapedWindowMode'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetShapedWindowMode'] = ctypes.c_int


