import sdl2_parser, sdl2_generator

POSTFIX_GAMECONTROLLER = """
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
"""

if __name__ == "__main__":

    ctx = sdl2_parser.ParseContext('./SDL2/SDL_gamecontroller.h')
    sdl2_parser.execute(ctx)

    # TODO : Merge anonymous structs into one union (e.g. SDL_RWops)
    #
    # SDL_GameControllerButtonBind is a bit complicated so I unfortunately have to
    # substitute the parsed definition with my handwritten one.
    ctx.decl_structs['SDL_GameControllerButtonBind'] = None

    sdl2_generator.sanitize(ctx)
    sdl2_generator.generate(ctx,
                            prefix = sdl2_generator.PREFIX + "from .sdl2_joystick import SDL_JoystickGUID\n",
                            postfix = sdl2_generator.POSTFIX + POSTFIX_GAMECONTROLLER)
