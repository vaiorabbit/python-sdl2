# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro
SDL_AUDIO_MASK_BITSIZE = 0xFF
SDL_AUDIO_MASK_DATATYPE = ( 1 << 8 )
SDL_AUDIO_MASK_ENDIAN = ( 1 << 12 )
SDL_AUDIO_MASK_SIGNED = ( 1 << 15 )
SDL_AUDIO_ALLOW_FREQUENCY_CHANGE = 0x00000001
SDL_AUDIO_ALLOW_FORMAT_CHANGE = 0x00000002
SDL_AUDIO_ALLOW_CHANNELS_CHANGE = 0x00000004
SDL_AUDIO_ALLOW_ANY_CHANGE = ( SDL_AUDIO_ALLOW_FREQUENCY_CHANGE | SDL_AUDIO_ALLOW_FORMAT_CHANGE | SDL_AUDIO_ALLOW_CHANNELS_CHANGE )
SDL_AUDIOCVT_MAX_FILTERS = 9
SDL_MIX_MAXVOLUME = 128

# Enum
SDL_AUDIO_STOPPED = 0
SDL_AUDIO_PLAYING = 1
SDL_AUDIO_PAUSED = 2

# Typedef
SDL_AudioFormat = ctypes.c_ushort
SDL_AudioCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int)
SDL_AudioFilter = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_ushort)
SDL_AudioDeviceID = ctypes.c_uint
SDL_AudioStatus = ctypes.c_int

# Struct

class SDL_AudioSpec(ctypes.Structure):
    _fields_ = [
        ("freq", ctypes.c_int),
        ("format", ctypes.c_ushort),
        ("channels", ctypes.c_uint8),
        ("silence", ctypes.c_uint8),
        ("samples", ctypes.c_ushort),
        ("padding", ctypes.c_ushort),
        ("size", ctypes.c_uint),
        ("callback", ctypes.c_void_p),
        ("userdata", ctypes.c_void_p),
    ]

