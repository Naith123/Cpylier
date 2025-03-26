from llvmlite import ir
import platform

def get_target_triple():
    """ 
    Uses platform module to automatically select the correct target triple
    """
    system = platform.system()
    match system:
        case "Windows":
            return "x86_64-pc-windows-msvc"
        case "Linux":
            return "x86_64-pc-linux-gnu"
        case "Darwin":
            return "x86_64-apple-darwin"  # macOS
        case _:
            raise RuntimeError(f"Unsupported OS: {system}")

def generate_ir(ast):
    module = ir.Module(name="module")
    module.triple = get_target_triple()


    func_type = ir.FunctionType(ir.IntType(32), [])
    main_func = ir.Function(module, func_type, name=ast.name)

    block = main_func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)

    ret_val = ir.Constant(ir.IntType(32), ast.body.expr.value)
    builder.ret(ret_val)

    return module
