# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro
SDL_INIT_TIMER = 0x00000001
SDL_INIT_AUDIO = 0x00000010
SDL_INIT_VIDEO = 0x00000020
SDL_INIT_JOYSTICK = 0x00000200
SDL_INIT_HAPTIC = 0x00001000
SDL_INIT_GAMECONTROLLER = 0x00002000
SDL_INIT_EVENTS = 0x00004000
SDL_INIT_NOPARACHUTE = 0x00100000
SDL_INIT_EVERYTHING = ( SDL_INIT_TIMER | SDL_INIT_AUDIO | SDL_INIT_VIDEO | SDL_INIT_EVENTS | SDL_INIT_JOYSTICK | SDL_INIT_HAPTIC | SDL_INIT_GAMECONTROLLER )

# Enum

# Typedef

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_Init')
    SDL2_API_ARGS_MAP['SDL_Init'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_Init'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_InitSubSystem')
    SDL2_API_ARGS_MAP['SDL_InitSubSystem'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_InitSubSystem'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_QuitSubSystem')
    SDL2_API_ARGS_MAP['SDL_QuitSubSystem'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_QuitSubSystem'] = None

    SDL2_API_NAMES.append('SDL_WasInit')
    SDL2_API_ARGS_MAP['SDL_WasInit'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_WasInit'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_Quit')
    SDL2_API_ARGS_MAP['SDL_Quit'] = None
    SDL2_API_RETVAL_MAP['SDL_Quit'] = None


