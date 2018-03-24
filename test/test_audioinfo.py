import ctypes, ctypes.util
import sys, os, threading, time
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

def print_devices(iscapture):
    typestr = "capture" if iscapture else "output"
    n = sdl2.SDL_GetNumAudioDevices(iscapture)

    print("%s devices:" % typestr)

    if n == -1:
        print("  Driver can't detect specific %s devices." % typestr)
    elif n == 0:
        print("  No %s devices found." % typestr)
    else:
        for i in range(0, n):
            print("  %s" % sdl2.SDL_GetAudioDeviceName(i, iscapture))

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2')) # '/usr/local/lib/libSDL2.dylib'
    sdl2.SDL_Init(sdl2.SDL_INIT_AUDIO)

    n = sdl2.SDL_GetNumAudioDrivers()
    if n == 0:
        print("No built-in audio drivers")
    else:
        print("Built-in audio drivers:")

    for i in range(0, n):
        print("  %s" % sdl2.SDL_GetAudioDriver(i))

    print("Using audio driver: %s" % sdl2.SDL_GetCurrentAudioDriver())

    print_devices(0)
    print_devices(1)

    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
