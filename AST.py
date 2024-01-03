from tokens import Token


class Expr:
    """
    Grouping: (Exp)
    Binary: Expr Token Expr
    Literal: Token
    Prefix: Token Expr
    Postfix: Expr Token
    """
    pass

class Binary(Expr):
    def __init__(self, left: Expr, op: Token, right: Expr) -> None:
        self.left = left;
        self.right = right;
        self.op = op;

class Literal(Expr):
    def __init__(self, literal: Token) -> None:
        self.lit = literal;
