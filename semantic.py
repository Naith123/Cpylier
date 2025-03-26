from parser import Node, Number, Return, Function

def check(ast):
    if isinstance(ast, Function):
        if isinstance(ast.body, Return):
            if not isinstance(ast.body.expr, Number):
                raise TypeError("Return value must be a number")
    return True
