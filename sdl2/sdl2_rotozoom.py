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
    SDL2_GFX_API_NAMES.append('rotozoomSurface')
    SDL2_GFX_API_ARGS_MAP['rotozoomSurface'] = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_int]
    SDL2_GFX_API_RETVAL_MAP['rotozoomSurface'] = ctypes.c_void_p

    SDL2_GFX_API_NAMES.append('rotozoomSurfaceXY')
    SDL2_GFX_API_ARGS_MAP['rotozoomSurfaceXY'] = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
    SDL2_GFX_API_RETVAL_MAP['rotozoomSurfaceXY'] = ctypes.c_void_p

    SDL2_GFX_API_NAMES.append('rotozoomSurfaceSize')
    SDL2_GFX_API_ARGS_MAP['rotozoomSurfaceSize'] = [ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_GFX_API_RETVAL_MAP['rotozoomSurfaceSize'] = None

    SDL2_GFX_API_NAMES.append('rotozoomSurfaceSizeXY')
    SDL2_GFX_API_ARGS_MAP['rotozoomSurfaceSizeXY'] = [ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_GFX_API_RETVAL_MAP['rotozoomSurfaceSizeXY'] = None

    SDL2_GFX_API_NAMES.append('zoomSurface')
    SDL2_GFX_API_ARGS_MAP['zoomSurface'] = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_int]
    SDL2_GFX_API_RETVAL_MAP['zoomSurface'] = ctypes.c_void_p

    SDL2_GFX_API_NAMES.append('zoomSurfaceSize')
    SDL2_GFX_API_ARGS_MAP['zoomSurfaceSize'] = [ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_GFX_API_RETVAL_MAP['zoomSurfaceSize'] = None

    SDL2_GFX_API_NAMES.append('shrinkSurface')
    SDL2_GFX_API_ARGS_MAP['shrinkSurface'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_GFX_API_RETVAL_MAP['shrinkSurface'] = ctypes.c_void_p

    SDL2_GFX_API_NAMES.append('rotateSurface90Degrees')
    SDL2_GFX_API_ARGS_MAP['rotateSurface90Degrees'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_GFX_API_RETVAL_MAP['rotateSurface90Degrees'] = ctypes.c_void_p


