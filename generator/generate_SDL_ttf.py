import sdl2_parser, sdl2_generator

if __name__ == "__main__":

    ctx = sdl2_parser.ParseContext('./SDL2/SDL_ttf.h')
    sdl2_parser.execute(ctx)

    sdl2_generator.sanitize(ctx)
    sdl2_generator.generate(ctx,
                            prefix = sdl2_generator.PREFIX +
                            "from .api import SDL2_TTF_API_NAMES, SDL2_TTF_API_ARGS_MAP, SDL2_TTF_API_RETVAL_MAP\n" +
                            "from .sdl2_pixels import SDL_Color\n",
                            table_prefix = "SDL2_TTF_")
