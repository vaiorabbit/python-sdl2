# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro
SDL_CACHELINE_SIZE = 128

# Enum

# Typedef

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetCPUCount')
    SDL2_API_ARGS_MAP['SDL_GetCPUCount'] = None
    SDL2_API_RETVAL_MAP['SDL_GetCPUCount'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetCPUCacheLineSize')
    SDL2_API_ARGS_MAP['SDL_GetCPUCacheLineSize'] = None
    SDL2_API_RETVAL_MAP['SDL_GetCPUCacheLineSize'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasRDTSC')
    SDL2_API_ARGS_MAP['SDL_HasRDTSC'] = None
    SDL2_API_RETVAL_MAP['SDL_HasRDTSC'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasAltiVec')
    SDL2_API_ARGS_MAP['SDL_HasAltiVec'] = None
    SDL2_API_RETVAL_MAP['SDL_HasAltiVec'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasMMX')
    SDL2_API_ARGS_MAP['SDL_HasMMX'] = None
    SDL2_API_RETVAL_MAP['SDL_HasMMX'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_Has3DNow')
    SDL2_API_ARGS_MAP['SDL_Has3DNow'] = None
    SDL2_API_RETVAL_MAP['SDL_Has3DNow'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasSSE')
    SDL2_API_ARGS_MAP['SDL_HasSSE'] = None
    SDL2_API_RETVAL_MAP['SDL_HasSSE'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasSSE2')
    SDL2_API_ARGS_MAP['SDL_HasSSE2'] = None
    SDL2_API_RETVAL_MAP['SDL_HasSSE2'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasSSE3')
    SDL2_API_ARGS_MAP['SDL_HasSSE3'] = None
    SDL2_API_RETVAL_MAP['SDL_HasSSE3'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasSSE41')
    SDL2_API_ARGS_MAP['SDL_HasSSE41'] = None
    SDL2_API_RETVAL_MAP['SDL_HasSSE41'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasSSE42')
    SDL2_API_ARGS_MAP['SDL_HasSSE42'] = None
    SDL2_API_RETVAL_MAP['SDL_HasSSE42'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasAVX')
    SDL2_API_ARGS_MAP['SDL_HasAVX'] = None
    SDL2_API_RETVAL_MAP['SDL_HasAVX'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasAVX2')
    SDL2_API_ARGS_MAP['SDL_HasAVX2'] = None
    SDL2_API_RETVAL_MAP['SDL_HasAVX2'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasNEON')
    SDL2_API_ARGS_MAP['SDL_HasNEON'] = None
    SDL2_API_RETVAL_MAP['SDL_HasNEON'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetSystemRAM')
    SDL2_API_ARGS_MAP['SDL_GetSystemRAM'] = None
    SDL2_API_RETVAL_MAP['SDL_GetSystemRAM'] = ctypes.c_int


