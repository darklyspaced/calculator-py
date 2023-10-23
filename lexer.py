from typing import List, Optional
from tokens import Token, TokenKind;

class Lexer:
    src = ""
    pos = 0
    tokens = []
    ch = ''

    def __init__(self, src: str):
        self.src = src


    def lex(self) -> List[Token]:
        while self.eat() != None:
            self.skip_whitespace()
            match self.ch:
                case '(':
                    self.add_tok(TokenKind.LPAREN)
                case ')':
                    self.add_tok(TokenKind.RPAREN)
                case '+':
                    self.add_tok(TokenKind.PLUS)
                case '-':
                    self.add_tok(TokenKind.MINUS)
                case '/':
                    self.add_tok(TokenKind.SLASH)
                case '*':
                    self.add_tok(TokenKind.STAR)
                case '^':
                    self.add_tok(TokenKind.CARET)
                case '!':
                    self.add_tok(TokenKind.EXCLAMATION)
                case None:
                    self.add_tok(TokenKind.EOF)
                case _: # NOTE: source of many bugs if impl is taken further
                    if self.ch.isnumeric():
                        num = [self.ch] 
                        next = self.eat()

                        while next != None and next.isnumeric():
                            num.append(self.ch)
                            next = self.eat()

                        lex = "".join(num)
                        self.add_tok(TokenKind.INTEGER, lex, int(lex))
                    else:
                        print("unsupported symbol: ", self.ch)

        return self.tokens
                    

    def add_tok(self, kind, lex = None, lit = None):
        if lex == None:
            self.tokens.append(Token(kind, self.ch, lit))
        else:
            self.tokens.append(Token(kind, lex, lit))


    def eat(self) -> Optional[str]:
        if not self.at_end():
            self.ch = self.src[self.pos] 
            self.pos += 1
            return self.ch
        return None;


    def peek(self) -> str:
        return self.src[self.pos + 1]


    def skip_whitespace(self):
        while self.ch.isspace():
            if self.eat() == None:
                return

    def at_end(self) -> bool:
        if self.pos > len(self.src) - 1:
            return True
        else:
            return False
