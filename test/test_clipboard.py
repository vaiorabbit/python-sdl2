import ctypes, ctypes.util
import sys, os
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2')) # '/usr/local/lib/libSDL2.dylib'

    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

    print(sdl2.SDL_HasClipboardText())
    print(sdl2.SDL_GetClipboardText())
    print(sdl2.SDL_SetClipboardText(b"Hello, world."))
    print(sdl2.SDL_HasClipboardText())
    print(sdl2.SDL_GetClipboardText())

    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
