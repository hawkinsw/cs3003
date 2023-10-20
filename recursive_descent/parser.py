from lexer import tokenizer, token
from parser import parser

def main():
    contents, tknzr = tokenizer.create_tokenizer("testing.input")

    parseri = parser.Parser(tknzr)
    parsed = parseri.parseExpr()

    if parseri.redo_tkn != None and not isinstance(parseri.redo_tkn,token.EOF):
        print(f"Parsing error: {parseri.redo_tkn}")
        return
    print(f"\n\n{contents=}\n...\nparses as ...\n")
    tree = parseri.tree_at(parsed)
    print(tree.show(stdout=False, data_property="node_repr"))

if __name__=="__main__":
    main()