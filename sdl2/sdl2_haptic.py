# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro
SDL_HAPTIC_CONSTANT = ( 1 << 0 )
SDL_HAPTIC_SINE = ( 1 << 1 )
SDL_HAPTIC_LEFTRIGHT = ( 1 << 2 )
SDL_HAPTIC_TRIANGLE = ( 1 << 3 )
SDL_HAPTIC_SAWTOOTHUP = ( 1 << 4 )
SDL_HAPTIC_SAWTOOTHDOWN = ( 1 << 5 )
SDL_HAPTIC_RAMP = ( 1 << 6 )
SDL_HAPTIC_SPRING = ( 1 << 7 )
SDL_HAPTIC_DAMPER = ( 1 << 8 )
SDL_HAPTIC_INERTIA = ( 1 << 9 )
SDL_HAPTIC_FRICTION = ( 1 << 10 )
SDL_HAPTIC_CUSTOM = ( 1 << 11 )
SDL_HAPTIC_GAIN = ( 1 << 12 )
SDL_HAPTIC_AUTOCENTER = ( 1 << 13 )
SDL_HAPTIC_STATUS = ( 1 << 14 )
SDL_HAPTIC_PAUSE = ( 1 << 15 )
SDL_HAPTIC_POLAR = 0
SDL_HAPTIC_CARTESIAN = 1
SDL_HAPTIC_SPHERICAL = 2
SDL_HAPTIC_INFINITY = 4294967295

# Enum

# Typedef

# Struct

class SDL_HapticDirection(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("dir", ctypes.c_int * 3),
    ]

class SDL_HapticConstant(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ushort),
        ("direction", SDL_HapticDirection),
        ("length", ctypes.c_uint),
        ("delay", ctypes.c_ushort),
        ("button", ctypes.c_ushort),
        ("interval", ctypes.c_ushort),
        ("level", ctypes.c_short),
        ("attack_length", ctypes.c_ushort),
        ("attack_level", ctypes.c_ushort),
        ("fade_length", ctypes.c_ushort),
        ("fade_level", ctypes.c_ushort),
    ]

class SDL_HapticPeriodic(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ushort),
        ("direction", SDL_HapticDirection),
        ("length", ctypes.c_uint),
        ("delay", ctypes.c_ushort),
        ("button", ctypes.c_ushort),
        ("interval", ctypes.c_ushort),
        ("period", ctypes.c_ushort),
        ("magnitude", ctypes.c_short),
        ("offset", ctypes.c_short),
        ("phase", ctypes.c_ushort),
        ("attack_length", ctypes.c_ushort),
        ("attack_level", ctypes.c_ushort),
        ("fade_length", ctypes.c_ushort),
        ("fade_level", ctypes.c_ushort),
    ]

class SDL_HapticCondition(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ushort),
        ("direction", SDL_HapticDirection),
        ("length", ctypes.c_uint),
        ("delay", ctypes.c_ushort),
        ("button", ctypes.c_ushort),
        ("interval", ctypes.c_ushort),
        ("right_sat", ctypes.c_ushort * 3),
        ("left_sat", ctypes.c_ushort * 3),
        ("right_coeff", ctypes.c_short * 3),
        ("left_coeff", ctypes.c_short * 3),
        ("deadband", ctypes.c_ushort * 3),
        ("center", ctypes.c_short * 3),
    ]

class SDL_HapticRamp(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ushort),
        ("direction", SDL_HapticDirection),
        ("length", ctypes.c_uint),
        ("delay", ctypes.c_ushort),
        ("button", ctypes.c_ushort),
        ("interval", ctypes.c_ushort),
        ("start", ctypes.c_short),
        ("end", ctypes.c_short),
        ("attack_length", ctypes.c_ushort),
        ("attack_level", ctypes.c_ushort),
        ("fade_length", ctypes.c_ushort),
        ("fade_level", ctypes.c_ushort),
    ]

class SDL_HapticLeftRight(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ushort),
        ("length", ctypes.c_uint),
        ("large_magnitude", ctypes.c_ushort),
        ("small_magnitude", ctypes.c_ushort),
    ]

class SDL_HapticCustom(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ushort),
        ("direction", SDL_HapticDirection),
        ("length", ctypes.c_uint),
        ("delay", ctypes.c_ushort),
        ("button", ctypes.c_ushort),
        ("interval", ctypes.c_ushort),
        ("channels", ctypes.c_uint8),
        ("period", ctypes.c_ushort),
        ("samples", ctypes.c_ushort),
        ("data", ctypes.c_void_p),
        ("attack_length", ctypes.c_ushort),
        ("attack_level", ctypes.c_ushort),
        ("fade_length", ctypes.c_ushort),
        ("fade_level", ctypes.c_ushort),
    ]

