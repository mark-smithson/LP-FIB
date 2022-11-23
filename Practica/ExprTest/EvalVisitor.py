if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):

    symtable = {}
    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[0]))


    def visitWrite(self, ctx):
        l = list(ctx.getChildren())
        print(self.symtable[l[1].getText()])

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
        return self.symtable[l[0].getText()]

    # Visit a parse tree produced by ExprParser#Value.
    def visitValue(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())


    # Visit a parse tree produced by ExprParser#Sum.
    def visitSum(self, ctx):
        l = list(ctx.getChildren())

        return self.visit(l[0]) + self.visit(l[2])


    # Visit a parse tree produced by ExprParser#Exp.
    def visitExp(self, ctx):
        l = list(ctx.getChildren())

        return self.visit(l[0])**self.visit(l[2])

    def visitAssi(self, ctx):
        l = list(ctx.getChildren())
        self.symtable[l[0].getText()] = self.visit(l[2])
