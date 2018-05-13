import ctypes, ctypes.util
import sys, os, threading, time
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2'), # '/usr/local/lib/libSDL2.dylib'
                   ttf_libpath = ctypes.util.find_library('SDL2_ttf')
                   )
    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

    WINDOW_W = 640
    WINDOW_H = 360
    window = sdl2.SDL_CreateWindow(b"Minimal SDL_TTF Test via python-sdl2", 0, 0, WINDOW_W, WINDOW_H, sdl2.SDL_WINDOW_OPENGL)

    renderer = sdl2.SDL_CreateRenderer(window, -1, 0)

    rect = sdl2.SDL_Rect()
    rect.x = 0
    rect.y = 0
    rect.w = WINDOW_W
    rect.h = WINDOW_H

    sdl2.TTF_Init()
    rwops_ptr = sdl2.SDL_RWFromFile(bytes(sys.argv[1], 'utf-8'), b"rb") # rwops = ctypes.cast(rwops_ptr, ctypes.POINTER(sdl2.SDL_RWops)).contents
    font = sdl2.TTF_OpenFontRW(rwops_ptr, 0, 42)

    fg = sdl2.SDL_Color()
    fg.r = 96
    fg.g = 96
    fg.b = 96
    fg.a = 255

    bg = sdl2.SDL_Color()
    bg.r = 0xE0
    bg.g = 0xE0
    bg.b = 0xE0
    bg.a = 255

    pos = [
        sdl2.SDL_Rect(),
        sdl2.SDL_Rect(),
    ]
    pos[0].x = 20
    pos[0].y = 120
    pos[0].w = 600
    pos[0].h = 60

    pos[1].x = 20
    pos[1].y = 180
    pos[1].w = 600
    pos[1].h = 60

    surfaces = [
        sdl2.TTF_RenderUTF8_Shaded(font, bytes("志於道、據於徳、依於仁、游於藝", 'utf-8'), fg, bg),
        sdl2.TTF_RenderUTF8_Shaded(font, bytes("ＳＣＯＲＥ　１２３４５６７８０", 'utf-8'), fg, bg),
    ]

    texture = [
        sdl2.SDL_CreateTextureFromSurface(renderer, surfaces[0]),
        sdl2.SDL_CreateTextureFromSurface(renderer, surfaces[1]),
    ]

    sdl2.SDL_SetRenderDrawColor(renderer, bg.r, bg.g, bg.b, bg.a)
    sdl2.SDL_RenderFillRect(renderer, ctypes.byref(rect))
    sdl2.SDL_RenderCopy(renderer, texture[0], None, ctypes.byref(pos[0]))
    sdl2.SDL_RenderCopy(renderer, texture[1], None, ctypes.byref(pos[1]))

    sdl2.SDL_RenderPresent(renderer)

    sdl2.SDL_FreeSurface(surfaces[0])
    sdl2.SDL_FreeSurface(surfaces[1])

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

        sdl2.SDL_Delay(fpsdelay)

    sdl2.TTF_Quit()
    sdl2.SDL_DestroyRenderer(renderer)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
