# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro

# Enum
SDL_POWERSTATE_UNKNOWN = 0
SDL_POWERSTATE_ON_BATTERY = 1
SDL_POWERSTATE_NO_BATTERY = 2
SDL_POWERSTATE_CHARGING = 3
SDL_POWERSTATE_CHARGED = 4

# Typedef
SDL_PowerState = ctypes.c_int

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetPowerInfo')
    SDL2_API_ARGS_MAP['SDL_GetPowerInfo'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetPowerInfo'] = ctypes.c_int


