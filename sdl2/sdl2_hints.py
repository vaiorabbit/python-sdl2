# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro

# Enum
SDL_HINT_DEFAULT = 0
SDL_HINT_NORMAL = 1
SDL_HINT_OVERRIDE = 2

# Typedef
SDL_HintPriority = ctypes.c_int
SDL_HintCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_SetHintWithPriority')
    SDL2_API_ARGS_MAP['SDL_SetHintWithPriority'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetHintWithPriority'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetHint')
    SDL2_API_ARGS_MAP['SDL_SetHint'] = [ctypes.c_char_p, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_SetHint'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetHint')
    SDL2_API_ARGS_MAP['SDL_GetHint'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GetHint'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GetHintBoolean')
    SDL2_API_ARGS_MAP['SDL_GetHintBoolean'] = [ctypes.c_char_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetHintBoolean'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_AddHintCallback')
    SDL2_API_ARGS_MAP['SDL_AddHintCallback'] = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_AddHintCallback'] = None

    SDL2_API_NAMES.append('SDL_DelHintCallback')
    SDL2_API_ARGS_MAP['SDL_DelHintCallback'] = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_DelHintCallback'] = None

    SDL2_API_NAMES.append('SDL_ClearHints')
    SDL2_API_ARGS_MAP['SDL_ClearHints'] = None
    SDL2_API_RETVAL_MAP['SDL_ClearHints'] = None


