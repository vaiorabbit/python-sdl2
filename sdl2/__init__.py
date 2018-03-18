from .defs import *
from .api import *
from .sdl2 import *
from .sdl2_cpuinfo import *
from .sdl2_version import *
from .sdl2_timer import *

__author__  = 'vaiorabbit'
__version__ = '1.0.0'
__license__ = 'zlib'

def sdl2_load(lib, output_error = False):

    api.SDL2_LOADER = ctypes.cdll.LoadLibrary(lib)

    # api.setup_symbols(lib, output_error)
    sdl2.setup_symbols()
    sdl2_cpuinfo.setup_symbols()
    sdl2_version.setup_symbols()
    sdl2_timer.setup_symbols()

    # SDL2_API_NAMES.append('SDL_SetMainReady')
    # SDL2_API_ARGS_MAP['SDL_SetMainReady'] = []
    # SDL2_API_RETVAL_MAP['SDL_SetMainReady'] = None

    for name in api.SDL2_API_NAMES:
        try:
            func_ptr = getattr(api.SDL2_LOADER, name) # ctypes _FuncPtr
            func_ptr.argtypes = api.SDL2_API_ARGS_MAP[name]
            func_ptr.restype = api.SDL2_API_RETVAL_MAP[name]
            globals()[name] = func_ptr
        except AttributeError:
            if output_error:
                print("Python-SDL2 : API {} not found.".format(name))
        finally:
            pass


def sdl2_loaded():

    return api.SDL2_LOADER != None
