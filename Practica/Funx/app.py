from flask import Flask, render_template, request

from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from TreeVisitor import TreeVisitor

app = Flask(__name__)

code = {}

input = []
output = []

@app.route("/", methods=['POST', 'GET'])
def home():
    global code
    result = request.form

    for key, value in result.items():
        value = value.replace('\r', '')
        value = value.replace('\n', '')

        pos_func = ""

        i = 0
        c = value[i]
        if "A" <= c <= "Z":
            okProc = True
            blankSpace = False
            while c != "{" and type(c) == type("") and i < len(value) - 1 and okProc:

                if c == " ":
                    blankSpace = True

                if c.isnumeric() and blankSpace:
                    okProc = False

                pos_func += c
                i = i + 1
                c = value[i]

            if pos_func != "" and not pos_func in code and okProc:
                code[pos_func] = value[i:]

        if len(input) < 5:
            input.append(value)

        else:
            for i in range(0, 4):
                input[i+1] = input[i]
            input[0] = value

        if len(output) < 5:
            input.append(value)

        else:
            for i in range(0, 4):
                input[i + 1] = input[i]
            input[0] = value

        print(code)

        lexer = FunxLexer(InputStream(value))

        token_stream = CommonTokenStream(lexer)
        parser = FunxParser(token_stream)

        tree = parser.root()

        eval = TreeVisitor()
        eval.visitRoot(tree)

    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
