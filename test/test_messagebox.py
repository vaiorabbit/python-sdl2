import ctypes, ctypes.util
import sys, os
sys.path.append(os.pardir)

import sdl2
#from sdl2 import *

def main():
    sdl2.sdl2_load(ctypes.util.find_library('SDL2')) # '/usr/local/lib/libSDL2.dylib'

    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

    # SDL_ShowSimpleMessageBox
    success = sdl2.SDL_ShowSimpleMessageBox(sdl2.SDL_MESSAGEBOX_ERROR,
                                            b"Simple MessageBox",
                                            'これが SDL_ShowSimpleMessageBox です。'.encode('utf8'),
                                            None)

    # SDL_ShowMessageBox
    button = (sdl2.SDL_MessageBoxButtonData * 2)() # _main__.SDL_MessageBoxButtonData_Array_2

    button[0].flags = sdl2.SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT
    button[0].buttonid = 0
    button[0].text = b"OK"

    button[1].flags = sdl2.SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT
    button[1].buttonid = 1
    button[1].text = b"Cancel"

    data = sdl2.SDL_MessageBoxData()
    data.flags = sdl2.SDL_MESSAGEBOX_INFORMATION
    data.window = None
    data.title = b"Custom MessageBox"
    data.message = "カスタマイズされたメッセージボックスの利用例です。".encode('utf8')
    data.numbuttons = 2
    data.buttons = ctypes.cast(button, ctypes.c_void_p)
    data.colorScheme = None

    buttonid = ctypes.c_int()
    retval = sdl2.SDL_ShowMessageBox(ctypes.byref(data), ctypes.byref(buttonid))
    print(retval, buttonid)

    sdl2.SDL_Quit()

if __name__ == '__main__':
    main()
