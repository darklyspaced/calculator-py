from enum import Enum

class TokenKind(Enum):
    INTEGER = "INT",
    RPAREN = ')',
    LPAREN = '(',
    PLUS = '+',
    MINUS = '-',
    STAR = '*',
    SLASH = '/',
    CARET = '^',
    EXCLAMATION = '!', # for factorials cause we need a postfix op
    EOF = "EOF",


class Token:
    kind: TokenKind
    lexeme: str
    # literal is essentially just Option<T>

    def __init__(self, kind: TokenKind, lexeme: str, literal):
        self.kind = kind
        self.lexeme = lexeme
        self.literal = literal

    def __str__(self):
        return f'{self.lexeme} {str(self.kind.name)}'
