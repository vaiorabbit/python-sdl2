# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro

# Enum
SDL_RENDERER_SOFTWARE = 1
SDL_RENDERER_ACCELERATED = 2
SDL_RENDERER_PRESENTVSYNC = 4
SDL_RENDERER_TARGETTEXTURE = 8
SDL_TEXTUREACCESS_STATIC = 0
SDL_TEXTUREACCESS_STREAMING = 1
SDL_TEXTUREACCESS_TARGET = 2
SDL_TEXTUREMODULATE_NONE = 0
SDL_TEXTUREMODULATE_COLOR = 1
SDL_TEXTUREMODULATE_ALPHA = 2
SDL_FLIP_NONE = 0
SDL_FLIP_HORIZONTAL = 1
SDL_FLIP_VERTICAL = 2

# Typedef
SDL_RendererFlags = ctypes.c_int
SDL_TextureAccess = ctypes.c_int
SDL_TextureModulate = ctypes.c_int
SDL_RendererFlip = ctypes.c_int

# Struct

class SDL_RendererInfo(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("flags", ctypes.c_uint),
        ("num_texture_formats", ctypes.c_uint),
        ("texture_formats", ctypes.c_uint * 16),
        ("max_texture_width", ctypes.c_int),
        ("max_texture_height", ctypes.c_int),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetNumRenderDrivers')
    SDL2_API_ARGS_MAP['SDL_GetNumRenderDrivers'] = None
    SDL2_API_RETVAL_MAP['SDL_GetNumRenderDrivers'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetRenderDriverInfo')
    SDL2_API_ARGS_MAP['SDL_GetRenderDriverInfo'] = [ctypes.c_int, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetRenderDriverInfo'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_CreateWindowAndRenderer')
    SDL2_API_ARGS_MAP['SDL_CreateWindowAndRenderer'] = [ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_CreateWindowAndRenderer'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_CreateRenderer')
    SDL2_API_ARGS_MAP['SDL_CreateRenderer'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_CreateRenderer'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_CreateSoftwareRenderer')
    SDL2_API_ARGS_MAP['SDL_CreateSoftwareRenderer'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_CreateSoftwareRenderer'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GetRenderer')
    SDL2_API_ARGS_MAP['SDL_GetRenderer'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetRenderer'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GetRendererInfo')
    SDL2_API_ARGS_MAP['SDL_GetRendererInfo'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetRendererInfo'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetRendererOutputSize')
    SDL2_API_ARGS_MAP['SDL_GetRendererOutputSize'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetRendererOutputSize'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_CreateTexture')
    SDL2_API_ARGS_MAP['SDL_CreateTexture'] = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_CreateTexture'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_CreateTextureFromSurface')
    SDL2_API_ARGS_MAP['SDL_CreateTextureFromSurface'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_CreateTextureFromSurface'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_QueryTexture')
    SDL2_API_ARGS_MAP['SDL_QueryTexture'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_QueryTexture'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetTextureColorMod')
    SDL2_API_ARGS_MAP['SDL_SetTextureColorMod'] = [ctypes.c_void_p, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_API_RETVAL_MAP['SDL_SetTextureColorMod'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetTextureColorMod')
    SDL2_API_ARGS_MAP['SDL_GetTextureColorMod'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetTextureColorMod'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetTextureAlphaMod')
    SDL2_API_ARGS_MAP['SDL_SetTextureAlphaMod'] = [ctypes.c_void_p, ctypes.c_uint8]
    SDL2_API_RETVAL_MAP['SDL_SetTextureAlphaMod'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetTextureAlphaMod')
    SDL2_API_ARGS_MAP['SDL_GetTextureAlphaMod'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetTextureAlphaMod'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetTextureBlendMode')
    SDL2_API_ARGS_MAP['SDL_SetTextureBlendMode'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetTextureBlendMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetTextureBlendMode')
    SDL2_API_ARGS_MAP['SDL_GetTextureBlendMode'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetTextureBlendMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_UpdateTexture')
    SDL2_API_ARGS_MAP['SDL_UpdateTexture'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_UpdateTexture'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_UpdateYUVTexture')
    SDL2_API_ARGS_MAP['SDL_UpdateYUVTexture'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_UpdateYUVTexture'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_LockTexture')
    SDL2_API_ARGS_MAP['SDL_LockTexture'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_LockTexture'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_UnlockTexture')
    SDL2_API_ARGS_MAP['SDL_UnlockTexture'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_UnlockTexture'] = None

    SDL2_API_NAMES.append('SDL_RenderTargetSupported')
    SDL2_API_ARGS_MAP['SDL_RenderTargetSupported'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderTargetSupported'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetRenderTarget')
    SDL2_API_ARGS_MAP['SDL_SetRenderTarget'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetRenderTarget'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetRenderTarget')
    SDL2_API_ARGS_MAP['SDL_GetRenderTarget'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetRenderTarget'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_RenderSetLogicalSize')
    SDL2_API_ARGS_MAP['SDL_RenderSetLogicalSize'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RenderSetLogicalSize'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderGetLogicalSize')
    SDL2_API_ARGS_MAP['SDL_RenderGetLogicalSize'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderGetLogicalSize'] = None

    SDL2_API_NAMES.append('SDL_RenderSetIntegerScale')
    SDL2_API_ARGS_MAP['SDL_RenderSetIntegerScale'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RenderSetIntegerScale'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderGetIntegerScale')
    SDL2_API_ARGS_MAP['SDL_RenderGetIntegerScale'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderGetIntegerScale'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderSetViewport')
    SDL2_API_ARGS_MAP['SDL_RenderSetViewport'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderSetViewport'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderGetViewport')
    SDL2_API_ARGS_MAP['SDL_RenderGetViewport'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderGetViewport'] = None

    SDL2_API_NAMES.append('SDL_RenderSetClipRect')
    SDL2_API_ARGS_MAP['SDL_RenderSetClipRect'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderSetClipRect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderGetClipRect')
    SDL2_API_ARGS_MAP['SDL_RenderGetClipRect'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderGetClipRect'] = None

    SDL2_API_NAMES.append('SDL_RenderIsClipEnabled')
    SDL2_API_ARGS_MAP['SDL_RenderIsClipEnabled'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderIsClipEnabled'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderSetScale')
    SDL2_API_ARGS_MAP['SDL_RenderSetScale'] = [ctypes.c_void_p, ctypes.c_float, ctypes.c_float]
    SDL2_API_RETVAL_MAP['SDL_RenderSetScale'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderGetScale')
    SDL2_API_ARGS_MAP['SDL_RenderGetScale'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderGetScale'] = None

    SDL2_API_NAMES.append('SDL_SetRenderDrawColor')
    SDL2_API_ARGS_MAP['SDL_SetRenderDrawColor'] = [ctypes.c_void_p, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_API_RETVAL_MAP['SDL_SetRenderDrawColor'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetRenderDrawColor')
    SDL2_API_ARGS_MAP['SDL_GetRenderDrawColor'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetRenderDrawColor'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetRenderDrawBlendMode')
    SDL2_API_ARGS_MAP['SDL_SetRenderDrawBlendMode'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetRenderDrawBlendMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetRenderDrawBlendMode')
    SDL2_API_ARGS_MAP['SDL_GetRenderDrawBlendMode'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetRenderDrawBlendMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderClear')
    SDL2_API_ARGS_MAP['SDL_RenderClear'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderClear'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderDrawPoint')
    SDL2_API_ARGS_MAP['SDL_RenderDrawPoint'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RenderDrawPoint'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderDrawPoints')
    SDL2_API_ARGS_MAP['SDL_RenderDrawPoints'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RenderDrawPoints'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderDrawLine')
    SDL2_API_ARGS_MAP['SDL_RenderDrawLine'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RenderDrawLine'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderDrawLines')
    SDL2_API_ARGS_MAP['SDL_RenderDrawLines'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RenderDrawLines'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderDrawRect')
    SDL2_API_ARGS_MAP['SDL_RenderDrawRect'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderDrawRect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderDrawRects')
    SDL2_API_ARGS_MAP['SDL_RenderDrawRects'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RenderDrawRects'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderFillRect')
    SDL2_API_ARGS_MAP['SDL_RenderFillRect'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderFillRect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderFillRects')
    SDL2_API_ARGS_MAP['SDL_RenderFillRects'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RenderFillRects'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderCopy')
    SDL2_API_ARGS_MAP['SDL_RenderCopy'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderCopy'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderCopyEx')
    SDL2_API_ARGS_MAP['SDL_RenderCopyEx'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RenderCopyEx'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderReadPixels')
    SDL2_API_ARGS_MAP['SDL_RenderReadPixels'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RenderReadPixels'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderPresent')
    SDL2_API_ARGS_MAP['SDL_RenderPresent'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderPresent'] = None

    SDL2_API_NAMES.append('SDL_DestroyTexture')
    SDL2_API_ARGS_MAP['SDL_DestroyTexture'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_DestroyTexture'] = None

    SDL2_API_NAMES.append('SDL_DestroyRenderer')
    SDL2_API_ARGS_MAP['SDL_DestroyRenderer'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_DestroyRenderer'] = None

    SDL2_API_NAMES.append('SDL_GL_BindTexture')
    SDL2_API_ARGS_MAP['SDL_GL_BindTexture'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GL_BindTexture'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GL_UnbindTexture')
    SDL2_API_ARGS_MAP['SDL_GL_UnbindTexture'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GL_UnbindTexture'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_RenderGetMetalLayer')
    SDL2_API_ARGS_MAP['SDL_RenderGetMetalLayer'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderGetMetalLayer'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_RenderGetMetalCommandEncoder')
    SDL2_API_ARGS_MAP['SDL_RenderGetMetalCommandEncoder'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RenderGetMetalCommandEncoder'] = ctypes.c_void_p


