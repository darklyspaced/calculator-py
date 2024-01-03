import lexer;

while True:
    src = str(input(">> "))
    lex = lexer.Lexer(src)
    tokens = lex.get_tokens()
    lex.print_tokens();
