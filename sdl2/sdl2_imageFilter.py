# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
from .api import SDL2_GFX_API_NAMES, SDL2_GFX_API_ARGS_MAP, SDL2_GFX_API_RETVAL_MAP

# Define/Macro

# Enum

# Typedef

# Struct

# Function
def setup_symbols():
    SDL2_GFX_API_NAMES.append('SDL_imageFilterMMXdetect')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterMMXdetect'] = None
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterMMXdetect'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterMMXoff')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterMMXoff'] = None
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterMMXoff'] = None

    SDL2_GFX_API_NAMES.append('SDL_imageFilterMMXon')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterMMXon'] = None
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterMMXon'] = None

    SDL2_GFX_API_NAMES.append('SDL_imageFilterAdd')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterAdd'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterAdd'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterMean')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterMean'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterMean'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterSub')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterSub'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterSub'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterAbsDiff')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterAbsDiff'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterAbsDiff'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterMult')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterMult'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterMult'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterMultNor')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterMultNor'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterMultNor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterMultDivby2')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterMultDivby2'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterMultDivby2'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterMultDivby4')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterMultDivby4'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterMultDivby4'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterBitAnd')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterBitAnd'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterBitAnd'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterBitOr')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterBitOr'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterBitOr'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterDiv')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterDiv'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterDiv'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterBitNegation')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterBitNegation'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterBitNegation'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterAddByte')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterAddByte'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterAddByte'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterAddUint')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterAddUint'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterAddUint'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterAddByteToHalf')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterAddByteToHalf'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterAddByteToHalf'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterSubByte')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterSubByte'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterSubByte'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterSubUint')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterSubUint'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterSubUint'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterShiftRight')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterShiftRight'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterShiftRight'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterShiftRightUint')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterShiftRightUint'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterShiftRightUint'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterMultByByte')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterMultByByte'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterMultByByte'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterShiftRightAndMultByByte')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterShiftRightAndMultByByte'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterShiftRightAndMultByByte'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterShiftLeftByte')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterShiftLeftByte'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterShiftLeftByte'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterShiftLeftUint')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterShiftLeftUint'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterShiftLeftUint'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterShiftLeft')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterShiftLeft'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterShiftLeft'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterBinarizeUsingThreshold')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterBinarizeUsingThreshold'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterBinarizeUsingThreshold'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterClipToRange')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterClipToRange'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterClipToRange'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('SDL_imageFilterNormalizeLinear')
    SDL2_GFX_API_ARGS_MAP['SDL_imageFilterNormalizeLinear'] = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    SDL2_GFX_API_RETVAL_MAP['SDL_imageFilterNormalizeLinear'] = ctypes.c_int


