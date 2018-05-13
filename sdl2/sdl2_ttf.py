# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
from .api import SDL2_TTF_API_NAMES, SDL2_TTF_API_ARGS_MAP, SDL2_TTF_API_RETVAL_MAP
from .sdl2_pixels import SDL_Color

# Define/Macro
SDL_TTF_MAJOR_VERSION = 2
SDL_TTF_MINOR_VERSION = 0
SDL_TTF_PATCHLEVEL = 14

# Enum

# Typedef

# Struct

# Function
def setup_symbols():
    SDL2_TTF_API_NAMES.append('TTF_Linked_Version')
    SDL2_TTF_API_ARGS_MAP['TTF_Linked_Version'] = None
    SDL2_TTF_API_RETVAL_MAP['TTF_Linked_Version'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_ByteSwappedUNICODE')
    SDL2_TTF_API_ARGS_MAP['TTF_ByteSwappedUNICODE'] = [ctypes.c_int]
    SDL2_TTF_API_RETVAL_MAP['TTF_ByteSwappedUNICODE'] = None

    SDL2_TTF_API_NAMES.append('TTF_Init')
    SDL2_TTF_API_ARGS_MAP['TTF_Init'] = None
    SDL2_TTF_API_RETVAL_MAP['TTF_Init'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_OpenFont')
    SDL2_TTF_API_ARGS_MAP['TTF_OpenFont'] = [ctypes.c_char_p, ctypes.c_int]
    SDL2_TTF_API_RETVAL_MAP['TTF_OpenFont'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_OpenFontIndex')
    SDL2_TTF_API_ARGS_MAP['TTF_OpenFontIndex'] = [ctypes.c_char_p, ctypes.c_int, ctypes.c_long]
    SDL2_TTF_API_RETVAL_MAP['TTF_OpenFontIndex'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_OpenFontRW')
    SDL2_TTF_API_ARGS_MAP['TTF_OpenFontRW'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_TTF_API_RETVAL_MAP['TTF_OpenFontRW'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_OpenFontIndexRW')
    SDL2_TTF_API_ARGS_MAP['TTF_OpenFontIndexRW'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_long]
    SDL2_TTF_API_RETVAL_MAP['TTF_OpenFontIndexRW'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_GetFontStyle')
    SDL2_TTF_API_ARGS_MAP['TTF_GetFontStyle'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_GetFontStyle'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_SetFontStyle')
    SDL2_TTF_API_ARGS_MAP['TTF_SetFontStyle'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_TTF_API_RETVAL_MAP['TTF_SetFontStyle'] = None

    SDL2_TTF_API_NAMES.append('TTF_GetFontOutline')
    SDL2_TTF_API_ARGS_MAP['TTF_GetFontOutline'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_GetFontOutline'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_SetFontOutline')
    SDL2_TTF_API_ARGS_MAP['TTF_SetFontOutline'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_TTF_API_RETVAL_MAP['TTF_SetFontOutline'] = None

    SDL2_TTF_API_NAMES.append('TTF_GetFontHinting')
    SDL2_TTF_API_ARGS_MAP['TTF_GetFontHinting'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_GetFontHinting'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_SetFontHinting')
    SDL2_TTF_API_ARGS_MAP['TTF_SetFontHinting'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_TTF_API_RETVAL_MAP['TTF_SetFontHinting'] = None

    SDL2_TTF_API_NAMES.append('TTF_FontHeight')
    SDL2_TTF_API_ARGS_MAP['TTF_FontHeight'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_FontHeight'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_FontAscent')
    SDL2_TTF_API_ARGS_MAP['TTF_FontAscent'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_FontAscent'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_FontDescent')
    SDL2_TTF_API_ARGS_MAP['TTF_FontDescent'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_FontDescent'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_FontLineSkip')
    SDL2_TTF_API_ARGS_MAP['TTF_FontLineSkip'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_FontLineSkip'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_GetFontKerning')
    SDL2_TTF_API_ARGS_MAP['TTF_GetFontKerning'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_GetFontKerning'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_SetFontKerning')
    SDL2_TTF_API_ARGS_MAP['TTF_SetFontKerning'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_TTF_API_RETVAL_MAP['TTF_SetFontKerning'] = None

    SDL2_TTF_API_NAMES.append('TTF_FontFaces')
    SDL2_TTF_API_ARGS_MAP['TTF_FontFaces'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_FontFaces'] = ctypes.c_long

    SDL2_TTF_API_NAMES.append('TTF_FontFaceIsFixedWidth')
    SDL2_TTF_API_ARGS_MAP['TTF_FontFaceIsFixedWidth'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_FontFaceIsFixedWidth'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_FontFaceFamilyName')
    SDL2_TTF_API_ARGS_MAP['TTF_FontFaceFamilyName'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_FontFaceFamilyName'] = ctypes.c_char_p

    SDL2_TTF_API_NAMES.append('TTF_FontFaceStyleName')
    SDL2_TTF_API_ARGS_MAP['TTF_FontFaceStyleName'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_FontFaceStyleName'] = ctypes.c_char_p

    SDL2_TTF_API_NAMES.append('TTF_GlyphIsProvided')
    SDL2_TTF_API_ARGS_MAP['TTF_GlyphIsProvided'] = [ctypes.c_void_p, ctypes.c_ushort]
    SDL2_TTF_API_RETVAL_MAP['TTF_GlyphIsProvided'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_GlyphMetrics')
    SDL2_TTF_API_ARGS_MAP['TTF_GlyphMetrics'] = [ctypes.c_void_p, ctypes.c_ushort, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_GlyphMetrics'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_SizeText')
    SDL2_TTF_API_ARGS_MAP['TTF_SizeText'] = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_SizeText'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_SizeUTF8')
    SDL2_TTF_API_ARGS_MAP['TTF_SizeUTF8'] = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_SizeUTF8'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_SizeUNICODE')
    SDL2_TTF_API_ARGS_MAP['TTF_SizeUNICODE'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_SizeUNICODE'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_RenderText_Solid')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderText_Solid'] = [ctypes.c_void_p, ctypes.c_char_p, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderText_Solid'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderUTF8_Solid')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderUTF8_Solid'] = [ctypes.c_void_p, ctypes.c_char_p, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderUTF8_Solid'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderUNICODE_Solid')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderUNICODE_Solid'] = [ctypes.c_void_p, ctypes.c_void_p, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderUNICODE_Solid'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderGlyph_Solid')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderGlyph_Solid'] = [ctypes.c_void_p, ctypes.c_ushort, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderGlyph_Solid'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderText_Shaded')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderText_Shaded'] = [ctypes.c_void_p, ctypes.c_char_p, SDL_Color, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderText_Shaded'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderUTF8_Shaded')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderUTF8_Shaded'] = [ctypes.c_void_p, ctypes.c_char_p, SDL_Color, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderUTF8_Shaded'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderUNICODE_Shaded')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderUNICODE_Shaded'] = [ctypes.c_void_p, ctypes.c_void_p, SDL_Color, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderUNICODE_Shaded'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderGlyph_Shaded')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderGlyph_Shaded'] = [ctypes.c_void_p, ctypes.c_ushort, SDL_Color, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderGlyph_Shaded'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderText_Blended')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderText_Blended'] = [ctypes.c_void_p, ctypes.c_char_p, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderText_Blended'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderUTF8_Blended')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderUTF8_Blended'] = [ctypes.c_void_p, ctypes.c_char_p, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderUTF8_Blended'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderUNICODE_Blended')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderUNICODE_Blended'] = [ctypes.c_void_p, ctypes.c_void_p, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderUNICODE_Blended'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderText_Blended_Wrapped')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderText_Blended_Wrapped'] = [ctypes.c_void_p, ctypes.c_char_p, SDL_Color, ctypes.c_uint]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderText_Blended_Wrapped'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderUTF8_Blended_Wrapped')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderUTF8_Blended_Wrapped'] = [ctypes.c_void_p, ctypes.c_char_p, SDL_Color, ctypes.c_uint]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderUTF8_Blended_Wrapped'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderUNICODE_Blended_Wrapped')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderUNICODE_Blended_Wrapped'] = [ctypes.c_void_p, ctypes.c_void_p, SDL_Color, ctypes.c_uint]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderUNICODE_Blended_Wrapped'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_RenderGlyph_Blended')
    SDL2_TTF_API_ARGS_MAP['TTF_RenderGlyph_Blended'] = [ctypes.c_void_p, ctypes.c_ushort, SDL_Color]
    SDL2_TTF_API_RETVAL_MAP['TTF_RenderGlyph_Blended'] = ctypes.c_void_p

    SDL2_TTF_API_NAMES.append('TTF_CloseFont')
    SDL2_TTF_API_ARGS_MAP['TTF_CloseFont'] = [ctypes.c_void_p]
    SDL2_TTF_API_RETVAL_MAP['TTF_CloseFont'] = None

    SDL2_TTF_API_NAMES.append('TTF_Quit')
    SDL2_TTF_API_ARGS_MAP['TTF_Quit'] = None
    SDL2_TTF_API_RETVAL_MAP['TTF_Quit'] = None

    SDL2_TTF_API_NAMES.append('TTF_WasInit')
    SDL2_TTF_API_ARGS_MAP['TTF_WasInit'] = None
    SDL2_TTF_API_RETVAL_MAP['TTF_WasInit'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_GetFontKerningSize')
    SDL2_TTF_API_ARGS_MAP['TTF_GetFontKerningSize'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_TTF_API_RETVAL_MAP['TTF_GetFontKerningSize'] = ctypes.c_int

    SDL2_TTF_API_NAMES.append('TTF_GetFontKerningSizeGlyphs')
    SDL2_TTF_API_ARGS_MAP['TTF_GetFontKerningSizeGlyphs'] = [ctypes.c_void_p, ctypes.c_ushort, ctypes.c_ushort]
    SDL2_TTF_API_RETVAL_MAP['TTF_GetFontKerningSizeGlyphs'] = ctypes.c_int


