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

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetBasePath')
    SDL2_API_ARGS_MAP['SDL_GetBasePath'] = None
    SDL2_API_RETVAL_MAP['SDL_GetBasePath'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GetPrefPath')
    SDL2_API_ARGS_MAP['SDL_GetPrefPath'] = [ctypes.c_char_p, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GetPrefPath'] = ctypes.c_char_p


