import ctypes, ctypes.util
import sys, os, threading, time
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2'), # '/usr/local/lib/libSDL2.dylib'
                   ttf_libpath = ctypes.util.find_library('SDL2_ttf'),
                   img_libpath = ctypes.util.find_library('SDL2_image'),
                   gfx_libpath = ctypes.util.find_library('SDL2_gfx')
                   )
    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

    WINDOW_W = 640
    WINDOW_H = 360
    window = sdl2.SDL_CreateWindow(b"Minimal SDL2_gfx Test via python-sdl2", 0, 0, WINDOW_W, WINDOW_H, sdl2.SDL_WINDOW_OPENGL)

    renderer = sdl2.SDL_CreateRenderer(window, -1, 0)

    fpsdelay = 100
    count = 0
    event = sdl2.SDL_Event()
    done = False
    while not done:
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            # 'type' and 'timestamp' are common members for all SDL Event structs.
            event_type = event.common.type
            # event_timestamp = event.common.timestamp
            # print("Event : type=0x%s, timestamp=%s" % (event_type, event_timestamp) )

            if event_type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                    done = True

        sdl2.SDL_SetRenderDrawColor(renderer, 0xA0, 0xA0, 0xA0, 0xFF)
        sdl2.SDL_RenderClear(renderer)

        sdl2.pixelColor(renderer, 100, 100, 0xFFFFFFFF) # Uint32 color = 0x[AA][BB][GG][RR]
        sdl2.pixelRGBA(renderer, 101, 100, 0xFF, 0x00, 0x00, 0xFF)

        sdl2.hlineColor(renderer, 0, 100, 50, 0xFFFFFFFF)
        sdl2.vlineColor(renderer, 50, 0, 100, 0xFFFF00FF)

        sdl2.rectangleColor(renderer, 5, 5, 95, 95, 0xFF00FFFF)
        sdl2.rectangleRGBA(renderer, 10, 10, 90, 90, 0, 0, 0xFF, 0xFF)

        sdl2.circleColor(renderer, 150, 150, 50, 0xFF00FF00)
        sdl2.filledCircleRGBA(renderer, 150, 150, 45, 0x00, 0xFF, 0x00, 0xFF)

        sdl2.aalineColor(renderer, 200, 200, 300, 300, 0xFFFFFFFF)
        sdl2.aalineColor(renderer, 300, 200, 200, 300, 0xFFFFFFFF)

        sdl2.aacircleColor(renderer, 300, 200, 25, 0xFF00FF00)
        sdl2.pieColor(renderer, 200, 300, 25, 0, 270, 0xFF00FF00)

        sdl2.SDL_RenderPresent(renderer)

        sdl2.SDL_Delay(fpsdelay)

    sdl2.IMG_Quit()
    sdl2.SDL_DestroyRenderer(renderer)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
