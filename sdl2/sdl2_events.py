# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
from .sdl2_keyboard import SDL_Keysym

# Define/Macro
SDL_RELEASED = 0
SDL_PRESSED = 1
SDL_TEXTEDITINGEVENT_TEXT_SIZE = ( 32 )
SDL_TEXTINPUTEVENT_TEXT_SIZE = ( 32 )
SDL_QUERY = -1
SDL_IGNORE = 0
SDL_DISABLE = 0
SDL_ENABLE = 1

# Enum
SDL_FIRSTEVENT = 0
SDL_QUIT = 256
SDL_APP_TERMINATING = 257
SDL_APP_LOWMEMORY = 258
SDL_APP_WILLENTERBACKGROUND = 259
SDL_APP_DIDENTERBACKGROUND = 260
SDL_APP_WILLENTERFOREGROUND = 261
SDL_APP_DIDENTERFOREGROUND = 262
SDL_WINDOWEVENT = 512
SDL_SYSWMEVENT = 513
SDL_KEYDOWN = 768
SDL_KEYUP = 769
SDL_TEXTEDITING = 770
SDL_TEXTINPUT = 771
SDL_KEYMAPCHANGED = 772
SDL_MOUSEMOTION = 1024
SDL_MOUSEBUTTONDOWN = 1025
SDL_MOUSEBUTTONUP = 1026
SDL_MOUSEWHEEL = 1027
SDL_JOYAXISMOTION = 1536
SDL_JOYBALLMOTION = 1537
SDL_JOYHATMOTION = 1538
SDL_JOYBUTTONDOWN = 1539
SDL_JOYBUTTONUP = 1540
SDL_JOYDEVICEADDED = 1541
SDL_JOYDEVICEREMOVED = 1542
SDL_CONTROLLERAXISMOTION = 1616
SDL_CONTROLLERBUTTONDOWN = 1617
SDL_CONTROLLERBUTTONUP = 1618
SDL_CONTROLLERDEVICEADDED = 1619
SDL_CONTROLLERDEVICEREMOVED = 1620
SDL_CONTROLLERDEVICEREMAPPED = 1621
SDL_FINGERDOWN = 1792
SDL_FINGERUP = 1793
SDL_FINGERMOTION = 1794
SDL_DOLLARGESTURE = 2048
SDL_DOLLARRECORD = 2049
SDL_MULTIGESTURE = 2050
SDL_CLIPBOARDUPDATE = 2304
SDL_DROPFILE = 4096
SDL_DROPTEXT = 4097
SDL_DROPBEGIN = 4098
SDL_DROPCOMPLETE = 4099
SDL_AUDIODEVICEADDED = 4352
SDL_AUDIODEVICEREMOVED = 4353
SDL_RENDER_TARGETS_RESET = 8192
SDL_RENDER_DEVICE_RESET = 8193
SDL_USEREVENT = 32768
SDL_LASTEVENT = 65535
SDL_ADDEVENT = 0
SDL_PEEKEVENT = 1
SDL_GETEVENT = 2

# Typedef
SDL_EventType = ctypes.c_int
SDL_eventaction = ctypes.c_int
SDL_EventFilter = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

# Struct

class SDL_CommonEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
    ]

class SDL_WindowEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("windowID", ctypes.c_uint),
        ("event", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("data1", ctypes.c_int),
        ("data2", ctypes.c_int),
    ]

class SDL_KeyboardEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("windowID", ctypes.c_uint),
        ("state", ctypes.c_uint8),
        ("repeat", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("keysym", SDL_Keysym),
    ]

class SDL_TextEditingEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("windowID", ctypes.c_uint),
        ("text", ctypes.c_char * 32),
        ("start", ctypes.c_int),
        ("length", ctypes.c_int),
    ]

class SDL_TextInputEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("windowID", ctypes.c_uint),
        ("text", ctypes.c_char * 32),
    ]

class SDL_MouseMotionEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("windowID", ctypes.c_uint),
        ("which", ctypes.c_uint),
        ("state", ctypes.c_uint),
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("xrel", ctypes.c_int),
        ("yrel", ctypes.c_int),
    ]

class SDL_MouseButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("windowID", ctypes.c_uint),
        ("which", ctypes.c_uint),
        ("button", ctypes.c_uint8),
        ("state", ctypes.c_uint8),
        ("clicks", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
    ]

class SDL_MouseWheelEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("windowID", ctypes.c_uint),
        ("which", ctypes.c_uint),
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("direction", ctypes.c_uint),
    ]

class SDL_JoyAxisEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("which", ctypes.c_int),
        ("axis", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("value", ctypes.c_short),
        ("padding4", ctypes.c_ushort),
    ]

class SDL_JoyBallEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("which", ctypes.c_int),
        ("ball", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("xrel", ctypes.c_short),
        ("yrel", ctypes.c_short),
    ]

class SDL_JoyHatEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("which", ctypes.c_int),
        ("hat", ctypes.c_uint8),
        ("value", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
    ]

class SDL_JoyButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("which", ctypes.c_int),
        ("button", ctypes.c_uint8),
        ("state", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
    ]

class SDL_JoyDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("which", ctypes.c_int),
    ]

class SDL_ControllerAxisEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("which", ctypes.c_int),
        ("axis", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("value", ctypes.c_short),
        ("padding4", ctypes.c_ushort),
    ]

class SDL_ControllerButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("which", ctypes.c_int),
        ("button", ctypes.c_uint8),
        ("state", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
    ]

