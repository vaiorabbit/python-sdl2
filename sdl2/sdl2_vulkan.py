# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP

# Define/Macro

# Enum

# Typedef
VkInstance = ctypes.c_void_p
VkSurfaceKHR = ctypes.c_void_p
SDL_vulkanInstance = ctypes.c_void_p
SDL_vulkanSurface = ctypes.c_void_p

# Struct

# Function
def setup_symbols():
    SDL2_API_NAMES.append('SDL_Vulkan_LoadLibrary')
    SDL2_API_ARGS_MAP['SDL_Vulkan_LoadLibrary'] = [ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_Vulkan_LoadLibrary'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_Vulkan_GetVkGetInstanceProcAddr')
    SDL2_API_ARGS_MAP['SDL_Vulkan_GetVkGetInstanceProcAddr'] = None
    SDL2_API_RETVAL_MAP['SDL_Vulkan_GetVkGetInstanceProcAddr'] = ctypes.c_void_p

    SDL2_API_NAMES.append('SDL_Vulkan_UnloadLibrary')
    SDL2_API_ARGS_MAP['SDL_Vulkan_UnloadLibrary'] = None
    SDL2_API_RETVAL_MAP['SDL_Vulkan_UnloadLibrary'] = None

    SDL2_API_NAMES.append('SDL_Vulkan_GetInstanceExtensions')
    SDL2_API_ARGS_MAP['SDL_Vulkan_GetInstanceExtensions'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p]
    SDL2_API_RETVAL_MAP['SDL_Vulkan_GetInstanceExtensions'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_Vulkan_CreateSurface')
    SDL2_API_ARGS_MAP['SDL_Vulkan_CreateSurface'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_Vulkan_CreateSurface'] = ctypes.c_int

    SDL2_API_NAMES.append('SDL_Vulkan_GetDrawableSize')
    SDL2_API_ARGS_MAP['SDL_Vulkan_GetDrawableSize'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    SDL2_API_RETVAL_MAP['SDL_Vulkan_GetDrawableSize'] = None


