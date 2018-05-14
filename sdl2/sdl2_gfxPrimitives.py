# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
from .api import SDL2_GFX_API_NAMES, SDL2_GFX_API_ARGS_MAP, SDL2_GFX_API_RETVAL_MAP

# Define/Macro
SDL2_GFXPRIMITIVES_MAJOR = 1
SDL2_GFXPRIMITIVES_MINOR = 0
SDL2_GFXPRIMITIVES_MICRO = 4

# Enum

# Typedef

# Struct

# Function
def setup_symbols():
    SDL2_GFX_API_NAMES.append('pixelColor')
    SDL2_GFX_API_ARGS_MAP['pixelColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['pixelColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('pixelRGBA')
    SDL2_GFX_API_ARGS_MAP['pixelRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['pixelRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('hlineColor')
    SDL2_GFX_API_ARGS_MAP['hlineColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['hlineColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('hlineRGBA')
    SDL2_GFX_API_ARGS_MAP['hlineRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['hlineRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('vlineColor')
    SDL2_GFX_API_ARGS_MAP['vlineColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['vlineColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('vlineRGBA')
    SDL2_GFX_API_ARGS_MAP['vlineRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['vlineRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('rectangleColor')
    SDL2_GFX_API_ARGS_MAP['rectangleColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['rectangleColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('rectangleRGBA')
    SDL2_GFX_API_ARGS_MAP['rectangleRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['rectangleRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('roundedRectangleColor')
    SDL2_GFX_API_ARGS_MAP['roundedRectangleColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['roundedRectangleColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('roundedRectangleRGBA')
    SDL2_GFX_API_ARGS_MAP['roundedRectangleRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['roundedRectangleRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('boxColor')
    SDL2_GFX_API_ARGS_MAP['boxColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['boxColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('boxRGBA')
    SDL2_GFX_API_ARGS_MAP['boxRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['boxRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('roundedBoxColor')
    SDL2_GFX_API_ARGS_MAP['roundedBoxColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['roundedBoxColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('roundedBoxRGBA')
    SDL2_GFX_API_ARGS_MAP['roundedBoxRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['roundedBoxRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('lineColor')
    SDL2_GFX_API_ARGS_MAP['lineColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['lineColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('lineRGBA')
    SDL2_GFX_API_ARGS_MAP['lineRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['lineRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('aalineColor')
    SDL2_GFX_API_ARGS_MAP['aalineColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['aalineColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('aalineRGBA')
    SDL2_GFX_API_ARGS_MAP['aalineRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['aalineRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('thickLineColor')
    SDL2_GFX_API_ARGS_MAP['thickLineColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['thickLineColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('thickLineRGBA')
    SDL2_GFX_API_ARGS_MAP['thickLineRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['thickLineRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('circleColor')
    SDL2_GFX_API_ARGS_MAP['circleColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['circleColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('circleRGBA')
    SDL2_GFX_API_ARGS_MAP['circleRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['circleRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('arcColor')
    SDL2_GFX_API_ARGS_MAP['arcColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['arcColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('arcRGBA')
    SDL2_GFX_API_ARGS_MAP['arcRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['arcRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('aacircleColor')
    SDL2_GFX_API_ARGS_MAP['aacircleColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['aacircleColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('aacircleRGBA')
    SDL2_GFX_API_ARGS_MAP['aacircleRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['aacircleRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('filledCircleColor')
    SDL2_GFX_API_ARGS_MAP['filledCircleColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['filledCircleColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('filledCircleRGBA')
    SDL2_GFX_API_ARGS_MAP['filledCircleRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['filledCircleRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('ellipseColor')
    SDL2_GFX_API_ARGS_MAP['ellipseColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['ellipseColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('ellipseRGBA')
    SDL2_GFX_API_ARGS_MAP['ellipseRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['ellipseRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('aaellipseColor')
    SDL2_GFX_API_ARGS_MAP['aaellipseColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['aaellipseColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('aaellipseRGBA')
    SDL2_GFX_API_ARGS_MAP['aaellipseRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['aaellipseRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('filledEllipseColor')
    SDL2_GFX_API_ARGS_MAP['filledEllipseColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['filledEllipseColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('filledEllipseRGBA')
    SDL2_GFX_API_ARGS_MAP['filledEllipseRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['filledEllipseRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('pieColor')
    SDL2_GFX_API_ARGS_MAP['pieColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['pieColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('pieRGBA')
    SDL2_GFX_API_ARGS_MAP['pieRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['pieRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('filledPieColor')
    SDL2_GFX_API_ARGS_MAP['filledPieColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['filledPieColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('filledPieRGBA')
    SDL2_GFX_API_ARGS_MAP['filledPieRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['filledPieRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('trigonColor')
    SDL2_GFX_API_ARGS_MAP['trigonColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['trigonColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('trigonRGBA')
    SDL2_GFX_API_ARGS_MAP['trigonRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['trigonRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('aatrigonColor')
    SDL2_GFX_API_ARGS_MAP['aatrigonColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['aatrigonColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('aatrigonRGBA')
    SDL2_GFX_API_ARGS_MAP['aatrigonRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['aatrigonRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('filledTrigonColor')
    SDL2_GFX_API_ARGS_MAP['filledTrigonColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['filledTrigonColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('filledTrigonRGBA')
    SDL2_GFX_API_ARGS_MAP['filledTrigonRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['filledTrigonRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('polygonColor')
    SDL2_GFX_API_ARGS_MAP['polygonColor'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['polygonColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('polygonRGBA')
    SDL2_GFX_API_ARGS_MAP['polygonRGBA'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['polygonRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('aapolygonColor')
    SDL2_GFX_API_ARGS_MAP['aapolygonColor'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['aapolygonColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('aapolygonRGBA')
    SDL2_GFX_API_ARGS_MAP['aapolygonRGBA'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['aapolygonRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('filledPolygonColor')
    SDL2_GFX_API_ARGS_MAP['filledPolygonColor'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['filledPolygonColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('filledPolygonRGBA')
    SDL2_GFX_API_ARGS_MAP['filledPolygonRGBA'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['filledPolygonRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('texturedPolygon')
    SDL2_GFX_API_ARGS_MAP['texturedPolygon'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_GFX_API_RETVAL_MAP['texturedPolygon'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('bezierColor')
    SDL2_GFX_API_ARGS_MAP['bezierColor'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['bezierColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('bezierRGBA')
    SDL2_GFX_API_ARGS_MAP['bezierRGBA'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['bezierRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('gfxPrimitivesSetFont')
    SDL2_GFX_API_ARGS_MAP['gfxPrimitivesSetFont'] = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['gfxPrimitivesSetFont'] = None

    SDL2_GFX_API_NAMES.append('gfxPrimitivesSetFontRotation')
    SDL2_GFX_API_ARGS_MAP['gfxPrimitivesSetFontRotation'] = [ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['gfxPrimitivesSetFontRotation'] = None

    SDL2_GFX_API_NAMES.append('characterColor')
    SDL2_GFX_API_ARGS_MAP['characterColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_char, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['characterColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('characterRGBA')
    SDL2_GFX_API_ARGS_MAP['characterRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_char, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['characterRGBA'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('stringColor')
    SDL2_GFX_API_ARGS_MAP['stringColor'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_char_p, ctypes.c_uint]
    SDL2_GFX_API_RETVAL_MAP['stringColor'] = ctypes.c_int

    SDL2_GFX_API_NAMES.append('stringRGBA')
    SDL2_GFX_API_ARGS_MAP['stringRGBA'] = [ctypes.c_void_p, ctypes.c_short, ctypes.c_short, ctypes.c_char_p, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
    SDL2_GFX_API_RETVAL_MAP['stringRGBA'] = ctypes.c_int


