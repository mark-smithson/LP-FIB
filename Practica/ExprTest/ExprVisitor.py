# Generated from Expr.g by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#instr.
    def visitInstr(self, ctx:ExprParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Write.
    def visitWrite(self, ctx:ExprParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Div.
    def visitDiv(self, ctx:ExprParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Sub.
    def visitSub(self, ctx:ExprParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Mod.
    def visitMod(self, ctx:ExprParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Mult.
    def visitMult(self, ctx:ExprParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Var.
    def visitVar(self, ctx:ExprParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Value.
    def visitValue(self, ctx:ExprParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Sum.
    def visitSum(self, ctx:ExprParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Exp.
    def visitExp(self, ctx:ExprParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Assi.
    def visitAssi(self, ctx:ExprParser.AssiContext):
        return self.visitChildren(ctx)



del ExprParser