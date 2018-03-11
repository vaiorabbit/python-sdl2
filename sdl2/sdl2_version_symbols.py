import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

class SDL_version(ctypes.Structure):
    _fields_ = [
        ("major", ctypes.c_ubyte),
        ("minor", ctypes.c_ubyte),
        ("patch", ctypes.c_ubyte),
    ]

def setup_symbols():

    SDL2_API_NAMES.append('SDL_GetVersion')
    SDL2_API_ARGS_MAP['SDL_GetVersion'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetVersion'] = None
