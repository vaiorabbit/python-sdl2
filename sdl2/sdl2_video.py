# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro
SDL_WINDOWPOS_UNDEFINED_MASK = 0x1FFF0000
SDL_WINDOWPOS_CENTERED_MASK = 0x2FFF0000

# Enum
SDL_WINDOW_FULLSCREEN = 1
SDL_WINDOW_OPENGL = 2
SDL_WINDOW_SHOWN = 4
SDL_WINDOW_HIDDEN = 8
SDL_WINDOW_BORDERLESS = 16
SDL_WINDOW_RESIZABLE = 32
SDL_WINDOW_MINIMIZED = 64
SDL_WINDOW_MAXIMIZED = 128
SDL_WINDOW_INPUT_GRABBED = 256
SDL_WINDOW_INPUT_FOCUS = 512
SDL_WINDOW_MOUSE_FOCUS = 1024
SDL_WINDOW_FULLSCREEN_DESKTOP = 4097
SDL_WINDOW_FOREIGN = 2048
SDL_WINDOW_ALLOW_HIGHDPI = 8192
SDL_WINDOW_MOUSE_CAPTURE = 16384
SDL_WINDOW_ALWAYS_ON_TOP = 32768
SDL_WINDOW_SKIP_TASKBAR = 65536
SDL_WINDOW_UTILITY = 131072
SDL_WINDOW_TOOLTIP = 262144
SDL_WINDOW_POPUP_MENU = 524288
SDL_WINDOW_VULKAN = 268435456
SDL_WINDOWEVENT_NONE = 0
SDL_WINDOWEVENT_SHOWN = 1
SDL_WINDOWEVENT_HIDDEN = 2
SDL_WINDOWEVENT_EXPOSED = 3
SDL_WINDOWEVENT_MOVED = 4
SDL_WINDOWEVENT_RESIZED = 5
SDL_WINDOWEVENT_SIZE_CHANGED = 6
SDL_WINDOWEVENT_MINIMIZED = 7
SDL_WINDOWEVENT_MAXIMIZED = 8
SDL_WINDOWEVENT_RESTORED = 9
SDL_WINDOWEVENT_ENTER = 10
SDL_WINDOWEVENT_LEAVE = 11
SDL_WINDOWEVENT_FOCUS_GAINED = 12
SDL_WINDOWEVENT_FOCUS_LOST = 13
SDL_WINDOWEVENT_CLOSE = 14
SDL_WINDOWEVENT_TAKE_FOCUS = 15
SDL_WINDOWEVENT_HIT_TEST = 16
SDL_GL_RED_SIZE = 0
SDL_GL_GREEN_SIZE = 1
SDL_GL_BLUE_SIZE = 2
SDL_GL_ALPHA_SIZE = 3
SDL_GL_BUFFER_SIZE = 4
SDL_GL_DOUBLEBUFFER = 5
SDL_GL_DEPTH_SIZE = 6
SDL_GL_STENCIL_SIZE = 7
SDL_GL_ACCUM_RED_SIZE = 8
SDL_GL_ACCUM_GREEN_SIZE = 9
SDL_GL_ACCUM_BLUE_SIZE = 10
SDL_GL_ACCUM_ALPHA_SIZE = 11
SDL_GL_STEREO = 12
SDL_GL_MULTISAMPLEBUFFERS = 13
SDL_GL_MULTISAMPLESAMPLES = 14
SDL_GL_ACCELERATED_VISUAL = 15
SDL_GL_RETAINED_BACKING = 16
SDL_GL_CONTEXT_MAJOR_VERSION = 17
SDL_GL_CONTEXT_MINOR_VERSION = 18
SDL_GL_CONTEXT_EGL = 19
SDL_GL_CONTEXT_FLAGS = 20
SDL_GL_CONTEXT_PROFILE_MASK = 21
SDL_GL_SHARE_WITH_CURRENT_CONTEXT = 22
SDL_GL_FRAMEBUFFER_SRGB_CAPABLE = 23
SDL_GL_CONTEXT_RELEASE_BEHAVIOR = 24
SDL_GL_CONTEXT_RESET_NOTIFICATION = 25
SDL_GL_CONTEXT_NO_ERROR = 26
SDL_GL_CONTEXT_PROFILE_CORE = 1
SDL_GL_CONTEXT_PROFILE_COMPATIBILITY = 2
SDL_GL_CONTEXT_PROFILE_ES = 4
SDL_GL_CONTEXT_DEBUG_FLAG = 1
SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG = 2
SDL_GL_CONTEXT_ROBUST_ACCESS_FLAG = 4
SDL_GL_CONTEXT_RESET_ISOLATION_FLAG = 8
SDL_GL_CONTEXT_RELEASE_BEHAVIOR_NONE = 0
SDL_GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH = 1
SDL_GL_CONTEXT_RESET_NO_NOTIFICATION = 0
SDL_GL_CONTEXT_RESET_LOSE_CONTEXT = 1
SDL_HITTEST_NORMAL = 0
SDL_HITTEST_DRAGGABLE = 1
SDL_HITTEST_RESIZE_TOPLEFT = 2
SDL_HITTEST_RESIZE_TOP = 3
SDL_HITTEST_RESIZE_TOPRIGHT = 4
SDL_HITTEST_RESIZE_RIGHT = 5
SDL_HITTEST_RESIZE_BOTTOMRIGHT = 6
SDL_HITTEST_RESIZE_BOTTOM = 7
SDL_HITTEST_RESIZE_BOTTOMLEFT = 8
SDL_HITTEST_RESIZE_LEFT = 9

