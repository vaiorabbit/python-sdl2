# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro

# Enum

# Typedef

# Struct

class SDL_Keysym(ctypes.Structure):
    _fields_ = [
        ("scancode", ctypes.c_int),
        ("sym", ctypes.c_int),
        ("mod", ctypes.c_ushort),
        ("unused", ctypes.c_uint),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetKeyboardFocus')
    SDL2_API_ARGS_MAP['SDL_GetKeyboardFocus'] = None
    SDL2_API_RETVAL_MAP['SDL_GetKeyboardFocus'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GetKeyboardState')
    SDL2_API_ARGS_MAP['SDL_GetKeyboardState'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetKeyboardState'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GetModState')
    SDL2_API_ARGS_MAP['SDL_GetModState'] = None
    SDL2_API_RETVAL_MAP['SDL_GetModState'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetModState')
    SDL2_API_ARGS_MAP['SDL_SetModState'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetModState'] = None

    SDL2_API_NAMES.append('SDL_GetKeyFromScancode')
    SDL2_API_ARGS_MAP['SDL_GetKeyFromScancode'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetKeyFromScancode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetScancodeFromKey')
    SDL2_API_ARGS_MAP['SDL_GetScancodeFromKey'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetScancodeFromKey'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetScancodeName')
    SDL2_API_ARGS_MAP['SDL_GetScancodeName'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetScancodeName'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GetScancodeFromName')
    SDL2_API_ARGS_MAP['SDL_GetScancodeFromName'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GetScancodeFromName'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetKeyName')
    SDL2_API_ARGS_MAP['SDL_GetKeyName'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetKeyName'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GetKeyFromName')
    SDL2_API_ARGS_MAP['SDL_GetKeyFromName'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GetKeyFromName'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_StartTextInput')
    SDL2_API_ARGS_MAP['SDL_StartTextInput'] = None
    SDL2_API_RETVAL_MAP['SDL_StartTextInput'] = None

    SDL2_API_NAMES.append('SDL_IsTextInputActive')
    SDL2_API_ARGS_MAP['SDL_IsTextInputActive'] = None
    SDL2_API_RETVAL_MAP['SDL_IsTextInputActive'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_StopTextInput')
    SDL2_API_ARGS_MAP['SDL_StopTextInput'] = None
    SDL2_API_RETVAL_MAP['SDL_StopTextInput'] = None

    SDL2_API_NAMES.append('SDL_SetTextInputRect')
    SDL2_API_ARGS_MAP['SDL_SetTextInputRect'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetTextInputRect'] = None

    SDL2_API_NAMES.append('SDL_HasScreenKeyboardSupport')
    SDL2_API_ARGS_MAP['SDL_HasScreenKeyboardSupport'] = None
    SDL2_API_RETVAL_MAP['SDL_HasScreenKeyboardSupport'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_IsScreenKeyboardShown')
    SDL2_API_ARGS_MAP['SDL_IsScreenKeyboardShown'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_IsScreenKeyboardShown'] = ctypes.c_int


