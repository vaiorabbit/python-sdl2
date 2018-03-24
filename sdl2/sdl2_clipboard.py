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
    SDL2_API_NAMES.append('SDL_SetClipboardText')
    SDL2_API_ARGS_MAP['SDL_SetClipboardText'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_SetClipboardText'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetClipboardText')
    SDL2_API_ARGS_MAP['SDL_GetClipboardText'] = None
    SDL2_API_RETVAL_MAP['SDL_GetClipboardText'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_HasClipboardText')
    SDL2_API_ARGS_MAP['SDL_HasClipboardText'] = None
    SDL2_API_RETVAL_MAP['SDL_HasClipboardText'] = ctypes.c_int


