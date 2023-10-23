import lexer;

while True:
    src = str(input(">> "))
    lex = lexer.Lexer(src)
    # for tok in lex.lex():
    #     print(tok)
    print([tok.__str__() for tok in lex.lex()])