class SDL_ControllerDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("which", ctypes.c_int),
    ]

class SDL_AudioDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("which", ctypes.c_uint),
        ("iscapture", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
    ]

class SDL_TouchFingerEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("touchId", ctypes.c_longlong),
        ("fingerId", ctypes.c_longlong),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("dx", ctypes.c_float),
        ("dy", ctypes.c_float),
        ("pressure", ctypes.c_float),
    ]

class SDL_MultiGestureEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("touchId", ctypes.c_longlong),
        ("dTheta", ctypes.c_float),
        ("dDist", ctypes.c_float),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("numFingers", ctypes.c_ushort),
        ("padding", ctypes.c_ushort),
    ]

class SDL_DollarGestureEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("touchId", ctypes.c_longlong),
        ("gestureId", ctypes.c_longlong),
        ("numFingers", ctypes.c_uint),
        ("error", ctypes.c_float),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
    ]

class SDL_DropEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("file", ctypes.c_char_p),
        ("windowID", ctypes.c_uint),
    ]

class SDL_QuitEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
    ]

class SDL_OSEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
    ]

class SDL_UserEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("windowID", ctypes.c_uint),
        ("code", ctypes.c_int),
        ("data1", ctypes.c_void_p),
        ("data2", ctypes.c_void_p),
    ]

class SDL_SysWMEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("timestamp", ctypes.c_uint),
        ("msg", ctypes.c_void_p),
    ]

class SDL_Event(ctypes.Union):
    _fields_ = [
        ("type", ctypes.c_uint),
        ("common", SDL_CommonEvent),
        ("window", SDL_WindowEvent),
        ("key", SDL_KeyboardEvent),
        ("edit", SDL_TextEditingEvent),
        ("text", SDL_TextInputEvent),
        ("motion", SDL_MouseMotionEvent),
        ("button", SDL_MouseButtonEvent),
        ("wheel", SDL_MouseWheelEvent),
        ("jaxis", SDL_JoyAxisEvent),
        ("jball", SDL_JoyBallEvent),
        ("jhat", SDL_JoyHatEvent),
        ("jbutton", SDL_JoyButtonEvent),
        ("jdevice", SDL_JoyDeviceEvent),
        ("caxis", SDL_ControllerAxisEvent),
        ("cbutton", SDL_ControllerButtonEvent),
        ("cdevice", SDL_ControllerDeviceEvent),
        ("adevice", SDL_AudioDeviceEvent),
        ("quit", SDL_QuitEvent),
        ("user", SDL_UserEvent),
        ("syswm", SDL_SysWMEvent),
        ("tfinger", SDL_TouchFingerEvent),
        ("mgesture", SDL_MultiGestureEvent),
        ("dgesture", SDL_DollarGestureEvent),
        ("drop", SDL_DropEvent),
        ("padding", ctypes.c_uint8 * 56),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_PumpEvents')
    SDL2_API_ARGS_MAP['SDL_PumpEvents'] = None
    SDL2_API_RETVAL_MAP['SDL_PumpEvents'] = None

    SDL2_API_NAMES.append('SDL_PeepEvents')
    SDL2_API_ARGS_MAP['SDL_PeepEvents'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_PeepEvents'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasEvent')
    SDL2_API_ARGS_MAP['SDL_HasEvent'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_HasEvent'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HasEvents')
    SDL2_API_ARGS_MAP['SDL_HasEvents'] = [ctypes.c_uint, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_HasEvents'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_FlushEvent')
    SDL2_API_ARGS_MAP['SDL_FlushEvent'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_FlushEvent'] = None

    SDL2_API_NAMES.append('SDL_FlushEvents')
    SDL2_API_ARGS_MAP['SDL_FlushEvents'] = [ctypes.c_uint, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_FlushEvents'] = None

    SDL2_API_NAMES.append('SDL_PollEvent')
    SDL2_API_ARGS_MAP['SDL_PollEvent'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_PollEvent'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_WaitEvent')
    SDL2_API_ARGS_MAP['SDL_WaitEvent'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_WaitEvent'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_WaitEventTimeout')
    SDL2_API_ARGS_MAP['SDL_WaitEventTimeout'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_WaitEventTimeout'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_PushEvent')
    SDL2_API_ARGS_MAP['SDL_PushEvent'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_PushEvent'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetEventFilter')
    SDL2_API_ARGS_MAP['SDL_SetEventFilter'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetEventFilter'] = None

    SDL2_API_NAMES.append('SDL_GetEventFilter')
    SDL2_API_ARGS_MAP['SDL_GetEventFilter'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetEventFilter'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_AddEventWatch')
    SDL2_API_ARGS_MAP['SDL_AddEventWatch'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_AddEventWatch'] = None

    SDL2_API_NAMES.append('SDL_DelEventWatch')
    SDL2_API_ARGS_MAP['SDL_DelEventWatch'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_DelEventWatch'] = None

    SDL2_API_NAMES.append('SDL_FilterEvents')
    SDL2_API_ARGS_MAP['SDL_FilterEvents'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_FilterEvents'] = None

    SDL2_API_NAMES.append('SDL_EventState')
    SDL2_API_ARGS_MAP['SDL_EventState'] = [ctypes.c_uint, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_EventState'] = ctypes.c_uint8

    SDL2_API_NAMES.append('SDL_RegisterEvents')
    SDL2_API_ARGS_MAP['SDL_RegisterEvents'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_RegisterEvents'] = ctypes.c_uint


