import sdl2_parser, sdl2_generator

if __name__ == "__main__":

    ctx = sdl2_parser.ParseContext('./SDL2/SDL_surface.h')
    sdl2_parser.execute(ctx)

    sdl2_generator.sanitize(ctx)
    sdl2_generator.generate(ctx, prefix = sdl2_generator.PREFIX + "from .sdl2_rect import SDL_Rect\n")
