import ctypes, ctypes.util
import sys, os
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2')) # '/usr/local/lib/libSDL2.dylib'

    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
    # sdl2.SDL_SetMainReady()

    version = sdl2.SDL_version()
    sdl2.SDL_GetVersion(ctypes.byref(version))
    print('Major, Minor and Patch: ', version.major, version.minor, version.patch)
    print('Revision and its Number: ', sdl2.SDL_GetRevision(), sdl2.SDL_GetRevisionNumber())

    print('Base Path: ', sdl2.SDL_GetBasePath())
    print('Touch Devices: ', sdl2.SDL_GetNumTouchDevices())
    print('Power State: ', sdl2.SDL_GetPowerInfo(None, None))

    print('Have AVX: ', sdl2.SDL_HasAVX())
    print('System RAM: ', sdl2.SDL_GetSystemRAM())

    print('Platform: ', sdl2.SDL_GetPlatform())

    print('Pixel Format: ', sdl2.SDL_GetPixelFormatName(sdl2.SDL_PIXELFORMAT_RGBA32))

    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
