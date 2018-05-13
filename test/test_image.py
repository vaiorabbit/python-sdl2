import ctypes, ctypes.util
import sys, os, threading, time
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2'), # '/usr/local/lib/libSDL2.dylib'
                   ttf_libpath = ctypes.util.find_library('SDL2_ttf'),
                   img_libpath = ctypes.util.find_library('SDL2_image')
                   )
    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

    WINDOW_W = 640
    WINDOW_H = 360
    window = sdl2.SDL_CreateWindow(b"Minimal SDL_Image Test via python-sdl2", 0, 0, WINDOW_W, WINDOW_H, sdl2.SDL_WINDOW_OPENGL)

    renderer = sdl2.SDL_CreateRenderer(window, -1, 0)

    sdl2.IMG_Init(sdl2.IMG_INIT_JPG|sdl2.IMG_INIT_PNG|sdl2.IMG_INIT_TIF|sdl2.IMG_INIT_WEBP)

    rwops_ptr = sdl2.SDL_RWFromFile(bytes(sys.argv[1], 'utf-8'), b"rb")

    print("PNG?: %s" % ('true' if sdl2.IMG_isPNG(rwops_ptr) else 'false'))

    texture = sdl2.IMG_LoadTexture_RW(renderer, rwops_ptr, 1)

    wh = 300
    pos = sdl2.SDL_Rect()
    pos.x = int((WINDOW_W - wh) / 2)
    pos.y = int((WINDOW_H - wh) / 2)
    pos.w = wh
    pos.h = wh

    sdl2.SDL_RenderCopy(renderer, texture, None, ctypes.byref(pos))

    sdl2.SDL_RenderPresent(renderer)

    fpsdelay = 100
    count = 0
    event = sdl2.SDL_Event()
    done = False
    while not done:
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            # 'type' and 'timestamp' are common members for all SDL Event structs.
            event_type = event.common.type
            event_timestamp = event.common.timestamp
            # print("Event : type=0x%s, timestamp=%s" % (event_type, event_timestamp) )

            if event_type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                    done = True

        sdl2.SDL_SetRenderDrawColor(renderer, 0xA0, 0xA0, 0xA0, 0xFF)
        sdl2.SDL_RenderClear(renderer)
        sdl2.SDL_RenderCopy(renderer, texture, None, ctypes.byref(pos))
        sdl2.SDL_RenderPresent(renderer)

        sdl2.SDL_Delay(fpsdelay)

    sdl2.IMG_Quit()
    sdl2.SDL_DestroyRenderer(renderer)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