# Typedef
SDL_WindowFlags = ctypes.c_int
SDL_WindowEventID = ctypes.c_int
SDL_GLContext = ctypes.c_void_p
SDL_GLattr = ctypes.c_int
SDL_GLprofile = ctypes.c_int
SDL_GLcontextFlag = ctypes.c_int
SDL_GLcontextReleaseFlag = ctypes.c_int
SDL_GLContextResetNotification = ctypes.c_int
SDL_HitTestResult = ctypes.c_int
SDL_HitTest = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

# Struct

class SDL_DisplayMode(ctypes.Structure):
    _fields_ = [
        ("format", ctypes.c_uint),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("refresh_rate", ctypes.c_int),
        ("driverdata", ctypes.c_void_p),
    ]

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_GetNumVideoDrivers')
    SDL2_API_ARGS_MAP['SDL_GetNumVideoDrivers'] = None
    SDL2_API_RETVAL_MAP['SDL_GetNumVideoDrivers'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetVideoDriver')
    SDL2_API_ARGS_MAP['SDL_GetVideoDriver'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetVideoDriver'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_VideoInit')
    SDL2_API_ARGS_MAP['SDL_VideoInit'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_VideoInit'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_VideoQuit')
    SDL2_API_ARGS_MAP['SDL_VideoQuit'] = None
    SDL2_API_RETVAL_MAP['SDL_VideoQuit'] = None

    SDL2_API_NAMES.append('SDL_GetCurrentVideoDriver')
    SDL2_API_ARGS_MAP['SDL_GetCurrentVideoDriver'] = None
    SDL2_API_RETVAL_MAP['SDL_GetCurrentVideoDriver'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GetNumVideoDisplays')
    SDL2_API_ARGS_MAP['SDL_GetNumVideoDisplays'] = None
    SDL2_API_RETVAL_MAP['SDL_GetNumVideoDisplays'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetDisplayName')
    SDL2_API_ARGS_MAP['SDL_GetDisplayName'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetDisplayName'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_GetDisplayBounds')
    SDL2_API_ARGS_MAP['SDL_GetDisplayBounds'] = [ctypes.c_int, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetDisplayBounds'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetDisplayDPI')
    SDL2_API_ARGS_MAP['SDL_GetDisplayDPI'] = [ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetDisplayDPI'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetDisplayUsableBounds')
    SDL2_API_ARGS_MAP['SDL_GetDisplayUsableBounds'] = [ctypes.c_int, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetDisplayUsableBounds'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetNumDisplayModes')
    SDL2_API_ARGS_MAP['SDL_GetNumDisplayModes'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GetNumDisplayModes'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetDisplayMode')
    SDL2_API_ARGS_MAP['SDL_GetDisplayMode'] = [ctypes.c_int, ctypes.c_int, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetDisplayMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetDesktopDisplayMode')
    SDL2_API_ARGS_MAP['SDL_GetDesktopDisplayMode'] = [ctypes.c_int, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetDesktopDisplayMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetCurrentDisplayMode')
    SDL2_API_ARGS_MAP['SDL_GetCurrentDisplayMode'] = [ctypes.c_int, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetCurrentDisplayMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetClosestDisplayMode')
    SDL2_API_ARGS_MAP['SDL_GetClosestDisplayMode'] = [ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetClosestDisplayMode'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GetWindowDisplayIndex')
    SDL2_API_ARGS_MAP['SDL_GetWindowDisplayIndex'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowDisplayIndex'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetWindowDisplayMode')
    SDL2_API_ARGS_MAP['SDL_SetWindowDisplayMode'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetWindowDisplayMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetWindowDisplayMode')
    SDL2_API_ARGS_MAP['SDL_GetWindowDisplayMode'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowDisplayMode'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetWindowPixelFormat')
    SDL2_API_ARGS_MAP['SDL_GetWindowPixelFormat'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowPixelFormat'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_CreateWindow')
    SDL2_API_ARGS_MAP['SDL_CreateWindow'] = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_CreateWindow'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_CreateWindowFrom')
    SDL2_API_ARGS_MAP['SDL_CreateWindowFrom'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_CreateWindowFrom'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GetWindowID')
    SDL2_API_ARGS_MAP['SDL_GetWindowID'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowID'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_GetWindowFromID')
    SDL2_API_ARGS_MAP['SDL_GetWindowFromID'] = [ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_GetWindowFromID'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GetWindowFlags')
    SDL2_API_ARGS_MAP['SDL_GetWindowFlags'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowFlags'] = ctypes.c_uint

    SDL2_API_NAMES.append('SDL_SetWindowTitle')
    SDL2_API_ARGS_MAP['SDL_SetWindowTitle'] = [ctypes.c_void_p, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_SetWindowTitle'] = None

    SDL2_API_NAMES.append('SDL_GetWindowTitle')
    SDL2_API_ARGS_MAP['SDL_GetWindowTitle'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowTitle'] = ctypes.c_char_p

    SDL2_API_NAMES.append('SDL_SetWindowIcon')
    SDL2_API_ARGS_MAP['SDL_SetWindowIcon'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetWindowIcon'] = None

    SDL2_API_NAMES.append('SDL_SetWindowData')
    SDL2_API_ARGS_MAP['SDL_SetWindowData'] = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetWindowData'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GetWindowData')
    SDL2_API_ARGS_MAP['SDL_GetWindowData'] = [ctypes.c_void_p, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowData'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_SetWindowPosition')
    SDL2_API_ARGS_MAP['SDL_SetWindowPosition'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetWindowPosition'] = None

    SDL2_API_NAMES.append('SDL_GetWindowPosition')
    SDL2_API_ARGS_MAP['SDL_GetWindowPosition'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowPosition'] = None

    SDL2_API_NAMES.append('SDL_SetWindowSize')
    SDL2_API_ARGS_MAP['SDL_SetWindowSize'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetWindowSize'] = None

    SDL2_API_NAMES.append('SDL_GetWindowSize')
    SDL2_API_ARGS_MAP['SDL_GetWindowSize'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowSize'] = None

    SDL2_API_NAMES.append('SDL_GetWindowBordersSize')
    SDL2_API_ARGS_MAP['SDL_GetWindowBordersSize'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowBordersSize'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetWindowMinimumSize')
    SDL2_API_ARGS_MAP['SDL_SetWindowMinimumSize'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetWindowMinimumSize'] = None

    SDL2_API_NAMES.append('SDL_GetWindowMinimumSize')
    SDL2_API_ARGS_MAP['SDL_GetWindowMinimumSize'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowMinimumSize'] = None

    SDL2_API_NAMES.append('SDL_SetWindowMaximumSize')
    SDL2_API_ARGS_MAP['SDL_SetWindowMaximumSize'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetWindowMaximumSize'] = None

    SDL2_API_NAMES.append('SDL_GetWindowMaximumSize')
    SDL2_API_ARGS_MAP['SDL_GetWindowMaximumSize'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowMaximumSize'] = None

    SDL2_API_NAMES.append('SDL_SetWindowBordered')
    SDL2_API_ARGS_MAP['SDL_SetWindowBordered'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetWindowBordered'] = None

    SDL2_API_NAMES.append('SDL_SetWindowResizable')
    SDL2_API_ARGS_MAP['SDL_SetWindowResizable'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetWindowResizable'] = None

    SDL2_API_NAMES.append('SDL_ShowWindow')
    SDL2_API_ARGS_MAP['SDL_ShowWindow'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_ShowWindow'] = None

    SDL2_API_NAMES.append('SDL_HideWindow')
    SDL2_API_ARGS_MAP['SDL_HideWindow'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_HideWindow'] = None

    SDL2_API_NAMES.append('SDL_RaiseWindow')
    SDL2_API_ARGS_MAP['SDL_RaiseWindow'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RaiseWindow'] = None

    SDL2_API_NAMES.append('SDL_MaximizeWindow')
    SDL2_API_ARGS_MAP['SDL_MaximizeWindow'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_MaximizeWindow'] = None

    SDL2_API_NAMES.append('SDL_MinimizeWindow')
    SDL2_API_ARGS_MAP['SDL_MinimizeWindow'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_MinimizeWindow'] = None

    SDL2_API_NAMES.append('SDL_RestoreWindow')
    SDL2_API_ARGS_MAP['SDL_RestoreWindow'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_RestoreWindow'] = None

    SDL2_API_NAMES.append('SDL_SetWindowFullscreen')
    SDL2_API_ARGS_MAP['SDL_SetWindowFullscreen'] = [ctypes.c_void_p, ctypes.c_uint]
    SDL2_API_RETVAL_MAP['SDL_SetWindowFullscreen'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetWindowSurface')
    SDL2_API_ARGS_MAP['SDL_GetWindowSurface'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowSurface'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_UpdateWindowSurface')
    SDL2_API_ARGS_MAP['SDL_UpdateWindowSurface'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_UpdateWindowSurface'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_UpdateWindowSurfaceRects')
    SDL2_API_ARGS_MAP['SDL_UpdateWindowSurfaceRects'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_UpdateWindowSurfaceRects'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetWindowGrab')
    SDL2_API_ARGS_MAP['SDL_SetWindowGrab'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_SetWindowGrab'] = None

    SDL2_API_NAMES.append('SDL_GetWindowGrab')
    SDL2_API_ARGS_MAP['SDL_GetWindowGrab'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowGrab'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetGrabbedWindow')
    SDL2_API_ARGS_MAP['SDL_GetGrabbedWindow'] = None
    SDL2_API_RETVAL_MAP['SDL_GetGrabbedWindow'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_SetWindowBrightness')
    SDL2_API_ARGS_MAP['SDL_SetWindowBrightness'] = [ctypes.c_void_p, ctypes.c_float]
    SDL2_API_RETVAL_MAP['SDL_SetWindowBrightness'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetWindowBrightness')
    SDL2_API_ARGS_MAP['SDL_GetWindowBrightness'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowBrightness'] = ctypes.c_float

    SDL2_API_NAMES.append('SDL_SetWindowOpacity')
    SDL2_API_ARGS_MAP['SDL_SetWindowOpacity'] = [ctypes.c_void_p, ctypes.c_float]
    SDL2_API_RETVAL_MAP['SDL_SetWindowOpacity'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetWindowOpacity')
    SDL2_API_ARGS_MAP['SDL_GetWindowOpacity'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowOpacity'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetWindowModalFor')
    SDL2_API_ARGS_MAP['SDL_SetWindowModalFor'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetWindowModalFor'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetWindowInputFocus')
    SDL2_API_ARGS_MAP['SDL_SetWindowInputFocus'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetWindowInputFocus'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetWindowGammaRamp')
    SDL2_API_ARGS_MAP['SDL_SetWindowGammaRamp'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetWindowGammaRamp'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GetWindowGammaRamp')
    SDL2_API_ARGS_MAP['SDL_GetWindowGammaRamp'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GetWindowGammaRamp'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_SetWindowHitTest')
    SDL2_API_ARGS_MAP['SDL_SetWindowHitTest'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_SetWindowHitTest'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_DestroyWindow')
    SDL2_API_ARGS_MAP['SDL_DestroyWindow'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_DestroyWindow'] = None

    SDL2_API_NAMES.append('SDL_IsScreenSaverEnabled')
    SDL2_API_ARGS_MAP['SDL_IsScreenSaverEnabled'] = None
    SDL2_API_RETVAL_MAP['SDL_IsScreenSaverEnabled'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_EnableScreenSaver')
    SDL2_API_ARGS_MAP['SDL_EnableScreenSaver'] = None
    SDL2_API_RETVAL_MAP['SDL_EnableScreenSaver'] = None

    SDL2_API_NAMES.append('SDL_DisableScreenSaver')
    SDL2_API_ARGS_MAP['SDL_DisableScreenSaver'] = None
    SDL2_API_RETVAL_MAP['SDL_DisableScreenSaver'] = None

    SDL2_API_NAMES.append('SDL_GL_LoadLibrary')
    SDL2_API_ARGS_MAP['SDL_GL_LoadLibrary'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GL_LoadLibrary'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GL_GetProcAddress')
    SDL2_API_ARGS_MAP['SDL_GL_GetProcAddress'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GL_GetProcAddress'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GL_UnloadLibrary')
    SDL2_API_ARGS_MAP['SDL_GL_UnloadLibrary'] = None
    SDL2_API_RETVAL_MAP['SDL_GL_UnloadLibrary'] = None

    SDL2_API_NAMES.append('SDL_GL_ExtensionSupported')
    SDL2_API_ARGS_MAP['SDL_GL_ExtensionSupported'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_GL_ExtensionSupported'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GL_ResetAttributes')
    SDL2_API_ARGS_MAP['SDL_GL_ResetAttributes'] = None
    SDL2_API_RETVAL_MAP['SDL_GL_ResetAttributes'] = None

    SDL2_API_NAMES.append('SDL_GL_SetAttribute')
    SDL2_API_ARGS_MAP['SDL_GL_SetAttribute'] = [ctypes.c_int, ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GL_SetAttribute'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GL_GetAttribute')
    SDL2_API_ARGS_MAP['SDL_GL_GetAttribute'] = [ctypes.c_int, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GL_GetAttribute'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GL_CreateContext')
    SDL2_API_ARGS_MAP['SDL_GL_CreateContext'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GL_CreateContext'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GL_MakeCurrent')
    SDL2_API_ARGS_MAP['SDL_GL_MakeCurrent'] = [ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GL_MakeCurrent'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GL_GetCurrentWindow')
    SDL2_API_ARGS_MAP['SDL_GL_GetCurrentWindow'] = None
    SDL2_API_RETVAL_MAP['SDL_GL_GetCurrentWindow'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GL_GetCurrentContext')
    SDL2_API_ARGS_MAP['SDL_GL_GetCurrentContext'] = None
    SDL2_API_RETVAL_MAP['SDL_GL_GetCurrentContext'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_GL_GetDrawableSize')
    SDL2_API_ARGS_MAP['SDL_GL_GetDrawableSize'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GL_GetDrawableSize'] = None

    SDL2_API_NAMES.append('SDL_GL_SetSwapInterval')
    SDL2_API_ARGS_MAP['SDL_GL_SetSwapInterval'] = [ctypes.c_int]
    SDL2_API_RETVAL_MAP['SDL_GL_SetSwapInterval'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GL_GetSwapInterval')
    SDL2_API_ARGS_MAP['SDL_GL_GetSwapInterval'] = None
    SDL2_API_RETVAL_MAP['SDL_GL_GetSwapInterval'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_GL_SwapWindow')
    SDL2_API_ARGS_MAP['SDL_GL_SwapWindow'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GL_SwapWindow'] = None

    SDL2_API_NAMES.append('SDL_GL_DeleteContext')
    SDL2_API_ARGS_MAP['SDL_GL_DeleteContext'] = [ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_GL_DeleteContext'] = None