class SDL_HapticEffect(ctypes.Union):
    _fields_ = [
        ("type", ctypes.c_ushort),
        ("constant", SDL_HapticConstant),
        ("periodic", SDL_HapticPeriodic),
        ("condition", SDL_HapticCondition),
        ("ramp", SDL_HapticRamp),
        ("leftright", SDL_HapticLeftRight),
        ("custom", SDL_HapticCustom),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_NumHaptics')
    SDL2_API_ARGS_MAP['SDL_NumHaptics'] = None
    SDL2_API_RETVAL_MAP['SDL_NumHaptics'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticName')
    SDL2_API_ARGS_MAP['SDL_HapticName'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_HapticName'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_HapticOpen')
    SDL2_API_ARGS_MAP['SDL_HapticOpen'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_HapticOpen'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_HapticOpened')
    SDL2_API_ARGS_MAP['SDL_HapticOpened'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_HapticOpened'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticIndex')
    SDL2_API_ARGS_MAP['SDL_HapticIndex'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticIndex'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_MouseIsHaptic')
    SDL2_API_ARGS_MAP['SDL_MouseIsHaptic'] = None
    SDL2_API_RETVAL_MAP['SDL_MouseIsHaptic'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticOpenFromMouse')
    SDL2_API_ARGS_MAP['SDL_HapticOpenFromMouse'] = None
    SDL2_API_RETVAL_MAP['SDL_HapticOpenFromMouse'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_JoystickIsHaptic')
    SDL2_API_ARGS_MAP['SDL_JoystickIsHaptic'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_JoystickIsHaptic'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticOpenFromJoystick')
    SDL2_API_ARGS_MAP['SDL_HapticOpenFromJoystick'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticOpenFromJoystick'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_HapticClose')
    SDL2_API_ARGS_MAP['SDL_HapticClose'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticClose'] = None

    SDL2_API_NAMES.append('SDL_HapticNumEffects')
    SDL2_API_ARGS_MAP['SDL_HapticNumEffects'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticNumEffects'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticNumEffectsPlaying')
    SDL2_API_ARGS_MAP['SDL_HapticNumEffectsPlaying'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticNumEffectsPlaying'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticQuery')
    SDL2_API_ARGS_MAP['SDL_HapticQuery'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticQuery'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_HapticNumAxes')
    SDL2_API_ARGS_MAP['SDL_HapticNumAxes'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticNumAxes'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticEffectSupported')
    SDL2_API_ARGS_MAP['SDL_HapticEffectSupported'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticEffectSupported'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticNewEffect')
    SDL2_API_ARGS_MAP['SDL_HapticNewEffect'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticNewEffect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticUpdateEffect')
    SDL2_API_ARGS_MAP['SDL_HapticUpdateEffect'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticUpdateEffect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticRunEffect')
    SDL2_API_ARGS_MAP['SDL_HapticRunEffect'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_HapticRunEffect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticStopEffect')
    SDL2_API_ARGS_MAP['SDL_HapticStopEffect'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_HapticStopEffect'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticDestroyEffect')
    SDL2_API_ARGS_MAP['SDL_HapticDestroyEffect'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_HapticDestroyEffect'] = None

    SDL2_API_NAMES.append('SDL_HapticGetEffectStatus')
    SDL2_API_ARGS_MAP['SDL_HapticGetEffectStatus'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_HapticGetEffectStatus'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticSetGain')
    SDL2_API_ARGS_MAP['SDL_HapticSetGain'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_HapticSetGain'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticSetAutocenter')
    SDL2_API_ARGS_MAP['SDL_HapticSetAutocenter'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_HapticSetAutocenter'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticPause')
    SDL2_API_ARGS_MAP['SDL_HapticPause'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticPause'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticUnpause')
    SDL2_API_ARGS_MAP['SDL_HapticUnpause'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticUnpause'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticStopAll')
    SDL2_API_ARGS_MAP['SDL_HapticStopAll'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticStopAll'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticRumbleSupported')
    SDL2_API_ARGS_MAP['SDL_HapticRumbleSupported'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticRumbleSupported'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticRumbleInit')
    SDL2_API_ARGS_MAP['SDL_HapticRumbleInit'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticRumbleInit'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticRumblePlay')
    SDL2_API_ARGS_MAP['SDL_HapticRumblePlay'] = [ctypes.c_void_p, ctypes.c_float, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_HapticRumblePlay'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_HapticRumbleStop')
    SDL2_API_ARGS_MAP['SDL_HapticRumbleStop'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HapticRumbleStop'] = ctypes.c_int


