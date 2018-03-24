# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro
SDL_JOYSTICK_AXIS_MAX = 32767
SDL_JOYSTICK_AXIS_MIN = -32768
SDL_HAT_CENTERED = 0x00
SDL_HAT_UP = 0x01
SDL_HAT_RIGHT = 0x02
SDL_HAT_DOWN = 0x04
SDL_HAT_LEFT = 0x08
SDL_HAT_RIGHTUP = ( SDL_HAT_RIGHT | SDL_HAT_UP )
SDL_HAT_RIGHTDOWN = ( SDL_HAT_RIGHT | SDL_HAT_DOWN )
SDL_HAT_LEFTUP = ( SDL_HAT_LEFT | SDL_HAT_UP )
SDL_HAT_LEFTDOWN = ( SDL_HAT_LEFT | SDL_HAT_DOWN )

# Enum
SDL_JOYSTICK_TYPE_UNKNOWN = 0
SDL_JOYSTICK_TYPE_GAMECONTROLLER = 1
SDL_JOYSTICK_TYPE_WHEEL = 2
SDL_JOYSTICK_TYPE_ARCADE_STICK = 3
SDL_JOYSTICK_TYPE_FLIGHT_STICK = 4
SDL_JOYSTICK_TYPE_DANCE_PAD = 5
SDL_JOYSTICK_TYPE_GUITAR = 6
SDL_JOYSTICK_TYPE_DRUM_KIT = 7
SDL_JOYSTICK_TYPE_ARCADE_PAD = 8
SDL_JOYSTICK_TYPE_THROTTLE = 9
SDL_JOYSTICK_POWER_UNKNOWN = -1
SDL_JOYSTICK_POWER_EMPTY = 0
SDL_JOYSTICK_POWER_LOW = 1
SDL_JOYSTICK_POWER_MEDIUM = 2
SDL_JOYSTICK_POWER_FULL = 3
SDL_JOYSTICK_POWER_WIRED = 4
SDL_JOYSTICK_POWER_MAX = 5

# Typedef
SDL_JoystickID = ctypes.c_int
SDL_JoystickType = ctypes.c_int
SDL_JoystickPowerLevel = ctypes.c_int

# Struct

