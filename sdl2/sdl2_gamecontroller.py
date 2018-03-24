# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
from .sdl2_joystick import SDL_JoystickGUID

# Define/Macro

# Enum
SDL_CONTROLLER_BINDTYPE_NONE = 0
SDL_CONTROLLER_BINDTYPE_BUTTON = 1
SDL_CONTROLLER_BINDTYPE_AXIS = 2
SDL_CONTROLLER_BINDTYPE_HAT = 3
SDL_CONTROLLER_AXIS_INVALID = -1
SDL_CONTROLLER_AXIS_LEFTX = 0
SDL_CONTROLLER_AXIS_LEFTY = 1
SDL_CONTROLLER_AXIS_RIGHTX = 2
SDL_CONTROLLER_AXIS_RIGHTY = 3
SDL_CONTROLLER_AXIS_TRIGGERLEFT = 4
SDL_CONTROLLER_AXIS_TRIGGERRIGHT = 5
SDL_CONTROLLER_AXIS_MAX = 6
SDL_CONTROLLER_BUTTON_INVALID = -1
SDL_CONTROLLER_BUTTON_A = 0
SDL_CONTROLLER_BUTTON_B = 1
SDL_CONTROLLER_BUTTON_X = 2
SDL_CONTROLLER_BUTTON_Y = 3
SDL_CONTROLLER_BUTTON_BACK = 4
SDL_CONTROLLER_BUTTON_GUIDE = 5
SDL_CONTROLLER_BUTTON_START = 6
SDL_CONTROLLER_BUTTON_LEFTSTICK = 7
SDL_CONTROLLER_BUTTON_RIGHTSTICK = 8
SDL_CONTROLLER_BUTTON_LEFTSHOULDER = 9
SDL_CONTROLLER_BUTTON_RIGHTSHOULDER = 10
SDL_CONTROLLER_BUTTON_DPAD_UP = 11
SDL_CONTROLLER_BUTTON_DPAD_DOWN = 12
SDL_CONTROLLER_BUTTON_DPAD_LEFT = 13
SDL_CONTROLLER_BUTTON_DPAD_RIGHT = 14
SDL_CONTROLLER_BUTTON_MAX = 15

# Typedef
SDL_GameControllerBindType = ctypes.c_int
SDL_GameControllerAxis = ctypes.c_int
SDL_GameControllerButton = ctypes.c_int

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GameControllerAddMappingsFromRW')
    SDL2_API_ARGS_MAP['SDL_GameControllerAddMappingsFromRW'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerAddMappingsFromRW'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GameControllerAddMapping')
    SDL2_API_ARGS_MAP['SDL_GameControllerAddMapping'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerAddMapping'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GameControllerNumMappings')
    SDL2_API_ARGS_MAP['SDL_GameControllerNumMappings'] = None
    SDL2_API_RETVAL_MAP['SDL_GameControllerNumMappings'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GameControllerMappingForIndex')
    SDL2_API_ARGS_MAP['SDL_GameControllerMappingForIndex'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerMappingForIndex'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GameControllerMappingForGUID')
    SDL2_API_ARGS_MAP['SDL_GameControllerMappingForGUID'] = [SDL_JoystickGUID]
    SDL2_API_RETVAL_MAP['SDL_GameControllerMappingForGUID'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GameControllerMapping')
    SDL2_API_ARGS_MAP['SDL_GameControllerMapping'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerMapping'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_IsGameController')
    SDL2_API_ARGS_MAP['SDL_IsGameController'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_IsGameController'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GameControllerNameForIndex')
    SDL2_API_ARGS_MAP['SDL_GameControllerNameForIndex'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerNameForIndex'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GameControllerOpen')
    SDL2_API_ARGS_MAP['SDL_GameControllerOpen'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerOpen'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GameControllerFromInstanceID')
    SDL2_API_ARGS_MAP['SDL_GameControllerFromInstanceID'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerFromInstanceID'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GameControllerName')
    SDL2_API_ARGS_MAP['SDL_GameControllerName'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerName'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GameControllerGetVendor')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetVendor'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetVendor'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_GameControllerGetProduct')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetProduct'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetProduct'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_GameControllerGetProductVersion')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetProductVersion'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetProductVersion'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_GameControllerGetAttached')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetAttached'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetAttached'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GameControllerGetJoystick')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetJoystick'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetJoystick'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GameControllerEventState')
    SDL2_API_ARGS_MAP['SDL_GameControllerEventState'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerEventState'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GameControllerUpdate')
    SDL2_API_ARGS_MAP['SDL_GameControllerUpdate'] = None
    SDL2_API_RETVAL_MAP['SDL_GameControllerUpdate'] = None

    SDL2_API_NAMES.append('SDL_GameControllerGetAxisFromString')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetAxisFromString'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetAxisFromString'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GameControllerGetStringForAxis')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetStringForAxis'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetStringForAxis'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GameControllerGetBindForAxis')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetBindForAxis'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetBindForAxis'] = None

    SDL2_API_NAMES.append('SDL_GameControllerGetAxis')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetAxis'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetAxis'] = ctypes.c_short

    SDL2_API_NAMES.append('SDL_GameControllerGetButtonFromString')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetButtonFromString'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetButtonFromString'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GameControllerGetStringForButton')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetStringForButton'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetStringForButton'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GameControllerGetBindForButton')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetBindForButton'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetBindForButton'] = None

    SDL2_API_NAMES.append('SDL_GameControllerGetButton')
    SDL2_API_ARGS_MAP['SDL_GameControllerGetButton'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GameControllerGetButton'] = ctypes.c_uint8

    SDL2_API_NAMES.append('SDL_GameControllerClose')
    SDL2_API_ARGS_MAP['SDL_GameControllerClose'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GameControllerClose'] = None


class _SDL_GameControllerButtonBind_value_hat(ctypes.Structure):
    _fields_ = [
        ("hat", ctypes.c_int),
        ("hat_mask", ctypes.c_int),
    ]

class _SDL_GameControllerButtonBind_value(ctypes.Union):
    _fields_ = [
        ("button", ctypes.c_int),
        ("axis", ctypes.c_int),
        ("hat", _SDL_GameControllerButtonBind_value_hat),
    ]

class SDL_GameControllerButtonBind(ctypes.Structure):
    _fields_ = [
        ("bindType", ctypes.c_int),
        ("value", _SDL_GameControllerButtonBind_value),
    ]

