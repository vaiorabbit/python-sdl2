import ctypes, ctypes.util
import sys, os
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2')) # '/usr/local/lib/libSDL2.dylib'

    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

    WINDOW_W = 320
    WINDOW_H = 240
    window = sdl2.SDL_CreateWindow(b"1st SDL Window via Python-SDL2", 0, 0, WINDOW_W, WINDOW_H, 0)

    fpsdelay = 100
    count = 0
    event = sdl2.SDL_Event()
    done = False
    while not done:
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            # 'type' and 'timestamp' are common members for all SDL Event structs.
            event_type = event.common.type
            event_timestamp = event.common.timestamp
            print("Event : type=0x%s, timestamp=%s" % (event_type, event_timestamp) )

            if event_type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                    print("\tSPACE key pressed.")


        count += 1
        if count >= 100:
            done = True
        sdl2.SDL_Delay(fpsdelay)

    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
