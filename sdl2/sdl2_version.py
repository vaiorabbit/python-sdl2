# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro
SDL_MAJOR_VERSION = 2
SDL_MINOR_VERSION = 0
SDL_PATCHLEVEL = 8

# Enum

# Typedef

# Struct

class SDL_version(ctypes.Structure):
    _fields_ = [
        ("major", ctypes.c_uint8),
        ("minor", ctypes.c_uint8),
        ("patch", ctypes.c_uint8),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetVersion')
    SDL2_API_ARGS_MAP['SDL_GetVersion'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetVersion'] = None

    SDL2_API_NAMES.append('SDL_GetRevision')
    SDL2_API_ARGS_MAP['SDL_GetRevision'] = None
    SDL2_API_RETVAL_MAP['SDL_GetRevision'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GetRevisionNumber')
    SDL2_API_ARGS_MAP['SDL_GetRevisionNumber'] = None
    SDL2_API_RETVAL_MAP['SDL_GetRevisionNumber'] = ctypes.c_int


