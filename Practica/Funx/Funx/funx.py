from flask import Flask, render_template, request

from antlr4 import *
from funxLexer import funxLexer
from funxParser import funxParser

if __name__ is not None and "." in __name__:
    from .funxParser import funxParser
    from .funxVisitor import funxVisitor
else:
    from funxParser import funxParser
    from funxVisitor import funxVisitor


class TreeVisitor(funxVisitor):
    symtable = [{}]
    functable = {}

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        val = self.visit(l[0])
        print(val)
        return val


    def visitBlock(self, ctx):
        l = list(ctx.getChildren())
        if len(l) > 0:
            res_i = self.visit(l[0])
            if res_i is None:
                return self.visit(l[1])
            else:
                return res_i
        return None

    def visitWrite(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[1]))
        return self.visit(l[1])

    def visitWhile(self, ctx):
        l = list(ctx.getChildren())
        while self.visit(l[1]):
            res = self.visit(l[3])
            if res != None:
                return res
        return None

    def visitFor(self, ctx):
        l = list(ctx.getChildren())
        self.visit(l[1])

        while self.visit(l[3]):
            res = self.visit(l[7])
            if res != None:
                return res
            self.visit(l[5])

        return None


    def visitCreateFunc(self, ctx):
        l = list(ctx.getChildren())
        procName = l[0].getText()

        if procName in self.functable:
            raise Exception("Exception: " + procName + " it already exists")

        params = self.visit(l[1])
        self.functable[procName] = [l[3], params]

    # Visit a parse tree produced by FunxParser#InvokFunc.
    def visitInvokFunc(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0])

    # Visit a parse tree produced by ExprParser#InvFunc.
    def visitInvFunc(self, ctx):
        l = list(ctx.getChildren())
        func = l[0].getText()
        if func not in self.functable:
            raise Exception("Exception: " + func + " does not exists")

        selfparams = self.visit(l[1])
        proc = self.functable[func]
        code = proc[0]
        params = proc[1]
        self.symtable.append({})

        if len(selfparams) != len(params):
            raise Exception("Exception: " + func + " does not have the same amount of parameters")

        for i in range(0, len(params)):
            self.symtable[-1][params[i]] = selfparams[i]

        res = self.visit(code)
        self.symtable.pop()

        return res

    # Visit a parse tree produced by FunxParser#CreateArr.
    def visitCreateArr(self, ctx):
        l = list(ctx.getChildren())
        els = self.visit(l[3])
        self.symtable[-1][l[0].getText()] = els


    # Visit a parse tree produced by FunxParser#ParamsArr.
    def visitParamsArr(self, ctx):
        l = list(ctx.getChildren())
        els = []
        for child in l:
            elem = self.visit(child)
            if elem is None:
                raise Exception("Exception: Wrong parameters in list creation")
            else:
                els.append(elem)

        return els


    # Visit a parse tree produced by FunxParser#AppendArr.
    def visitAppendArr(self, ctx):
        l = list(ctx.getChildren())
        id = l[0].getText()
        if id not in self.symtable[-1]:
            raise Exception("Exception: " + id + " does not exist")

        elem = self.visit(l[2])
        self.symtable[-1][id].append(elem)

    def visitPopArr(self, ctx):
        l = list(ctx.getChildren())
        id = l[1].getText()

        if id not in self.symtable[-1]:
            raise Exception("Exception: " + id + " does not exist")
        if len(self.symtable[-1][id]) == 0:
            raise Exception("Exception: list is empty")

        self.symtable[-1][id].pop(len(self.symtable[-1][id]) - 1)



    # Visit a parse tree produced by FunxParser#LenArr.
    def visitLenArr(self, ctx):
        l = list(ctx.getChildren())
        id = l[2].getText()

        if id not in self.symtable[-1]:
            raise Exception("Exception: " + id + " does not exist")

        l = self.symtable[-1][id]
        if isinstance(l, list):
            return len(l)
        else:
            raise Exception("Exception: " + id + " is not a list")

    def visitAccArr(self, ctx):
        l = list(ctx.getChildren())
        id = l[0].getText()
        if id not in self.symtable[-1]:
            raise Exception("Exception: " + id + " does not exist")
        i = self.visit(l[2])

        if len(self.symtable[-1][id]) <= i:
            raise Exception("Exception: " + self.symtable[-1][id] + "is out of range of list index")

        return self.symtable[-1][id][i]

    def visitParamsCreateFunc(self, ctx):
        l = list(ctx.getChildren())
        params = [param.getText() for param in l]

        return params

    def visitParamsInvFunc(self, ctx):
        l = list(ctx.getChildren())
        params = [self.visit(param) for param in l]

        return params

    def visitIfst(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            return self.visit(l[3])
        return None

    def visitIfelsest(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            return self.visit(l[3])
        else:
            return self.visit(l[7])

    def visitDiv(self, ctx):
        l = list(ctx.getChildren())
        if l[2] == 0:
            raise Exception("Exception: Attempted to divide by Zero")
        else:
            return self.visit(l[0]) // self.visit(l[2])

    def visitMod(self, ctx):
        l = list(ctx.getChildren())

        if l[2] == 0:
            raise Exception("Exceptionr: Attempted to divide by Zero")
        else:
            return self.visit(l[0]) % self.visit(l[2])

    # Visit a parse tree produced by ExprParser#Sub.
    def visitSub(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) - self.visit(l[2])

    # Visit a parse tree produced by ExprParser#Mult.
    def visitMult(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) * self.visit(l[2])

    def visitVar(self, ctx):
        l = list(ctx.getChildren())
        return self.symtable[-1][l[0].getText()]

    # Visit a parse tree produced by ExprParser#Value.
    def visitValue(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    # Visit a parse tree produced by ExprParser#Sum.
    def visitSum(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) + self.visit(l[2])

    def visitNeg(self, ctx):
        l = list(ctx.getChildren())
        return (-1)*self.visit(l[1])

    def visitParentExp(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    # Visit a parse tree produced by ExprParser#Exp.
    def visitExp(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) ** self.visit(l[2])

    def visitVarFunc(self, ctx):
        l = list(ctx.getChildren())
        return int(self.functable[l[0].getText()][0].getText())

    def visitAssi(self, ctx):
        l = list(ctx.getChildren())
        self.symtable[-1][l[0].getText()] = self.visit(l[2])
        return None

    def visitLt(self, ctx):
        l = list(ctx.getChildren())
        return 1 if self.visit(l[0]) < self.visit(l[2]) else 0


    # Visit a parse tree produced by ExprParser#Gt.
    def visitGt(self, ctx):
        l = list(ctx.getChildren())
        return 1 if self.visit(l[0]) > self.visit(l[2]) else 0

    # Visit a parse tree produced by ExprParser#Ge.
    def visitGe(self, ctx):
        l = list(ctx.getChildren())
        return 1 if self.visit(l[0]) >= self.visit(l[2]) else 0

    # Visit a parse tree produced by ExprParser#Le.
    def visitLe(self, ctx):
        l = list(ctx.getChildren())
        return 1 if self.visit(l[0]) <= self.visit(l[2]) else 0

    # Visit a parse tree produced by ExprParser#Eq.
    def visitEq(self, ctx):
        l = list(ctx.getChildren())
        return 1 if self.visit(l[0]) == self.visit(l[2]) else 0

    # Visit a parse tree produced by ExprParser#Neq.
    def visitNeq(self, ctx):
        l = list(ctx.getChildren())
        return 1 if self.visit(l[0]) != self.visit(l[2]) else 0


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

        # Comment
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

        lexer = funxLexer(InputStream(value))

        token_stream = CommonTokenStream(lexer)
        parser = funxParser(token_stream)

        tree = parser.root()

        eval = TreeVisitor()

        valO = None
        try:
            valO = eval.visitRoot(tree)
        except Exception as e:
            valO = e

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
