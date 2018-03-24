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
SDL_TimerCallback = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p)
SDL_TimerID = ctypes.c_int

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetTicks')
    SDL2_API_ARGS_MAP['SDL_GetTicks'] = None
    SDL2_API_RETVAL_MAP['SDL_GetTicks'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_GetPerformanceCounter')
    SDL2_API_ARGS_MAP['SDL_GetPerformanceCounter'] = None
    SDL2_API_RETVAL_MAP['SDL_GetPerformanceCounter'] = ctypes.c_ulonglong

    SDL2_API_NAMES.append('SDL_GetPerformanceFrequency')
    SDL2_API_ARGS_MAP['SDL_GetPerformanceFrequency'] = None
    SDL2_API_RETVAL_MAP['SDL_GetPerformanceFrequency'] = ctypes.c_ulonglong

    SDL2_API_NAMES.append('SDL_Delay')
    SDL2_API_ARGS_MAP['SDL_Delay'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_Delay'] = None

    SDL2_API_NAMES.append('SDL_AddTimer')
    SDL2_API_ARGS_MAP['SDL_AddTimer'] = [ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_AddTimer'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RemoveTimer')
    SDL2_API_ARGS_MAP['SDL_RemoveTimer'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RemoveTimer'] = ctypes.c_int


