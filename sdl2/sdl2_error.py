# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro

# Enum
SDL_ENOMEM = 0
SDL_EFREAD = 1
SDL_EFWRITE = 2
SDL_EFSEEK = 3
SDL_UNSUPPORTED = 4
SDL_LASTERROR = 5

# Typedef
SDL_errorcode = ctypes.c_int

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_SetError')
    SDL2_API_ARGS_MAP['SDL_SetError'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_SetError'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetError')
    SDL2_API_ARGS_MAP['SDL_GetError'] = None
    SDL2_API_RETVAL_MAP['SDL_GetError'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_ClearError')
    SDL2_API_ARGS_MAP['SDL_ClearError'] = None
    SDL2_API_RETVAL_MAP['SDL_ClearError'] = None

    SDL2_API_NAMES.append('SDL_Error')
    SDL2_API_ARGS_MAP['SDL_Error'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_Error'] = ctypes.c_int


