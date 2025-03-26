class Node:
    pass

class Number(Node):
    def __init__(self, value):
        self.value = int(value)

class Return(Node):
    def __init__(self, expr):
        self.expr = expr

class Function(Node):
    def __init__(self, name, body):
        self.name = name
        self.body = body

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self, expected_type):
        token_type, token_value = self.tokens[self.pos]
        if token_type != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {token_type}")
        self.pos += 1
        return token_value

    def parse_return(self):
        self.consume('KEYWORD')  # return
        expr = self.consume('NUMBER')
        self.consume('SEMICOLON')
        return Return(Number(expr))

    def parse_function(self):
        self.consume('KEYWORD')  # int
        name = self.consume('IDENTIFIER')
        self.consume('LPAREN')
        self.consume('RPAREN')
        self.consume('LBRACE')
        stmt = self.parse_return()
        self.consume('RBRACE')
        return Function(name, stmt)

    def parse(self):
        return self.parse_function()

if __name__ == "__main__":
    from lexer import lexer
    code = "int main() { return 42; }"
    tokens = lexer(code)
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)
