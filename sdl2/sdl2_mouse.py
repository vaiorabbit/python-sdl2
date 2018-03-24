# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro
SDL_BUTTON_LEFT = 1
SDL_BUTTON_MIDDLE = 2
SDL_BUTTON_RIGHT = 3
SDL_BUTTON_X1 = 4
SDL_BUTTON_X2 = 5

# Enum
SDL_SYSTEM_CURSOR_ARROW = 0
SDL_SYSTEM_CURSOR_IBEAM = 1
SDL_SYSTEM_CURSOR_WAIT = 2
SDL_SYSTEM_CURSOR_CROSSHAIR = 3
SDL_SYSTEM_CURSOR_WAITARROW = 4
SDL_SYSTEM_CURSOR_SIZENWSE = 5
SDL_SYSTEM_CURSOR_SIZENESW = 6
SDL_SYSTEM_CURSOR_SIZEWE = 7
SDL_SYSTEM_CURSOR_SIZENS = 8
SDL_SYSTEM_CURSOR_SIZEALL = 9
SDL_SYSTEM_CURSOR_NO = 10
SDL_SYSTEM_CURSOR_HAND = 11
SDL_NUM_SYSTEM_CURSORS = 12
SDL_MOUSEWHEEL_NORMAL = 0
SDL_MOUSEWHEEL_FLIPPED = 1

# Typedef
SDL_SystemCursor = ctypes.c_int
SDL_MouseWheelDirection = ctypes.c_int

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetMouseFocus')
    SDL2_API_ARGS_MAP['SDL_GetMouseFocus'] = None
    SDL2_API_RETVAL_MAP['SDL_GetMouseFocus'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GetMouseState')
    SDL2_API_ARGS_MAP['SDL_GetMouseState'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetMouseState'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_GetGlobalMouseState')
    SDL2_API_ARGS_MAP['SDL_GetGlobalMouseState'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetGlobalMouseState'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_GetRelativeMouseState')
    SDL2_API_ARGS_MAP['SDL_GetRelativeMouseState'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetRelativeMouseState'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_WarpMouseInWindow')
    SDL2_API_ARGS_MAP['SDL_WarpMouseInWindow'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_WarpMouseInWindow'] = None

    SDL2_API_NAMES.append('SDL_WarpMouseGlobal')
    SDL2_API_ARGS_MAP['SDL_WarpMouseGlobal'] = [ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_WarpMouseGlobal'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetRelativeMouseMode')
    SDL2_API_ARGS_MAP['SDL_SetRelativeMouseMode'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetRelativeMouseMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_CaptureMouse')
    SDL2_API_ARGS_MAP['SDL_CaptureMouse'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_CaptureMouse'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetRelativeMouseMode')
    SDL2_API_ARGS_MAP['SDL_GetRelativeMouseMode'] = None
    SDL2_API_RETVAL_MAP['SDL_GetRelativeMouseMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_CreateCursor')
    SDL2_API_ARGS_MAP['SDL_CreateCursor'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_CreateCursor'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_CreateColorCursor')
    SDL2_API_ARGS_MAP['SDL_CreateColorCursor'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_CreateColorCursor'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_CreateSystemCursor')
    SDL2_API_ARGS_MAP['SDL_CreateSystemCursor'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_CreateSystemCursor'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_SetCursor')
    SDL2_API_ARGS_MAP['SDL_SetCursor'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetCursor'] = None

    SDL2_API_NAMES.append('SDL_GetCursor')
    SDL2_API_ARGS_MAP['SDL_GetCursor'] = None
    SDL2_API_RETVAL_MAP['SDL_GetCursor'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GetDefaultCursor')
    SDL2_API_ARGS_MAP['SDL_GetDefaultCursor'] = None
    SDL2_API_RETVAL_MAP['SDL_GetDefaultCursor'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_FreeCursor')
    SDL2_API_ARGS_MAP['SDL_FreeCursor'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_FreeCursor'] = None

    SDL2_API_NAMES.append('SDL_ShowCursor')
    SDL2_API_ARGS_MAP['SDL_ShowCursor'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_ShowCursor'] = ctypes.c_int


