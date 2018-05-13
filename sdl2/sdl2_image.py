# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
from .api import SDL2_IMG_API_NAMES, SDL2_IMG_API_ARGS_MAP, SDL2_IMG_API_RETVAL_MAP

# Define/Macro
SDL_IMAGE_MAJOR_VERSION = 2
SDL_IMAGE_MINOR_VERSION = 0
SDL_IMAGE_PATCHLEVEL = 3

# Enum
IMG_INIT_JPG = 1
IMG_INIT_PNG = 2
IMG_INIT_TIF = 4
IMG_INIT_WEBP = 8

# Typedef
IMG_InitFlags = ctypes.c_int

# Struct

# Function
def setup_symbols():
    SDL2_IMG_API_NAMES.append('IMG_Linked_Version')
    SDL2_IMG_API_ARGS_MAP['IMG_Linked_Version'] = None
    SDL2_IMG_API_RETVAL_MAP['IMG_Linked_Version'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_Init')
    SDL2_IMG_API_ARGS_MAP['IMG_Init'] = [ctypes.c_int]
    SDL2_IMG_API_RETVAL_MAP['IMG_Init'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_Quit')
    SDL2_IMG_API_ARGS_MAP['IMG_Quit'] = None
    SDL2_IMG_API_RETVAL_MAP['IMG_Quit'] = None

    SDL2_IMG_API_NAMES.append('IMG_LoadTyped_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadTyped_RW'] = [ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadTyped_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_Load')
    SDL2_IMG_API_ARGS_MAP['IMG_Load'] = [ctypes.c_char_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_Load'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_Load_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_Load_RW'] = [ctypes.c_void_p, ctypes.c_int]
    SDL2_IMG_API_RETVAL_MAP['IMG_Load_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadTexture')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadTexture'] = [ctypes.c_void_p, ctypes.c_char_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadTexture'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadTexture_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadTexture_RW'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadTexture_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadTextureTyped_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadTextureTyped_RW'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadTextureTyped_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_isICO')
    SDL2_IMG_API_ARGS_MAP['IMG_isICO'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isICO'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isCUR')
    SDL2_IMG_API_ARGS_MAP['IMG_isCUR'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isCUR'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isBMP')
    SDL2_IMG_API_ARGS_MAP['IMG_isBMP'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isBMP'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isGIF')
    SDL2_IMG_API_ARGS_MAP['IMG_isGIF'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isGIF'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isJPG')
    SDL2_IMG_API_ARGS_MAP['IMG_isJPG'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isJPG'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isLBM')
    SDL2_IMG_API_ARGS_MAP['IMG_isLBM'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isLBM'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isPCX')
    SDL2_IMG_API_ARGS_MAP['IMG_isPCX'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isPCX'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isPNG')
    SDL2_IMG_API_ARGS_MAP['IMG_isPNG'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isPNG'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isPNM')
    SDL2_IMG_API_ARGS_MAP['IMG_isPNM'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isPNM'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isSVG')
    SDL2_IMG_API_ARGS_MAP['IMG_isSVG'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isSVG'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isTIF')
    SDL2_IMG_API_ARGS_MAP['IMG_isTIF'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isTIF'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isXCF')
    SDL2_IMG_API_ARGS_MAP['IMG_isXCF'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isXCF'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isXPM')
    SDL2_IMG_API_ARGS_MAP['IMG_isXPM'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isXPM'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isXV')
    SDL2_IMG_API_ARGS_MAP['IMG_isXV'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isXV'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_isWEBP')
    SDL2_IMG_API_ARGS_MAP['IMG_isWEBP'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_isWEBP'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_LoadICO_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadICO_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadICO_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadCUR_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadCUR_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadCUR_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadBMP_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadBMP_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadBMP_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadGIF_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadGIF_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadGIF_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadJPG_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadJPG_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadJPG_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadLBM_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadLBM_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadLBM_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadPCX_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadPCX_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadPCX_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadPNG_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadPNG_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadPNG_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadPNM_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadPNM_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadPNM_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadSVG_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadSVG_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadSVG_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadTGA_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadTGA_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadTGA_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadTIF_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadTIF_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadTIF_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadXCF_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadXCF_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadXCF_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadXPM_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadXPM_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadXPM_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadXV_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadXV_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadXV_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_LoadWEBP_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_LoadWEBP_RW'] = [ctypes.c_void_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_LoadWEBP_RW'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_ReadXPMFromArray')
    SDL2_IMG_API_ARGS_MAP['IMG_ReadXPMFromArray'] = [ctypes.c_char_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_ReadXPMFromArray'] = ctypes.c_void_p

    SDL2_IMG_API_NAMES.append('IMG_SavePNG')
    SDL2_IMG_API_ARGS_MAP['IMG_SavePNG'] = [ctypes.c_void_p, ctypes.c_char_p]
    SDL2_IMG_API_RETVAL_MAP['IMG_SavePNG'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_SavePNG_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_SavePNG_RW'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    SDL2_IMG_API_RETVAL_MAP['IMG_SavePNG_RW'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_SaveJPG')
    SDL2_IMG_API_ARGS_MAP['IMG_SaveJPG'] = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
    SDL2_IMG_API_RETVAL_MAP['IMG_SaveJPG'] = ctypes.c_int

    SDL2_IMG_API_NAMES.append('IMG_SaveJPG_RW')
    SDL2_IMG_API_ARGS_MAP['IMG_SaveJPG_RW'] = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    SDL2_IMG_API_RETVAL_MAP['IMG_SaveJPG_RW'] = ctypes.c_int


