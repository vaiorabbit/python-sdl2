import ctypes, ctypes.util
import sys, os
sys.path.append(os.pardir)

import sdl2

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2')) # '/usr/local/lib/libSDL2.dylib'

    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
    sdl2.SDL_SetMainReady()

    version = sdl2.SDL_version()
    sdl2.SDL_GetVersion(ctypes.byref(version))
    print(version.major, version.minor, version.patch)

    print(sdl2.SDL_HasAVX())
    print(sdl2.SDL_GetSystemRAM())

    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
