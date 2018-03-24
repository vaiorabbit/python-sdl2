import ctypes, ctypes.util
import sys, os
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2')) # '/usr/local/lib/libSDL2.dylib'

    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
    # sdl2.SDL_SetMainReady()

    #rwops_ptr = sdl2.SDL_AllocRW()
    rwops_ptr = sdl2.SDL_RWFromFile(b'test_timer.py', b'rb')
    rwops = ctypes.cast(rwops_ptr, ctypes.POINTER(sdl2.SDL_RWops)).contents
    size_func = ctypes.CFUNCTYPE(ctypes.c_int64, ctypes.c_void_p)(rwops.size)
    print(sdl2.SDL_ReadU8(rwops_ptr))
    print(size_func(rwops_ptr))
    sdl2.SDL_FreeRW(rwops_ptr)

    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
