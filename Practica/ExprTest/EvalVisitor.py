if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


def exp(x, y):
    return x ** y


ops = {'+': sum, '-': sub,
       '*': mult, '/': div, '^': exp}



class EvalVisitor(ExprVisitor):
    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[0]))
    def visitExpr(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return int(l[0].getText())
        else:  # len(l) == 3
            if len(l) == 2:
                return self.visit(l[0])
            else:
                return ops[l[1].getText()](self.visit(l[0]),
                                               self.visit(l[2]))