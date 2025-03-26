Cpylier is a C Compiler written in Python.

# Current Features
1. Parsing & AST Generation
	- Reads source code
	- Generates Abstract Syntax tree
2. Semantic Analysis
	- Type checking & Scope Validation of AST
3. LLVM IR Generation
	- Converts AST to LLVM Intermediate Representation
	- Sets target triple dynamically.
4. User chosen Execution modes
	- JIT Execution - Runs IR directly with LLVM JIT
	- IR Output - Outputs IR
	- Clang Compilation - Compiles IR to executable
	
# Planned Features
1. C Language features
	- Variables & Assignments
	- Conditionals
	- Loops
	- Function Calls
	- Structs & Pointers
	- C Standard Library
2. Backend Improvements
	- Generate ASM instead of IR
	- Custom x86_64 backend to replace Clang
3. IR Optimisations
	- Constant Folding
	- Dead Code Elmination
	- Loop Unrolling
	- Function Inlining
	- LLVM Optimsation Passes
4. D- ebugging/Error Handling
	- Syntax Error reporting
	- Semantic Error detection
	- AST Pretty-Printing
5. A- head of Time Compilation
	- Custom Object File Generator
	- Customer Linker
6. M- ulti-File Compilation
	- Multiple files
	- Support include statements
	
# Roadmap
1. Support variables, conditionals, loops
2. Improve error handling
3. Constant folding, dead code elmination
4. Multi-File Compilation
5. Assembler Backend