import sys
import subprocess
from lexer import lexer
from parser import Parser
from semantic import check
from codegen import generate_ir
from llvmlite import binding

def execute_ir(ir_code):
    """Execute LLVM IR using JIT."""
    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()

    target = binding.Target.from_default_triple()
    target_machine = target.create_target_machine()

    mod = binding.parse_assembly(str(ir_code))
    mod.verify()

    engine = binding.create_mcjit_compiler(mod, target_machine)
    engine.finalize_object()
    
    entry_func = engine.get_function_address("main")
    
    import ctypes
    func = ctypes.CFUNCTYPE(ctypes.c_int)(entry_func)
    return func()

def compile_with_clang(ir_code, output_filename="output"):
    """Save IR to file and compile with Clang."""
    ir_filename = output_filename + ".ll"
    exe_filename = output_filename

    # Write IR to file
    with open(ir_filename, "w") as f:
        f.write(str(ir_code))

    # Compile with Clang
    clang_command = ["clang", ir_filename, "-o", exe_filename]
    subprocess.run(clang_command, check=True)

    print(f"Compiled successfully! Run with: ./{exe_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python compiler.py <mode> <filename.c>")
        print("Modes: --ir (print IR) | --jit (interpret) | --clang (compile with Clang)")
        sys.exit(1)

    mode = sys.argv[1]
    filename = sys.argv[2]

    with open(filename) as f:
        code = f.read()

    tokens = lexer(code)
    parser = Parser(tokens)
    ast = parser.parse()
    check(ast)
    module = generate_ir(ast)

    if mode == "--ir":
        print("Generated LLVM IR:")
        print(module)

    elif mode == "--jit":
        print("Executing IR in Python (JIT Mode):")
        result = execute_ir(module)
        print("Return value:", result)

    elif mode == "--clang":
        compile_with_clang(module)

    else:
        print("Invalid mode. Use --ir, --jit, or --clang.")
