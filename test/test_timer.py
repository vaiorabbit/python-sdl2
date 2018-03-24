import ctypes, ctypes.util
import sys, os, threading, time
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

def timer_callback_fn(interval, param):
    print("HI")
    return interval

def timer_test():
    resolution = 60
    cb = sdl2.SDL_TimerCallback(timer_callback_fn)
    print(type(cb))
    t1 = sdl2.SDL_AddTimer(resolution, cb, None)
    print("Waiting Timer...")
    time.sleep(1)
    print("Timer Done.")
    sdl2.SDL_RemoveTimer(t1)

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2')) # '/usr/local/lib/libSDL2.dylib'
    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

    thr = threading.Thread(target = timer_test, name = "thr")
    thr.start()
    print("Waiting Thread...")
    thr.join()
    print("Thread Done.")

    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
