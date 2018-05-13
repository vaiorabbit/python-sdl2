import ctypes, re, sys
import sdl2_parser

PREFIX = """# Python-SDL2 : Yet another SDL2 wrapper for Python
#
# * https://github.com/vaiorabbit/python-sdl2
#
# [NOTICE] This is an automatically generated file.

import ctypes
from .api import SDL2_API_NAMES, SDL2_API_ARGS_MAP, SDL2_API_RETVAL_MAP
"""
POSTFIX = ""

####################################################################################################

def sanitize_enum(ctx):
    pass

def sanitize_macro(ctx):
    # 0x____u -> 0x____
    pattern = re.compile(r'(0x[0-9a-fA-F]+)u')
    for macro_name, macro_value in ctx.decl_macros.items():
        if len(macro_value) != 1:
            continue
        m = re.search(pattern, macro_value[0])
        if m:
            ctx.decl_macros[macro_name][0] = m.group(1)

    # refer mapping
    for macro_name, macro_value in ctx.decl_macros.items():
        define_mapping = sdl2_parser.get_define_mapping(macro_name)
        if define_mapping:
            ctx.decl_macros[macro_name] = define_mapping
        else:
            ctx.decl_macros[macro_name] = None

    # contatinate (SDL_INIT_EVERYTHING, etc.)
    for macro_name, macro_value in ctx.decl_macros.items():
        if macro_value == None or len(macro_value) <= 1:
            continue
        ctx.decl_macros[macro_name] = [''.join(macro_value)]

def sanitize_struct(ctx):
    for struct_name, struct_info in ctx.decl_structs.items():
        if struct_info == None:
            continue
        underlying_ctypes_type = "ctypes.Union" if str(struct_info.kind) == "CursorKind.UNION_DECL" else "ctypes.Structure"
        struct_info.kind = underlying_ctypes_type
        for field in struct_info.fields:
            field.type_kind = sdl2_parser.get_cindex_ctypes_mapping(str(field.type_kind), field.type_name)

def sanitize_typedef(ctx):
    # refer mapping
    for typedef_name, typedef_info in ctx.decl_typedefs.items():
        if typedef_info.func_proto != None:
            for arg in typedef_info.func_proto.args:
                arg.type_kind = sdl2_parser.get_cindex_ctypes_mapping(str(arg.type_kind), arg.type_name)
            typedef_info.func_proto.retval.type_kind = sdl2_parser.get_cindex_ctypes_mapping(str(typedef_info.func_proto.retval.type_kind), typedef_info.func_proto.retval.type_name)
        else:
            if str(typedef_info.type_kind) == "TypeKind.RECORD":
                typedef_info.type_kind = None
            else:
                typedef_info.type_kind = sdl2_parser.get_cindex_ctypes_mapping(str(typedef_info.type_kind), typedef_info.name)

def sanitize_function(ctx):
    for func_name, func_info in ctx.decl_functions.items():
        if func_info == None:
            continue
        for arg in func_info.args:
            arg.type_kind = sdl2_parser.get_cindex_ctypes_mapping(str(arg.type_kind), arg.type_name)
        func_info.retval.type_kind = sdl2_parser.get_cindex_ctypes_mapping(str(func_info.retval.type_kind), func_info.retval.type_name)

def sanitize(ctx):
    sanitize_enum(ctx)
    sanitize_macro(ctx)
    sanitize_struct(ctx)
    sanitize_typedef(ctx)
    sanitize_function(ctx)

####################################################################################################

def generate(ctx, prefix = PREFIX, postfix = POSTFIX, *, table_prefix = "SDL2_"):

    print(prefix, file = sys.stdout)

    # macro
    print("# Define/Macro")
    for macro_name, macro_value in ctx.decl_macros.items():
        if macro_value != None:
            print("%s = %s" % (macro_name, macro_value[0]), file = sys.stdout)
    print("", file = sys.stdout)

    # enum
    print("# Enum")
    for enum_name, enum_value in ctx.decl_enums.items():
        for enum in enum_value:
            print("%s = %s" % (enum[0], enum[1]), file = sys.stdout)
    print("", file = sys.stdout)

    # typedef
    print("# Typedef")
    for typedef_name, typedef_info in ctx.decl_typedefs.items():
        if typedef_info.type_kind == None:
            continue
        typedef_line = "%s = " % typedef_name
        if typedef_info.func_proto != None:
            typedef_line += "ctypes.CFUNCTYPE(%s" % typedef_info.func_proto.retval.type_kind
            for arg in typedef_info.func_proto.args:
                typedef_line += ", %s" % arg.type_kind
            typedef_line += ")"
        else:
            typedef_line += typedef_info.type_kind
        print(typedef_line, file = sys.stdout)
    print("", file = sys.stdout)

    # struct/union
    print("# Struct")
    print("", file = sys.stdout)
    for struct_name, struct_info in ctx.decl_structs.items():
        if struct_info == None:
            continue
        print("class %s(%s):" % (struct_name, struct_info.kind), file = sys.stdout)
        print("    _fields_ = [", file = sys.stdout)
        for field in struct_info.fields:
            element_count = "" if field.element_count <= 1 else " * %s" % (field.element_count)
            print("        (\"%s\", %s%s)," % (field.element_name, field.type_kind, element_count), file = sys.stdout)
        print("    ]\n", file = sys.stdout)

    # function
    print("# Function")
    print("def setup_symbols():", file = sys.stdout)
    if len(ctx.decl_functions) == 0:
        print("    pass", file = sys.stdout)
    else:
        for func_name, func_info in ctx.decl_functions.items():
            if func_info == None:
                continue
            print("    %sAPI_NAMES.append('%s')" % (table_prefix, func_name), file = sys.stdout)
            if len(func_info.args) == 0:
                print("    %sAPI_ARGS_MAP['%s'] = None" % (table_prefix, func_name) , file = sys.stdout)
            else:
                args_str = list(map((lambda t: str(t.type_kind)), func_info.args))
                print("    %sAPI_ARGS_MAP['%s'] = [%s]" % (table_prefix, func_name, ', '.join(args_str)), file = sys.stdout)
            print("    %sAPI_RETVAL_MAP['%s'] = %s" % (table_prefix, func_name, str(func_info.retval.type_kind)), file = sys.stdout)
            print("", file = sys.stdout)

    print(postfix, file = sys.stdout)

if __name__ == "__main__":

    PREFIX += "from .sdl2_keyboard import SDL_Keysym\n"

    ctx = sdl2_parser.ParseContext('./SDL2/SDL_events.h')
    sdl2_parser.execute(ctx)

    for typedef_name, typedef_info in ctx.decl_typedefs.items():
        sdl2_parser.register_sdl2_cindex_mapping(str(typedef_info.type_kind), typedef_name)

    sanitize(ctx)
    generate(ctx, PREFIX)
