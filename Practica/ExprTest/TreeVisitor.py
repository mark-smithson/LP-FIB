if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor


class TreeVisitor(ExprVisitor):
    def __init__(self):
        self.nivell = 0

    def visitWrite(self, ctx:ExprParser.WriteContext):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'WRITE -> ' + l[1].getText())
        self.nivell += 1
        self.visit(l[1])
        self.nivell -= 1

    def visitDiv(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'DIV(/)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1


    def visitMod(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'MOD(%)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1


    # Visit a parse tree produced by ExprParser#Sub.
    def visitSub(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'SUB(-)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1


    # Visit a parse tree produced by ExprParser#Mult.
    def visitMult(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'MULT(*)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1


    def visitVar(self, ctx):
        l = list(ctx.getChildren())
        print("  " * self.nivell +
              ExprParser.symbolicNames[l[0].getSymbol().type] +
              '(' + l[0].getText() + ')')

    # Visit a parse tree produced by ExprParser#Value.
    def visitValue(self, ctx):
        l = list(ctx.getChildren())
        print("  " * self.nivell +
              ExprParser.symbolicNames[l[0].getSymbol().type] +
              '(' + l[0].getText() + ')')


    # Visit a parse tree produced by ExprParser#Sum.
    def visitSum(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'SUM(+)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1


    # Visit a parse tree produced by ExprParser#Exp.
    def visitExp(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'EXP(^)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitAssi(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'ASSIGN(<-)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitLt(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'LT(<)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    # Visit a parse tree produced by ExprParser#Gt.
    def visitGt(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'GT(>)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    # Visit a parse tree produced by ExprParser#Ge.
    def visitGe(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'GE(>=)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    # Visit a parse tree produced by ExprParser#Le.
    def visitLe(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'LE(<=)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    # Visit a parse tree produced by ExprParser#Eq.
    def visitEq(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'EQ(=)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    # Visit a parse tree produced by ExprParser#Neq.
    def visitNeq(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'NEQ(!=)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

