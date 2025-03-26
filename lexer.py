import re

# Define token types
TOKEN_SPEC = [
    ('KEYWORD', r'\b(int|return)\b'),
    ('NUMBER', r'\b\d+\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('OP', r'[=+*/-]'),
    ('SEMICOLON', r';'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('WHITESPACE', r'\s+'),
]

TOKEN_REGEX = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPEC)

def lexer(code):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, code):
        kind = match.lastgroup
        value = match.group()
        if kind != 'WHITESPACE':  # Ignore spaces
            tokens.append((kind, value))
    return tokens

if __name__ == "__main__":
    code = "int main() { return 42; }"
    print(lexer(code))