class SDL_AudioCVT(ctypes.Structure):
    _fields_ = [
        ("needed", ctypes.c_int),
        ("src_format", ctypes.c_ushort),
        ("dst_format", ctypes.c_ushort),
        ("rate_incr", ctypes.c_double),
        ("buf", ctypes.c_void_p),
        ("len", ctypes.c_int),
        ("len_cvt", ctypes.c_int),
        ("len_mult", ctypes.c_int),
        ("len_ratio", ctypes.c_double),
        ("filters", ctypes.c_void_p * 10),
        ("filter_index", ctypes.c_int),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetNumAudioDrivers')
    SDL2_API_ARGS_MAP['SDL_GetNumAudioDrivers'] = None
    SDL2_API_RETVAL_MAP['SDL_GetNumAudioDrivers'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetAudioDriver')
    SDL2_API_ARGS_MAP['SDL_GetAudioDriver'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetAudioDriver'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_AudioInit')
    SDL2_API_ARGS_MAP['SDL_AudioInit'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_AudioInit'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_AudioQuit')
    SDL2_API_ARGS_MAP['SDL_AudioQuit'] = None
    SDL2_API_RETVAL_MAP['SDL_AudioQuit'] = None

    SDL2_API_NAMES.append('SDL_GetCurrentAudioDriver')
    SDL2_API_ARGS_MAP['SDL_GetCurrentAudioDriver'] = None
    SDL2_API_RETVAL_MAP['SDL_GetCurrentAudioDriver'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_OpenAudio')
    SDL2_API_ARGS_MAP['SDL_OpenAudio'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_OpenAudio'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetNumAudioDevices')
    SDL2_API_ARGS_MAP['SDL_GetNumAudioDevices'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetNumAudioDevices'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetAudioDeviceName')
    SDL2_API_ARGS_MAP['SDL_GetAudioDeviceName'] = [ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetAudioDeviceName'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_OpenAudioDevice')
    SDL2_API_ARGS_MAP['SDL_OpenAudioDevice'] = [ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_OpenAudioDevice'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_GetAudioStatus')
    SDL2_API_ARGS_MAP['SDL_GetAudioStatus'] = None
    SDL2_API_RETVAL_MAP['SDL_GetAudioStatus'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetAudioDeviceStatus')
    SDL2_API_ARGS_MAP['SDL_GetAudioDeviceStatus'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_GetAudioDeviceStatus'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_PauseAudio')
    SDL2_API_ARGS_MAP['SDL_PauseAudio'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_PauseAudio'] = None

    SDL2_API_NAMES.append('SDL_PauseAudioDevice')
    SDL2_API_ARGS_MAP['SDL_PauseAudioDevice'] = [ctypes.c_uint, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_PauseAudioDevice'] = None

    SDL2_API_NAMES.append('SDL_LoadWAV_RW')
    SDL2_API_ARGS_MAP['SDL_LoadWAV_RW'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_LoadWAV_RW'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_FreeWAV')
    SDL2_API_ARGS_MAP['SDL_FreeWAV'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_FreeWAV'] = None

    SDL2_API_NAMES.append('SDL_BuildAudioCVT')
    SDL2_API_ARGS_MAP['SDL_BuildAudioCVT'] = [ctypes.c_void_p, ctypes.c_ushort, ctypes.c_uint8, ctypes.c_int, ctypes.c_ushort, ctypes.c_uint8, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_BuildAudioCVT'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_ConvertAudio')
    SDL2_API_ARGS_MAP['SDL_ConvertAudio'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ConvertAudio'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_NewAudioStream')
    SDL2_API_ARGS_MAP['SDL_NewAudioStream'] = [ctypes.c_ushort, ctypes.c_uint8, ctypes.c_int, ctypes.c_ushort, ctypes.c_uint8, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_NewAudioStream'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_AudioStreamPut')
    SDL2_API_ARGS_MAP['SDL_AudioStreamPut'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_AudioStreamPut'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_AudioStreamGet')
    SDL2_API_ARGS_MAP['SDL_AudioStreamGet'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_AudioStreamGet'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_AudioStreamAvailable')
    SDL2_API_ARGS_MAP['SDL_AudioStreamAvailable'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_AudioStreamAvailable'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_AudioStreamFlush')
    SDL2_API_ARGS_MAP['SDL_AudioStreamFlush'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_AudioStreamFlush'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_AudioStreamClear')
    SDL2_API_ARGS_MAP['SDL_AudioStreamClear'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_AudioStreamClear'] = None

    SDL2_API_NAMES.append('SDL_FreeAudioStream')
    SDL2_API_ARGS_MAP['SDL_FreeAudioStream'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_FreeAudioStream'] = None

    SDL2_API_NAMES.append('SDL_MixAudio')
    SDL2_API_ARGS_MAP['SDL_MixAudio'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_MixAudio'] = None

    SDL2_API_NAMES.append('SDL_MixAudioFormat')
    SDL2_API_ARGS_MAP['SDL_MixAudioFormat'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ushort, ctypes.c_uint, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_MixAudioFormat'] = None

    SDL2_API_NAMES.append('SDL_QueueAudio')
    SDL2_API_ARGS_MAP['SDL_QueueAudio'] = [ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_QueueAudio'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_DequeueAudio')
    SDL2_API_ARGS_MAP['SDL_DequeueAudio'] = [ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_DequeueAudio'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_GetQueuedAudioSize')
    SDL2_API_ARGS_MAP['SDL_GetQueuedAudioSize'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_GetQueuedAudioSize'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_ClearQueuedAudio')
    SDL2_API_ARGS_MAP['SDL_ClearQueuedAudio'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_ClearQueuedAudio'] = None

    SDL2_API_NAMES.append('SDL_LockAudio')
    SDL2_API_ARGS_MAP['SDL_LockAudio'] = None
    SDL2_API_RETVAL_MAP['SDL_LockAudio'] = None

    SDL2_API_NAMES.append('SDL_LockAudioDevice')
    SDL2_API_ARGS_MAP['SDL_LockAudioDevice'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_LockAudioDevice'] = None

    SDL2_API_NAMES.append('SDL_UnlockAudio')
    SDL2_API_ARGS_MAP['SDL_UnlockAudio'] = None
    SDL2_API_RETVAL_MAP['SDL_UnlockAudio'] = None

    SDL2_API_NAMES.append('SDL_UnlockAudioDevice')
    SDL2_API_ARGS_MAP['SDL_UnlockAudioDevice'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_UnlockAudioDevice'] = None

    SDL2_API_NAMES.append('SDL_CloseAudio')
    SDL2_API_ARGS_MAP['SDL_CloseAudio'] = None
    SDL2_API_RETVAL_MAP['SDL_CloseAudio'] = None

    SDL2_API_NAMES.append('SDL_CloseAudioDevice')
    SDL2_API_ARGS_MAP['SDL_CloseAudioDevice'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_CloseAudioDevice'] = None


# TODO : def SDL_LoadWAV

