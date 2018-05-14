from .api import *
from .sdl2 import *
from .sdl2_hints import *
from .sdl2_cpuinfo import *
from .sdl2_version import *
from .sdl2_timer import *
from .sdl2_events import *
from .sdl2_keyboard import *
from .sdl2_keycode import *
from .sdl2_scancode import *
from .sdl2_audio import *
from .sdl2_rwops import *
from .sdl2_platform import *
from .sdl2_error import *
from .sdl2_clipboard import *
from .sdl2_rect import *
from .sdl2_render import *
from .sdl2_video import *
from .sdl2_surface import *
from .sdl2_filesystem import *
from .sdl2_log import *
from .sdl2_haptic import *
from .sdl2_touch import *
from .sdl2_power import *
from .sdl2_pixels import *
from .sdl2_messagebox import *
from .sdl2_gesture import *
from .sdl2_vulkan import *
from .sdl2_gamecontroller import *
from .sdl2_joystick import *
from .sdl2_mouse import *
from .sdl2_shape import *
from .sdl2_blendmode import *

from .sdl2_ttf import *
from .sdl2_image import *
from .sdl2_gfxPrimitives import *
from .sdl2_rotozoom import *
from .sdl2_imageFilter import *
from .sdl2_framerate import *

__author__  = 'vaiorabbit'
__version__ = '1.0.0'
__license__ = 'zlib'

def sdl2_load(lib, output_error = False, *, ttf_libpath = None, img_libpath = None, gfx_libpath = None):

    api.SDL2_LOADER = ctypes.cdll.LoadLibrary(lib)

    # api.setup_symbols(lib, output_error)
    sdl2.setup_symbols()
    sdl2_cpuinfo.setup_symbols()
    sdl2_version.setup_symbols()
    sdl2_timer.setup_symbols()
    sdl2_events.setup_symbols()
    sdl2_keyboard.setup_symbols()
    sdl2_keycode.setup_symbols()
    sdl2_scancode.setup_symbols()
    sdl2_audio.setup_symbols()
    sdl2_rwops.setup_symbols()
    sdl2_platform.setup_symbols()
    sdl2_error.setup_symbols()
    sdl2_clipboard.setup_symbols()
    sdl2_rect.setup_symbols()
    sdl2_render.setup_symbols()
    sdl2_video.setup_symbols()
    sdl2_surface.setup_symbols()
    sdl2_filesystem.setup_symbols()
    sdl2_log.setup_symbols()
    sdl2_haptic.setup_symbols()
    sdl2_touch.setup_symbols()
    sdl2_power.setup_symbols()
    sdl2_pixels.setup_symbols()
    sdl2_messagebox.setup_symbols()
    sdl2_gesture.setup_symbols()
    sdl2_vulkan.setup_symbols()
    sdl2_gamecontroller.setup_symbols()
    sdl2_joystick.setup_symbols()
    sdl2_mouse.setup_symbols()
    sdl2_shape.setup_symbols()
    sdl2_blendmode.setup_symbols()

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

    if ttf_libpath != None:
        api.SDL2_TTF_LOADER = ctypes.cdll.LoadLibrary(ttf_libpath)
        if api.SDL2_TTF_LOADER != None:
            sdl2_ttf.setup_symbols()
            for name in api.SDL2_TTF_API_NAMES:
                try:
                    func_ptr = getattr(api.SDL2_TTF_LOADER, name) # ctypes _FuncPtr
                    func_ptr.argtypes = api.SDL2_TTF_API_ARGS_MAP[name]
                    func_ptr.restype = api.SDL2_TTF_API_RETVAL_MAP[name]
                    globals()[name] = func_ptr
                except AttributeError:
                    if output_error:
                        print("Python-SDL2 : API {} not found.".format(name))
                finally:
                    pass

    if img_libpath != None:
        api.SDL2_IMG_LOADER = ctypes.cdll.LoadLibrary(img_libpath)
        if api.SDL2_IMG_LOADER != None:
            sdl2_image.setup_symbols()
            for name in api.SDL2_IMG_API_NAMES:
                try:
                    func_ptr = getattr(api.SDL2_IMG_LOADER, name) # ctypes _FuncPtr
                    func_ptr.argtypes = api.SDL2_IMG_API_ARGS_MAP[name]
                    func_ptr.restype = api.SDL2_IMG_API_RETVAL_MAP[name]
                    globals()[name] = func_ptr
                except AttributeError:
                    if output_error:
                        print("Python-SDL2 : API {} not found.".format(name))
                finally:
                    pass

    if gfx_libpath != None:
        api.SDL2_GFX_LOADER = ctypes.cdll.LoadLibrary(gfx_libpath)
        if api.SDL2_GFX_LOADER != None:
            sdl2_gfxPrimitives.setup_symbols()
            sdl2_rotozoom.setup_symbols()
            sdl2_imageFilter.setup_symbols()
            sdl2_framerate.setup_symbols()
            for name in api.SDL2_GFX_API_NAMES:
                try:
                    func_ptr = getattr(api.SDL2_GFX_LOADER, name) # ctypes _FuncPtr
                    func_ptr.argtypes = api.SDL2_GFX_API_ARGS_MAP[name]
                    func_ptr.restype = api.SDL2_GFX_API_RETVAL_MAP[name]
                    globals()[name] = func_ptr
                except AttributeError:
                    if output_error:
                        print("Python-SDL2 : API {} not found.".format(name))
                finally:
                    pass

def sdl2_loaded():

    return api.SDL2_LOADER != None
