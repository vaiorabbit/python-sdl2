from .defs import *
from .api import *
from .sdl2_symbols import *
from .sdl2_cpuinfo_symbols import *
from .sdl2_version_symbols import *

__author__  = 'vaiorabbit'
__version__ = '1.0.0'
__license__ = 'zlib'

def sdl2_load(lib, output_error = False):

    api.SDL2_LOADER = ctypes.cdll.LoadLibrary(lib)

    sdl2_symbols.setup_symbols()
    sdl2_cpuinfo_symbols.setup_symbols()
    sdl2_version_symbols.setup_symbols()

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
