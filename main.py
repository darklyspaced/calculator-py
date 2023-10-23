import lexer;

while True:
    src = str(input(">> "))
    lex = lexer.Lexer(src)
    lex.lex()
    lex.print_tokens();
