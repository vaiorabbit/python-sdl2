import ctypes, re, sys
import sdl2_parser

PREFIX = """import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
"""

####################################################################################################

def sanitize_macro(ctx):
    # omit include guard
    del ctx.decl_macros['SDL_h_']

    # 0x____u -> 0x____
    pattern = re.compile(r'(0x[0-9a-fA-F]+)u')
    for macro_name, macro_value in ctx.decl_macros.items():
        if len(macro_value) != 1:
            continue
        m = re.search(pattern, macro_value[0])
        if m:
            ctx.decl_macros[macro_name][0] = m.group(1)

def sanitize_function(ctx):
    for func_name, func_info in ctx.decl_functions.items():
        for arg in func_info.args:
            arg.type_kind = sdl2_parser.get_cindex_ctypes_mapping(str(arg.type_kind), arg.type_name)
        func_info.retval.type_kind = sdl2_parser.get_cindex_ctypes_mapping(str(func_info.retval.type_kind), func_info.retval.type_name)

def sanitize(ctx):
    sanitize_macro(ctx)
    sanitize_function(ctx)

####################################################################################################

def reformat_macro(ctx):
    # contatinate (SDL_INIT_EVERYTHING)
    for macro_name, macro_value in ctx.decl_macros.items():
        if len(macro_value) <= 1:
            continue
        ctx.decl_macros[macro_name] = [''.join(macro_value)]

def reformat_function(ctx):
    pass

def reformat(ctx):
    reformat_macro(ctx)
    reformat_function(ctx)

####################################################################################################

def generate(ctx):

    print(PREFIX, file = sys.stdout)

    for macro_name, macro_value in ctx.decl_macros.items():
        print("%s = %s" % (macro_name, macro_value[0]), file = sys.stdout)

    print("", file = sys.stdout)
    print("def setup_symbols():", file = sys.stdout)
    for func_name, func_info in ctx.decl_functions.items():
        print("    SDL2_API_NAMES.append('%s')" % (func_name), file = sys.stdout)
        if len(func_info.args) == 0:
            print("    SDL2_API_ARGS_MAP['%s'] = None" % (func_name) , file = sys.stdout)
        else:
            args_str = list(map((lambda t: str(t.type_kind)), func_info.args))
            print("    SDL2_API_ARGS_MAP['%s'] = [%s]" % (func_name, ', '.join(args_str)), file = sys.stdout)
        print("    SDL2_API_RETVAL_MAP['%s'] = %s" % (func_name, str(func_info.retval.type_kind)), file = sys.stdout)
        print("", file = sys.stdout)

if __name__ == "__main__":
    ctx = sdl2_parser.ParseContext('./SDL2/SDL.h')
    sdl2_parser.execute(ctx)

    sanitize(ctx)
    reformat(ctx)
    generate(ctx)
