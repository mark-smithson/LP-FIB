if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor


class TreeVisitor(FunxVisitor):

    symtable = [{}]
    functable = {}

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[0]))

    def visitWrite(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[1]))

    def visitWhile(self, ctx):
        l = list(ctx.getChildren())
        while (self.visit(l[1])):
            self.visit(l[3])
    def visitCreateFunc(self, ctx):
        l = list(ctx.getChildren())
        procName = l[0].getText()

        if procName in self.functable:
            raise Exception(procName + " it already exists")

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
            raise Exception(func + " does not exists")

        selfparams = self.visit(l[1])
        proc = self.functable[func]
        code = proc[0]
        params = proc[1]
        self.symtable.append({})

        if len(selfparams) != len(params):
            raise Exception(func + " does not have the same amount of parametres")

        for i in range(0, len(params)):
            self.symtable[-1][params[i]] = selfparams[i]

        res = self.visit(code)
        self.symtable.pop()

        return res

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

    def visitIfelsest(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            return self.visit(l[3])
        else:
            return self.visit(l[7])

    def visitDiv(self, ctx):
        l = list(ctx.getChildren())

        if l[2] == 0:
            raise Exception("Math error: Attempted to divide by Zero")
        else:
            return self.visit(l[0])/self.visit(l[2])

    def visitMod(self, ctx):
        l = list(ctx.getChildren())

        if l[2] == 0:
            raise Exception("Math error: Attempted to divide by Zero")
        else:
            return self.visit(l[0])%self.visit(l[2])

    # Visit a parse tree produced by ExprParser#Sub.
    def visitSub(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) - self.visit(l[2])

    # Visit a parse tree produced by ExprParser#Mult.
    def visitMult(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0])*self.visit(l[2])

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

    def visitParentExp(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    # Visit a parse tree produced by ExprParser#Exp.
    def visitExp(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0])**self.visit(l[2])

    def visitVarFunc(self, ctx):
        l = list(ctx.getChildren())
        # print(self.functable[l[0].getText()][0].getText())
        return int(self.functable[l[0].getText()][0].getText())

    def visitAssi(self, ctx):
        l = list(ctx.getChildren())
        self.symtable[-1][l[0].getText()] = self.visit(l[2])

    def visitLt(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) < self.visit(l[2])

    # Visit a parse tree produced by ExprParser#Gt.
    def visitGt(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) > self.visit(l[2])

    # Visit a parse tree produced by ExprParser#Ge.
    def visitGe(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) >= self.visit(l[2])

    # Visit a parse tree produced by ExprParser#Le.
    def visitLe(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) <= self.visit(l[2])

    # Visit a parse tree produced by ExprParser#Eq.
    def visitEq(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) == self.visit(l[2])

    # Visit a parse tree produced by ExprParser#Neq.
    def visitNeq(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) != self.visit(l[2])
