# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro
SDL_MAX_LOG_MESSAGE = 4096

# Enum
SDL_LOG_CATEGORY_APPLICATION = 0
SDL_LOG_CATEGORY_ERROR = 1
SDL_LOG_CATEGORY_ASSERT = 2
SDL_LOG_CATEGORY_SYSTEM = 3
SDL_LOG_CATEGORY_AUDIO = 4
SDL_LOG_CATEGORY_VIDEO = 5
SDL_LOG_CATEGORY_RENDER = 6
SDL_LOG_CATEGORY_INPUT = 7
SDL_LOG_CATEGORY_TEST = 8
SDL_LOG_CATEGORY_RESERVED1 = 9
SDL_LOG_CATEGORY_RESERVED2 = 10
SDL_LOG_CATEGORY_RESERVED3 = 11
SDL_LOG_CATEGORY_RESERVED4 = 12
SDL_LOG_CATEGORY_RESERVED5 = 13
SDL_LOG_CATEGORY_RESERVED6 = 14
SDL_LOG_CATEGORY_RESERVED7 = 15
SDL_LOG_CATEGORY_RESERVED8 = 16
SDL_LOG_CATEGORY_RESERVED9 = 17
SDL_LOG_CATEGORY_RESERVED10 = 18
SDL_LOG_CATEGORY_CUSTOM = 19
SDL_LOG_PRIORITY_VERBOSE = 1
SDL_LOG_PRIORITY_DEBUG = 2
SDL_LOG_PRIORITY_INFO = 3
SDL_LOG_PRIORITY_WARN = 4
SDL_LOG_PRIORITY_ERROR = 5
SDL_LOG_PRIORITY_CRITICAL = 6
SDL_NUM_LOG_PRIORITIES = 7

# Typedef
SDL_LogPriority = ctypes.c_int
SDL_LogOutputFunction = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_LogSetAllPriority')
    SDL2_API_ARGS_MAP['SDL_LogSetAllPriority'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_LogSetAllPriority'] = None

    SDL2_API_NAMES.append('SDL_LogSetPriority')
    SDL2_API_ARGS_MAP['SDL_LogSetPriority'] = [ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_LogSetPriority'] = None

    SDL2_API_NAMES.append('SDL_LogGetPriority')
    SDL2_API_ARGS_MAP['SDL_LogGetPriority'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_LogGetPriority'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_LogResetPriorities')
    SDL2_API_ARGS_MAP['SDL_LogResetPriorities'] = None
    SDL2_API_RETVAL_MAP['SDL_LogResetPriorities'] = None

    SDL2_API_NAMES.append('SDL_Log')
    SDL2_API_ARGS_MAP['SDL_Log'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_Log'] = None

    SDL2_API_NAMES.append('SDL_LogVerbose')
    SDL2_API_ARGS_MAP['SDL_LogVerbose'] = [ctypes.c_int, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_LogVerbose'] = None

    SDL2_API_NAMES.append('SDL_LogDebug')
    SDL2_API_ARGS_MAP['SDL_LogDebug'] = [ctypes.c_int, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_LogDebug'] = None

    SDL2_API_NAMES.append('SDL_LogInfo')
    SDL2_API_ARGS_MAP['SDL_LogInfo'] = [ctypes.c_int, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_LogInfo'] = None

    SDL2_API_NAMES.append('SDL_LogWarn')
    SDL2_API_ARGS_MAP['SDL_LogWarn'] = [ctypes.c_int, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_LogWarn'] = None

    SDL2_API_NAMES.append('SDL_LogError')
    SDL2_API_ARGS_MAP['SDL_LogError'] = [ctypes.c_int, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_LogError'] = None

    SDL2_API_NAMES.append('SDL_LogCritical')
    SDL2_API_ARGS_MAP['SDL_LogCritical'] = [ctypes.c_int, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_LogCritical'] = None

    SDL2_API_NAMES.append('SDL_LogMessage')
    SDL2_API_ARGS_MAP['SDL_LogMessage'] = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_LogMessage'] = None

    SDL2_API_NAMES.append('SDL_LogGetOutputFunction')
    SDL2_API_ARGS_MAP['SDL_LogGetOutputFunction'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_LogGetOutputFunction'] = None

    SDL2_API_NAMES.append('SDL_LogSetOutputFunction')
    SDL2_API_ARGS_MAP['SDL_LogSetOutputFunction'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_LogSetOutputFunction'] = None


