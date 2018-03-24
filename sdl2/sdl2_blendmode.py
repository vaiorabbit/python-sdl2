# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro

# Enum
SDL_BLENDMODE_NONE = 0
SDL_BLENDMODE_BLEND = 1
SDL_BLENDMODE_ADD = 2
SDL_BLENDMODE_MOD = 4
SDL_BLENDMODE_INVALID = 2147483647
SDL_BLENDOPERATION_ADD = 1
SDL_BLENDOPERATION_SUBTRACT = 2
SDL_BLENDOPERATION_REV_SUBTRACT = 3
SDL_BLENDOPERATION_MINIMUM = 4
SDL_BLENDOPERATION_MAXIMUM = 5
SDL_BLENDFACTOR_ZERO = 1
SDL_BLENDFACTOR_ONE = 2
SDL_BLENDFACTOR_SRC_COLOR = 3
SDL_BLENDFACTOR_ONE_MINUS_SRC_COLOR = 4
SDL_BLENDFACTOR_SRC_ALPHA = 5
SDL_BLENDFACTOR_ONE_MINUS_SRC_ALPHA = 6
SDL_BLENDFACTOR_DST_COLOR = 7
SDL_BLENDFACTOR_ONE_MINUS_DST_COLOR = 8
SDL_BLENDFACTOR_DST_ALPHA = 9
SDL_BLENDFACTOR_ONE_MINUS_DST_ALPHA = 10

# Typedef
SDL_BlendMode = ctypes.c_int
SDL_BlendOperation = ctypes.c_int
SDL_BlendFactor = ctypes.c_int

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_ComposeCustomBlendMode')
    SDL2_API_ARGS_MAP['SDL_ComposeCustomBlendMode'] = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_ComposeCustomBlendMode'] = ctypes.c_int


