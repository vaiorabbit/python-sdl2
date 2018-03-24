import ctypes, ctypes.util
import sys, os, random
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

NUM_OBJECTS = 100

current_alpha = 255
current_color = 255
cycle_direction = 1

def draw_points(renderer):

    global current_alpha, current_color, cycle_direction

    viewport = sdl2.SDL_Rect()

    sdl2.SDL_RenderGetViewport(renderer, ctypes.byref(viewport))

    for i in range(0, 10 * NUM_OBJECTS):
        current_color = current_color + cycle_direction
        if current_color < 0:
            current_color = 0
            cycle_direction = -cycle_direction
        if current_color > 255:
            current_color = 255
            cycle_direction = -cycle_direction

        sdl2.SDL_SetRenderDrawColor(renderer, 255, current_color, current_color, current_alpha)
        x = int(random.random() * 65535) % viewport.w
        y = int(random.random() * 65535) % viewport.h
        sdl2.SDL_RenderDrawPoint(renderer, x, y)


def draw_lines(renderer):

    global current_alpha, current_color, cycle_direction

    rect = sdl2.SDL_Rect()
    viewport = sdl2.SDL_Rect()

    sdl2.SDL_RenderGetViewport(renderer, ctypes.byref(viewport))

    for i in range(0, NUM_OBJECTS):
        current_color = current_color + cycle_direction
        if current_color < 0:
            current_color = 0
            cycle_direction = -cycle_direction
        if current_color > 255:
            current_color = 255
            cycle_direction = -cycle_direction

        sdl2.SDL_SetRenderDrawColor(renderer, 255, current_color, current_color, current_alpha)

        if i == 0:
            sdl2.SDL_RenderDrawLine(renderer, 0, 0, viewport.w - 1, viewport.h - 1)
            sdl2.SDL_RenderDrawLine(renderer, 0, viewport.h - 1, viewport.w - 1, 0)
            sdl2.SDL_RenderDrawLine(renderer, 0, int(viewport.h / 2), viewport.w - 1, int(viewport.h / 2))
            sdl2.SDL_RenderDrawLine(renderer, int(viewport.w / 2), 0, int(viewport.w / 2), viewport.h - 1)
        else:
            x1 = (int(random.random() * 65535) % (viewport.w * 2)) - viewport.w
            x2 = (int(random.random() * 65535) % (viewport.w * 2)) - viewport.w
            y1 = (int(random.random() * 65535) % (viewport.h * 2)) - viewport.h
            y2 = (int(random.random() * 65535) % (viewport.h * 2)) - viewport.h
            sdl2.SDL_RenderDrawLine(renderer, x1, y1, x2, y2)


def draw_rects(renderer):

    global current_alpha, current_color, cycle_direction

    rect = sdl2.SDL_Rect()
    viewport = sdl2.SDL_Rect()

    sdl2.SDL_RenderGetViewport(renderer, ctypes.byref(viewport))

    for i in range(0, NUM_OBJECTS):
        current_color = current_color + cycle_direction
        if current_color < 0:
            current_color = 0
            cycle_direction = -cycle_direction
        if current_color > 255:
            current_color = 255
            cycle_direction = -cycle_direction

        sdl2.SDL_SetRenderDrawColor(renderer, 255, current_color, current_color, current_alpha)

        rect.w = (int(random.random() * 65535) % int(viewport.h / 2))
        rect.h = (int(random.random() * 65535) % int(viewport.h / 2))

        rect.x = ((int(random.random() * 65535) % (viewport.w * 2)) - viewport.w) - int(rect.w / 2)
        rect.y = ((int(random.random() * 65535) % (viewport.h * 2)) - viewport.h) - int(rect.h / 2)

        sdl2.SDL_RenderFillRect(renderer, ctypes.byref(rect))


def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2')) # '/usr/local/lib/libSDL2.dylib'

    sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)

    WINDOW_W = 640
    WINDOW_H = 360
    window = sdl2.SDL_CreateWindow(b"RenderDrawPoint/RenderDrawLine/RenderFillRect", 0, 0, WINDOW_W, WINDOW_H, sdl2.SDL_WINDOW_OPENGL)

    renderer = sdl2.SDL_CreateRenderer(window, -1, 0)

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
                    done = True

        sdl2.SDL_SetRenderDrawColor(renderer, 0xA0, 0xA0, 0xA0, 0xFF)
        sdl2.SDL_RenderClear(renderer)

        draw_points(renderer)
        draw_lines(renderer)
        draw_rects(renderer)

        sdl2.SDL_RenderPresent(renderer)

    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
