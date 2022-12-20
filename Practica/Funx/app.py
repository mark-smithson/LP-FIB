from flask import Flask, render_template, request

from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from TreeVisitor import TreeVisitor

app = Flask(__name__)

funcnames = []

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
        funcname = ""

        i = 0
        c = value[i]

        # Function declaration or invoke
        if "A" <= c <= "Z":
            okProc = True
            blankSpace = False
            while c != "{" and i < len(value) - 1 and okProc:
                if c == " ":
                    blankSpace = True

                if c.isnumeric() and blankSpace:
                    okProc = False

                pos_func += c
                i = i + 1
                c = value[i]

            print("HOLA")
            if pos_func != "" and not pos_func in code and okProc:
                j = 0

                while pos_func[j] != " " and j < len(pos_func):
                    funcname += pos_func[j]
                    j += 1

                if funcname not in funcnames:
                    code[pos_func] = value[i:]
                    funcnames.append(funcname)

        if len(input) < 5:
            input.append(value)

        else:
            for i in range(0, 4):
                input[i] = input[i + 1]
            input[len(input) - 1] = value

        print(code)
        print(funcnames)
        print("INP/OUT")
        print(input)
        lexer = FunxLexer(InputStream(value))

        token_stream = CommonTokenStream(lexer)
        parser = FunxParser(token_stream)

        tree = parser.root()

        eval = TreeVisitor()
        valO = eval.visitRoot(tree)

        if len(output) < 5:
            output.append(valO)

        else:
            for i in range(0, 4):
                output[i] = output[i + 1]
            output[len(output) - 1] = valO
        print(output)


    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