class SDL_JoystickGUID(ctypes.Structure):
    _fields_ = [
        ("data", ctypes.c_uint8 * 16),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_LockJoysticks')
    SDL2_API_ARGS_MAP['SDL_LockJoysticks'] = None
    SDL2_API_RETVAL_MAP['SDL_LockJoysticks'] = None

    SDL2_API_NAMES.append('SDL_UnlockJoysticks')
    SDL2_API_ARGS_MAP['SDL_UnlockJoysticks'] = None
    SDL2_API_RETVAL_MAP['SDL_UnlockJoysticks'] = None

    SDL2_API_NAMES.append('SDL_NumJoysticks')
    SDL2_API_ARGS_MAP['SDL_NumJoysticks'] = None
    SDL2_API_RETVAL_MAP['SDL_NumJoysticks'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickNameForIndex')
    SDL2_API_ARGS_MAP['SDL_JoystickNameForIndex'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickNameForIndex'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_JoystickGetDeviceGUID')
    SDL2_API_ARGS_MAP['SDL_JoystickGetDeviceGUID'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetDeviceGUID'] = None

    SDL2_API_NAMES.append('SDL_JoystickGetDeviceVendor')
    SDL2_API_ARGS_MAP['SDL_JoystickGetDeviceVendor'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetDeviceVendor'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_JoystickGetDeviceProduct')
    SDL2_API_ARGS_MAP['SDL_JoystickGetDeviceProduct'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetDeviceProduct'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_JoystickGetDeviceProductVersion')
    SDL2_API_ARGS_MAP['SDL_JoystickGetDeviceProductVersion'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetDeviceProductVersion'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_JoystickGetDeviceType')
    SDL2_API_ARGS_MAP['SDL_JoystickGetDeviceType'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetDeviceType'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickGetDeviceInstanceID')
    SDL2_API_ARGS_MAP['SDL_JoystickGetDeviceInstanceID'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetDeviceInstanceID'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickOpen')
    SDL2_API_ARGS_MAP['SDL_JoystickOpen'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickOpen'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_JoystickFromInstanceID')
    SDL2_API_ARGS_MAP['SDL_JoystickFromInstanceID'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickFromInstanceID'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_JoystickName')
    SDL2_API_ARGS_MAP['SDL_JoystickName'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickName'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_JoystickGetGUID')
    SDL2_API_ARGS_MAP['SDL_JoystickGetGUID'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetGUID'] = None

    SDL2_API_NAMES.append('SDL_JoystickGetVendor')
    SDL2_API_ARGS_MAP['SDL_JoystickGetVendor'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetVendor'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_JoystickGetProduct')
    SDL2_API_ARGS_MAP['SDL_JoystickGetProduct'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetProduct'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_JoystickGetProductVersion')
    SDL2_API_ARGS_MAP['SDL_JoystickGetProductVersion'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetProductVersion'] = ctypes.c_ushort

    SDL2_API_NAMES.append('SDL_JoystickGetType')
    SDL2_API_ARGS_MAP['SDL_JoystickGetType'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetType'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickGetGUIDString')
    SDL2_API_ARGS_MAP['SDL_JoystickGetGUIDString'] = [SDL_JoystickGUID, ctypes.c_char_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetGUIDString'] = None

    SDL2_API_NAMES.append('SDL_JoystickGetGUIDFromString')
    SDL2_API_ARGS_MAP['SDL_JoystickGetGUIDFromString'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetGUIDFromString'] = None

    SDL2_API_NAMES.append('SDL_JoystickGetAttached')
    SDL2_API_ARGS_MAP['SDL_JoystickGetAttached'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetAttached'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickInstanceID')
    SDL2_API_ARGS_MAP['SDL_JoystickInstanceID'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickInstanceID'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickNumAxes')
    SDL2_API_ARGS_MAP['SDL_JoystickNumAxes'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickNumAxes'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickNumBalls')
    SDL2_API_ARGS_MAP['SDL_JoystickNumBalls'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickNumBalls'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickNumHats')
    SDL2_API_ARGS_MAP['SDL_JoystickNumHats'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickNumHats'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickNumButtons')
    SDL2_API_ARGS_MAP['SDL_JoystickNumButtons'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickNumButtons'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickUpdate')
    SDL2_API_ARGS_MAP['SDL_JoystickUpdate'] = None
    SDL2_API_RETVAL_MAP['SDL_JoystickUpdate'] = None

    SDL2_API_NAMES.append('SDL_JoystickEventState')
    SDL2_API_ARGS_MAP['SDL_JoystickEventState'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickEventState'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickGetAxis')
    SDL2_API_ARGS_MAP['SDL_JoystickGetAxis'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetAxis'] = ctypes.c_short

    SDL2_API_NAMES.append('SDL_JoystickGetAxisInitialState')
    SDL2_API_ARGS_MAP['SDL_JoystickGetAxisInitialState'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetAxisInitialState'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickGetHat')
    SDL2_API_ARGS_MAP['SDL_JoystickGetHat'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetHat'] = ctypes.c_uint8

    SDL2_API_NAMES.append('SDL_JoystickGetBall')
    SDL2_API_ARGS_MAP['SDL_JoystickGetBall'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetBall'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_JoystickGetButton')
    SDL2_API_ARGS_MAP['SDL_JoystickGetButton'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_JoystickGetButton'] = ctypes.c_uint8

    SDL2_API_NAMES.append('SDL_JoystickClose')
    SDL2_API_ARGS_MAP['SDL_JoystickClose'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickClose'] = None

    SDL2_API_NAMES.append('SDL_JoystickCurrentPowerLevel')
    SDL2_API_ARGS_MAP['SDL_JoystickCurrentPowerLevel'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickCurrentPowerLevel'] = ctypes.c_int


