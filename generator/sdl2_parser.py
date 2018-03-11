import os, pprint, re, sys
from clang.cindex import Config, CursorKind, Index, TranslationUnit, TranslationUnitLoadError, TypeKind

Config.set_library_path("/usr/local/Cellar/llvm/5.0.1/lib")

####################################################################################################

def get_sdl2_cindex_mapping(strTypeKind, strSDL2Typedef):
    if strTypeKind != 'TypeKind.TYPEDEF':
        return strTypeKind

    cindex_mapping = {
        # SDL_stdinc.h
        'SDL_bool' : 'TypeKind.BOOL',
        'Sint8' : 'TypeKind.SCHAR',
        'Sint16' : 'TypeKind.SHORT',
        'Sint32' : 'TypeKind.INT',
        'Sint64' : 'TypeKind.LONG',
        'Uint8' : 'TypeKind.UCHAR',
        'Uint16' : 'TypeKind.USHORT',
        'Uint32' : 'TypeKind.UINT',
        'Uint64' : 'TypeKind.ULONG',
    }
    return cindex_mapping[strSDL2Typedef]

def get_cindex_ctypes_mapping(strTypeKind, strSDL2Typedef):

    pointerToChar = False
    if strTypeKind == 'TypeKind.POINTER':
        pattern = re.compile(r"\schar\s\*")
        m = re.search(pattern, strSDL2Typedef)
        if m:
            pointerToChar = True

    ctypes_mapping = {
        'TypeKind.VOID' : None,
        'TypeKind.BOOL' : 'ctypes.c_bool',
        'TypeKind.CHAR_U' : 'ctypes.c_ubyte',
        'TypeKind.UCHAR' : 'ctypes.c_uint8',
        'TypeKind.CHAR16' : 'ctypes.c_int16',
        'TypeKind.CHAR32' : 'ctypes.c_int32',
        'TypeKind.USHORT' : 'ctypes.c_ushort',
        'TypeKind.UINT' : 'ctypes.c_uint',
        'TypeKind.ULONG' : 'ctypes.c_ulong',
        'TypeKind.ULONGLONG' : 'ctypes.c_ulonglong',
        'TypeKind.UINT128' : 'ctypes.c_ulonglong',
        'TypeKind.CHAR_S' : 'ctypes.c_char',
        'TypeKind.SCHAR' : 'ctypes.c_char',
        'TypeKind.WCHAR' : 'ctypes.c_wchar',
        'TypeKind.SHORT' : 'ctypes.c_short',
        'TypeKind.INT' : 'ctypes.c_int',
        'TypeKind.LONG' : 'ctypes.c_long',
        'TypeKind.LONGLONG' : 'ctypes.c_longlong',
        'TypeKind.INT128' : 'ctypes.c_longlong',
        'TypeKind.FLOAT' : 'ctypes.c_float',
        'TypeKind.DOUBLE' : 'ctypes.c_double',
        'TypeKind.LONGDOUBLE' : 'ctypes.c_longdouble',
        'TypeKind.NULLPTR' : 'ctypes.c_void_p',
        'TypeKind.POINTER' : 'ctypes.c_void_p',
        'TypeKind.ENUM' : 'ctypes.c_int',
    }

    if pointerToChar:
        return 'ctypes.c_char_p'
    else:
        return ctypes_mapping[get_sdl2_cindex_mapping(strTypeKind, strSDL2Typedef)]


####################################################################################################

class FieldInfo(object):
    """
    Holds one field of struct/union.
    """

    def __init__(self):
        self.element_count = -1
        self.element_name = ""
        self.type_kind = TypeKind.INVALID
        self.type_name = ""

    def __repr__(self):
        return str(vars(self))

class StructInfo(object):
    """
    Holds struct/union information.
    """

    def __init__(self):
        self.fields = []
        self.kind = None # CursorKind.STRUCT_DECL or CursorKind.UNION_DECL
        self.name = "" # ex.) nk_color

    def __repr__(self):
        return str(vars(self))

    def push(self, field):
        self.fields.append(field)

    def pop(self):
        self.fields.pop()

class TypedefInfo(object):
    """
    Holds typedef information.
    """

    def __init__(self):
        self.name = ""
        self.element_count = -1
        self.type_kind = TypeKind.INVALID

    def __repr__(self):
        return "%s : ((%s) x %s)" % (self.name, self.type_kind, self.element_count)

class ArgumentInfo(object):
    """
    Holds one argument of function.
    """

    def __init__(self):
        self.name = ""
        self.type_kind = TypeKind.INVALID
        self.type_name = ""

    def __repr__(self):
        return str(vars(self))

