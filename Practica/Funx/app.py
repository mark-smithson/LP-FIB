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

inputC = 0
outputC = 0

inpL = []
outL = []


@app.route("/", methods=['POST', 'GET'])
def home():
    global code
    global inputC
    global outputC

    result = request.form

    for key, valueAll in result.items():
        i = 0

        # Comment of a function
        if valueAll[i] == '#':
            while valueAll[i] != '\n':
                i += 1
            i -= 1

        valueAll = valueAll.replace('\r', '')
        valueAll = valueAll.replace('\n', '')

        value = valueAll[i:]

        pos_func = ""
        funcname = ""

        i = 0
        c = value[i]

        # Function declaration or invoke
        if "A" <= c <= "Z":
            okProc = True
            blankSpace = False
            nonK = True
            while c != "{" and i < len(value) - 1 and okProc:
                if c == " ":
                    blankSpace = True

                if c.isnumeric() and blankSpace:
                    okProc = False

                pos_func += c
                i = i + 1
                c = value[i]

            nonK = (c == '{')
            if pos_func != "" and not pos_func in code and okProc and nonK:
                j = 0

                while j < len(pos_func) and pos_func[j] != " ":
                    funcname += pos_func[j]
                    j += 1

                if funcname not in funcnames:
                    code[pos_func] = value[i:]
                    funcnames.append(funcname)

        inputC += 1
        outputC += 1

        if len(input) < 5:
            input.append(valueAll)
            inpL.append(inputC)
        else:
            for i in range(0, 4):
                input[i] = input[i + 1]
                inpL[i] = inpL[i + 1]
            input[len(input) - 1] = valueAll
            inpL[len(inpL) - 1] = inputC

        #print(code)
        #print(funcnames)
        #print("INP/OUT")
        #print(inpL)
        lexer = FunxLexer(InputStream(value))

        token_stream = CommonTokenStream(lexer)
        parser = FunxParser(token_stream)

        tree = parser.root()

        eval = TreeVisitor()
        valO = eval.visitRoot(tree)
        #print(eval)
        if len(output) < 5:
            output.append(valO)
            outL.append(outputC)
        else:
            for i in range(0, 4):
                output[i] = output[i + 1]
                outL[i] = outL[i+1]
            output[len(output) - 1] = valO
            outL[len(outL) - 1] = outputC


    return render_template("base.html", funcname=code, InpOut=zip(input, output, inpL))


if __name__ == "__main__":
    app.run(debug=True)
