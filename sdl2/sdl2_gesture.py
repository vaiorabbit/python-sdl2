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
SDL_GestureID = ctypes.c_longlong

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_RecordGesture')
    SDL2_API_ARGS_MAP['SDL_RecordGesture'] = [ctypes.c_longlong]
    SDL2_API_RETVAL_MAP['SDL_RecordGesture'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SaveAllDollarTemplates')
    SDL2_API_ARGS_MAP['SDL_SaveAllDollarTemplates'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SaveAllDollarTemplates'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SaveDollarTemplate')
    SDL2_API_ARGS_MAP['SDL_SaveDollarTemplate'] = [ctypes.c_longlong, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SaveDollarTemplate'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_LoadDollarTemplates')
    SDL2_API_ARGS_MAP['SDL_LoadDollarTemplates'] = [ctypes.c_longlong, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_LoadDollarTemplates'] = ctypes.c_int


