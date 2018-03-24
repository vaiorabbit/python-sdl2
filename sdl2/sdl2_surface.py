# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
from .sdl2_rect import SDL_Rect

# Define/Macro
SDL_SWSURFACE = 0
SDL_PREALLOC = 0x00000001
SDL_RLEACCEL = 0x00000002
SDL_DONTFREE = 0x00000004

# Enum
SDL_YUV_CONVERSION_JPEG = 0
SDL_YUV_CONVERSION_BT601 = 1
SDL_YUV_CONVERSION_BT709 = 2
SDL_YUV_CONVERSION_AUTOMATIC = 3

# Typedef
SDL_blit = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
SDL_YUV_CONVERSION_MODE = ctypes.c_int

# Struct

class SDL_Surface(ctypes.Structure):
    _fields_ = [
        ("flags", ctypes.c_uint),
        ("format", ctypes.c_void_p),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("pitch", ctypes.c_int),
        ("pixels", ctypes.c_void_p),
        ("userdata", ctypes.c_void_p),
        ("locked", ctypes.c_int),
        ("lock_data", ctypes.c_void_p),
        ("clip_rect", SDL_Rect),
        ("map", ctypes.c_void_p),
        ("refcount", ctypes.c_int),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_CreateRGBSurface')
    SDL2_API_ARGS_MAP['SDL_CreateRGBSurface'] = [ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_CreateRGBSurface'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_CreateRGBSurfaceWithFormat')
    SDL2_API_ARGS_MAP['SDL_CreateRGBSurfaceWithFormat'] = [ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_CreateRGBSurfaceWithFormat'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_CreateRGBSurfaceFrom')
    SDL2_API_ARGS_MAP['SDL_CreateRGBSurfaceFrom'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_CreateRGBSurfaceFrom'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_CreateRGBSurfaceWithFormatFrom')
    SDL2_API_ARGS_MAP['SDL_CreateRGBSurfaceWithFormatFrom'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_CreateRGBSurfaceWithFormatFrom'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_FreeSurface')
    SDL2_API_ARGS_MAP['SDL_FreeSurface'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_FreeSurface'] = None

    SDL2_API_NAMES.append('SDL_SetSurfacePalette')
    SDL2_API_ARGS_MAP['SDL_SetSurfacePalette'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetSurfacePalette'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_LockSurface')
    SDL2_API_ARGS_MAP['SDL_LockSurface'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_LockSurface'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_UnlockSurface')
    SDL2_API_ARGS_MAP['SDL_UnlockSurface'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_UnlockSurface'] = None

    SDL2_API_NAMES.append('SDL_LoadBMP_RW')
    SDL2_API_ARGS_MAP['SDL_LoadBMP_RW'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_LoadBMP_RW'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_SaveBMP_RW')
    SDL2_API_ARGS_MAP['SDL_SaveBMP_RW'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SaveBMP_RW'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetSurfaceRLE')
    SDL2_API_ARGS_MAP['SDL_SetSurfaceRLE'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetSurfaceRLE'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetColorKey')
    SDL2_API_ARGS_MAP['SDL_SetColorKey'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_SetColorKey'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetColorKey')
    SDL2_API_ARGS_MAP['SDL_GetColorKey'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetColorKey'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetSurfaceColorMod')
    SDL2_API_ARGS_MAP['SDL_SetSurfaceColorMod'] = [ctypes.c_void_p, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_API_RETVAL_MAP['SDL_SetSurfaceColorMod'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetSurfaceColorMod')
    SDL2_API_ARGS_MAP['SDL_GetSurfaceColorMod'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetSurfaceColorMod'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetSurfaceAlphaMod')
    SDL2_API_ARGS_MAP['SDL_SetSurfaceAlphaMod'] = [ctypes.c_void_p, ctypes.c_uint8]
    SDL2_API_RETVAL_MAP['SDL_SetSurfaceAlphaMod'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetSurfaceAlphaMod')
    SDL2_API_ARGS_MAP['SDL_GetSurfaceAlphaMod'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetSurfaceAlphaMod'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetSurfaceBlendMode')
    SDL2_API_ARGS_MAP['SDL_SetSurfaceBlendMode'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetSurfaceBlendMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetSurfaceBlendMode')
    SDL2_API_ARGS_MAP['SDL_GetSurfaceBlendMode'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetSurfaceBlendMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetClipRect')
    SDL2_API_ARGS_MAP['SDL_SetClipRect'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetClipRect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetClipRect')
    SDL2_API_ARGS_MAP['SDL_GetClipRect'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetClipRect'] = None

    SDL2_API_NAMES.append('SDL_DuplicateSurface')
    SDL2_API_ARGS_MAP['SDL_DuplicateSurface'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_DuplicateSurface'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_ConvertSurface')
    SDL2_API_ARGS_MAP['SDL_ConvertSurface'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_ConvertSurface'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_ConvertSurfaceFormat')
    SDL2_API_ARGS_MAP['SDL_ConvertSurfaceFormat'] = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_ConvertSurfaceFormat'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_ConvertPixels')
    SDL2_API_ARGS_MAP['SDL_ConvertPixels'] = [ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_ConvertPixels'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_FillRect')
    SDL2_API_ARGS_MAP['SDL_FillRect'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_FillRect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_FillRects')
    SDL2_API_ARGS_MAP['SDL_FillRects'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_FillRects'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_UpperBlit')
    SDL2_API_ARGS_MAP['SDL_UpperBlit'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_UpperBlit'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_LowerBlit')
    SDL2_API_ARGS_MAP['SDL_LowerBlit'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_LowerBlit'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SoftStretch')
    SDL2_API_ARGS_MAP['SDL_SoftStretch'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SoftStretch'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_UpperBlitScaled')
    SDL2_API_ARGS_MAP['SDL_UpperBlitScaled'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_UpperBlitScaled'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_LowerBlitScaled')
    SDL2_API_ARGS_MAP['SDL_LowerBlitScaled'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_LowerBlitScaled'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetYUVConversionMode')
    SDL2_API_ARGS_MAP['SDL_SetYUVConversionMode'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetYUVConversionMode'] = None

    SDL2_API_NAMES.append('SDL_GetYUVConversionMode')
    SDL2_API_ARGS_MAP['SDL_GetYUVConversionMode'] = None
    SDL2_API_RETVAL_MAP['SDL_GetYUVConversionMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetYUVConversionModeForResolution')
    SDL2_API_ARGS_MAP['SDL_GetYUVConversionModeForResolution'] = [ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetYUVConversionModeForResolution'] = ctypes.c_int