class RetvalInfo(object):
    """
    Holds return value information.
    """

    def __init__(self):
        self.type_kind = TypeKind.INVALID
        self.type_name = ""

    def __repr__(self):
        return str(vars(self))

class FunctionInfo(object):
    """
    Holds function information.
    """

    def __init__(self):
        self.name = ""
        self.args = []
        self.retval = None

    def __repr__(self):
        return str(vars(self))

class ParseContext(object):
    """
    Holds current parsing context.
    """

    # Collection Mode
    Decl_Unknown  = 0
    Decl_Macro    = 1
    Decl_Typedef  = 2
    Decl_Enum     = 3
    Decl_Struct   = 4
    Decl_Function = 5

    def __init__(self, fn = ""):
        self.collection_mode = ParseContext.Decl_Unknown
        self.depth = 0
        self.decl_enums = {}
        self.decl_macros = {}
        self.decl_structs = {}
        self.decl_typedefs = {}
        self.decl_functions = {}
        self.parse_file = fn

    def push(self):
        self.depth += 1

    def pop(self):
        self.depth -= 1

    def add_decl_enum(self, name=None, values=[]):
        if name == None or name == "":
            name = "anonymous_enum_"  + str(len(self.decl_enums))
        self.decl_enums[name] = values

    def add_decl_macro(self, macro_name, macro_value):
        self.decl_macros[macro_name] = macro_value

    def add_decl_struct(self, struct_name, struct_value):
        self.decl_structs[struct_name] = struct_value

    def add_decl_typedef(self, typedef_name, typedef_value):
        self.decl_typedefs[typedef_name] = typedef_value

    def add_decl_function(self, function_name, function_value):
        self.decl_functions[function_name] = function_value

####################################################################################################

def collect_decl_macro(ctx, cursor):

    if str(cursor.location.file) != ctx.parse_file:
        return # pass

    ctx.collection_mode = ParseContext.Decl_Macro
    tokens = list(cursor.get_tokens())
    macro_name = str(tokens[0].spelling)
    # omit parenthesis -> concatenate all tokens except 'macro_name (tokens[0])'
    # macro_value = map((lambda t: str(t.spelling.replace('(', '').replace(')', ''))), tokens[1:len(tokens)])
    # macro_value = ''.join(macro_value)

    # macro_value = map((lambda t: str(t.spelling)), tokens[1:len(tokens)])
    # macro_value = ' '.join(macro_value)

    macro_value = list(map((lambda t: str(t.spelling)), tokens[1:len(tokens)]))

    # pick out numerical values with 'SDL_' prefix
    if re.match(r"^SDL_", macro_name): #and re.match(r"[+-]?\d+", macro_value):
        ctx.add_decl_macro(macro_name, macro_value)
    ctx.collection_mode = ParseContext.Decl_Unknown

def collect_decl_typedef(ctx, cursor):

    if str(cursor.location.file) != ctx.parse_file:
        return # pass

    ctx.collection_mode = ParseContext.Decl_Typedef
    ctx.push()

    underlying_type = cursor.underlying_typedef_type
    # print(cursor.type.spelling, underlying_type.spelling)
    typedef_info = TypedefInfo()
    typedef_info.name = cursor.displayname
    typedef_info.type_kind = underlying_type.get_canonical().kind
    typedef_info.element_count = 1

    if underlying_type.kind in {TypeKind.CONSTANTARRAY, TypeKind.INCOMPLETEARRAY, TypeKind.VARIABLEARRAY, TypeKind.DEPENDENTSIZEDARRAY}:
        typedef_info.type_kind = underlying_type.get_array_element_type().get_canonical().kind
        typedef_info.element_count = underlying_type.get_array_size()
    elif underlying_type.kind == TypeKind.POINTER:
        if underlying_type.get_pointee().get_canonical().kind == TypeKind.FUNCTIONPROTO:
            typedef_info.type_kind = underlying_type.get_pointee().get_canonical().kind
    elif underlying_type.kind == TypeKind.ELABORATED:
        ctx.push()
        cursor_structunion = underlying_type.get_declaration() # CursorKind.STRUCT_DECL or CursorKind.UNION_DECL
        collect_decl_struct(ctx, cursor_structunion, cursor.displayname)
        ctx.pop()
    else:
        pass
    ctx.pop()
    ctx.add_decl_typedef(typedef_info.name, typedef_info)
    ctx.collection_mode = ParseContext.Decl_Unknown

