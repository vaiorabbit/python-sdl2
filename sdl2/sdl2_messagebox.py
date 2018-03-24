# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro

# Enum
SDL_MESSAGEBOX_ERROR = 16
SDL_MESSAGEBOX_WARNING = 32
SDL_MESSAGEBOX_INFORMATION = 64
SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT = 1
SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT = 2
SDL_MESSAGEBOX_COLOR_BACKGROUND = 0
SDL_MESSAGEBOX_COLOR_TEXT = 1
SDL_MESSAGEBOX_COLOR_BUTTON_BORDER = 2
SDL_MESSAGEBOX_COLOR_BUTTON_BACKGROUND = 3
SDL_MESSAGEBOX_COLOR_BUTTON_SELECTED = 4
SDL_MESSAGEBOX_COLOR_MAX = 5

# Typedef
SDL_MessageBoxFlags = ctypes.c_int
SDL_MessageBoxButtonFlags = ctypes.c_int
SDL_MessageBoxColorType = ctypes.c_int

# Struct

class SDL_MessageBoxButtonData(ctypes.Structure):
    _fields_ = [
        ("flags", ctypes.c_uint),
        ("buttonid", ctypes.c_int),
        ("text", ctypes.c_char_p),
    ]

class SDL_MessageBoxColor(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_uint8),
        ("g", ctypes.c_uint8),
        ("b", ctypes.c_uint8),
    ]

class SDL_MessageBoxColorScheme(ctypes.Structure):
    _fields_ = [
        ("colors", SDL_MessageBoxColor * 5),
    ]

class SDL_MessageBoxData(ctypes.Structure):
    _fields_ = [
        ("flags", ctypes.c_uint),
        ("window", ctypes.c_void_p),
        ("title", ctypes.c_char_p),
        ("message", ctypes.c_char_p),
        ("numbuttons", ctypes.c_int),
        ("buttons", ctypes.c_void_p),
        ("colorScheme", ctypes.c_void_p),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_ShowMessageBox')
    SDL2_API_ARGS_MAP['SDL_ShowMessageBox'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ShowMessageBox'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_ShowSimpleMessageBox')
    SDL2_API_ARGS_MAP['SDL_ShowSimpleMessageBox'] = [ctypes.c_uint, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ShowSimpleMessageBox'] = ctypes.c_int


