import sdl2_parser, sdl2_generator

PREFIX_RWOPS = """import os
"""

POSTFIX_RWOPS = """
class _SDL_RWops_mem(ctypes.Structure):
    _fields_ = [
        ("base", ctypes.POINTER(ctypes.c_uint8)),
        ("here", ctypes.POINTER(ctypes.c_uint8)),
        ("stop", ctypes.POINTER(ctypes.c_uint8)),
    ]

class _SDL_RWops_unknown(ctypes.Structure):
    _fields_ = [
        ("data1", ctypes.c_void_p),
        ("data2", ctypes.c_void_p),
    ]

class _SDL_RWops_windowsio_buffer(ctypes.Structure):
    _fields_ = [
        ("data", ctypes.c_void_p),
        ("size", ctypes.c_size_t),
        ("left", ctypes.c_size_t),
    ]

class _SDL_RWops_windowsio(ctypes.Structure):
    _fields_ = [
        ("append", ctypes.c_int),
        ("h", ctypes.c_void_p),
        ("buffer", _SDL_RWops_windowsio_buffer),
    ]

class _Default_SDL_RWops_hidden(ctypes.Union):
    _anonymous_ = ('mem', 'unknown')
    _fields_ = [
        ("mem", _SDL_RWops_mem),
        ("unknown", _SDL_RWops_unknown),
    ]

class _Win32_SDL_RWops_hidden(ctypes.Union):
    _anonymous_ = ('mem', 'unknown', 'windowsio')
    _fields_ = [
        ("mem", _SDL_RWops_mem),
        ("unknown", _SDL_RWops_unknown),
        ("windowsio", _SDL_RWops_windowsio),
    ]

class _Default_SDL_RWops(ctypes.Structure):
    _fields_ = [
        ("size", ctypes.c_void_p),
        ("seek", ctypes.c_void_p),
        ("read", ctypes.c_void_p),
        ("write", ctypes.c_void_p),
        ("close", ctypes.c_void_p),
        ("type", ctypes.c_uint),
        ("hidden", _Default_SDL_RWops_hidden),
    ]

class _Win32_SDL_RWops(ctypes.Structure):
    _fields_ = [
        ("size", ctypes.c_void_p),
        ("seek", ctypes.c_void_p),
        ("read", ctypes.c_void_p),
        ("write", ctypes.c_void_p),
        ("close", ctypes.c_void_p),
        ("type", ctypes.c_uint),
        ("hidden", _Win32_SDL_RWops_hidden),
    ]

SDL_RWops = _Win32_SDL_RWops if os.name == "nt" else _Default_SDL_RWops
"""

if __name__ == "__main__":

    ctx = sdl2_parser.ParseContext('./SDL2/SDL_rwops.h')
    sdl2_parser.execute(ctx)

    # TODO : Merge anonymous structs into one union (e.g. SDL_RWops)
    #
    # SDL_RWops is a bit complicated so I unfortunately have to
    # substitute the parsed definition with my handwritten one.
    ctx.decl_structs['SDL_RWops'] = None

    sdl2_generator.sanitize(ctx)
    sdl2_generator.generate(ctx,
                            prefix = sdl2_generator.PREFIX + PREFIX_RWOPS,
                            postfix = sdl2_generator.POSTFIX + POSTFIX_RWOPS)