def collect_decl_enum(ctx, cursor):

    if str(cursor.location.file) != ctx.parse_file:
        return # pass

    ctx.collection_mode = ParseContext.Decl_Enum
    val = []
    ctx.push()
    for child in cursor.get_children():
        if child.kind == CursorKind.ENUM_CONSTANT_DECL:
            pair = (child.displayname, child.enum_value)
            val.append(pair)
    ctx.pop()
    ctx.add_decl_enum(name=cursor.displayname, values=val)
    ctx.collection_mode = ParseContext.Decl_Unknown

def collect_decl_struct(ctx, cursor, typedef_name=None):

    if str(cursor.location.file) != ctx.parse_file:
        return # pass

    ctx.collection_mode = ParseContext.Decl_Struct

    n_children = len(list(cursor.get_children()))
    if (not cursor.kind in {CursorKind.STRUCT_DECL, CursorKind.UNION_DECL}) or n_children <= 0:
        return

    struct_info = StructInfo()
    struct_info.kind = cursor.kind # CursorKind.STRUCT_DECL or CursorKind.UNION_DECL
    struct_info.name = typedef_name if typedef_name != None else cursor.displayname

    # NOTE : unnamed struct/union will be collected at 'collect_decl_typedef'.
    # ex.) typedef union {void *ptr; int id;} nk_handle; (exposed as an unnamed struct/union here)
    if struct_info.name == "":
        return

    fields = cursor.type.get_fields()
    for field in fields:
        ctx.push()
        canonical_kind = field.type.get_canonical().kind

        field_info = FieldInfo()
        field_info.element_count = 1
        field_info.element_name = field.displayname
        field_info.type_kind = canonical_kind
        field_info.type_name = field.type.spelling

        if canonical_kind in {TypeKind.CONSTANTARRAY, TypeKind.INCOMPLETEARRAY, TypeKind.VARIABLEARRAY, TypeKind.DEPENDENTSIZEDARRAY}:
            element_kind = field.type.get_array_element_type().kind
            element_detail = ""
            if element_kind in {TypeKind.ELABORATED, TypeKind.RECORD}:
                element_detail = " (" + field.type.spelling + ")"
            field_info.element_count = field.type.get_array_size()
        elif canonical_kind in {TypeKind.ELABORATED, TypeKind.RECORD}:
            pass # print("%s%s" % ("  " * (ctx.depth + 1), field.type.spelling))
        else:
            pass

        struct_info.push(field_info)
        ctx.pop()

    ctx.add_decl_struct(struct_info.name, struct_info)

    ctx.collection_mode = ParseContext.Decl_Unknown

def collect_decl_function(ctx, cursor):

    if str(cursor.location.file) != ctx.parse_file:
        return # pass

    ctx.collection_mode = ParseContext.Decl_Function
    ctx.push()

    func_info = FunctionInfo()
    func_info.name = cursor.spelling

    retval_info = RetvalInfo()
    retval_info.type_name = cursor.result_type.spelling
    retval_info.type_kind = cursor.result_type.kind

    func_info.retval = retval_info

    args = cursor.get_arguments()
    for arg in args:
        arg_info = ArgumentInfo()
        arg_info.name = arg.spelling
        arg_info.type_name = arg.type.spelling
        arg_info.type_kind = arg.type.get_canonical().kind
        func_info.args.append(arg_info)

    ctx.add_decl_function(func_info.name, func_info)

    ctx.pop()
    ctx.collection_mode = ParseContext.Decl_Unknown

def collect_decl(ctx, cursor):
    ctx.push()
    for child in cursor.get_children():
        if child.kind == CursorKind.MACRO_DEFINITION:
            collect_decl_macro(ctx, child)
        elif child.kind == CursorKind.TYPEDEF_DECL:
             collect_decl_typedef(ctx, child)
        elif child.kind == CursorKind.ENUM_DECL:
            collect_decl_enum(ctx, child)
        elif child.kind in {CursorKind.STRUCT_DECL, CursorKind.UNION_DECL}:
            collect_decl_struct(ctx, child)
        elif child.kind == CursorKind.FUNCTION_DECL:
            collect_decl_function(ctx, child)
        else:
            pass

    ctx.pop()


def execute(ctx):
    arg = [
        "-I/usr/local/Cellar/sdl2/2.0.8/include/", "-fsyntax-only", "-DDOXYGEN_SHOULD_IGNORE_THIS",
    ]

    opt = TranslationUnit.PARSE_SKIP_FUNCTION_BODIES | TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD | TranslationUnit.PARSE_INCOMPLETE
    idx = Index.create()

    try:
        tu  = idx.parse(ctx.parse_file, args=arg, unsaved_files=None, options=opt)
        ctx.depth = 0
        collect_decl(ctx, tu.cursor)
    except TranslationUnitLoadError as err:
        print(err)

    assert ctx.depth == 0
