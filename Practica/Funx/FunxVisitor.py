# Generated from Funx.g by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
else:
    from FunxParser import FunxParser

# This class defines a complete generic visitor for a parse tree produced by FunxParser.

class FunxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FunxParser#root.
    def visitRoot(self, ctx:FunxParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#block.
    def visitBlock(self, ctx:FunxParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#instr.
    def visitInstr(self, ctx:FunxParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#CreateFunc.
    def visitCreateFunc(self, ctx:FunxParser.CreateFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#InvFunc.
    def visitInvFunc(self, ctx:FunxParser.InvFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#ParamsCreateFunc.
    def visitParamsCreateFunc(self, ctx:FunxParser.ParamsCreateFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#ParamsInvFunc.
    def visitParamsInvFunc(self, ctx:FunxParser.ParamsInvFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Write.
    def visitWrite(self, ctx:FunxParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Ifst.
    def visitIfst(self, ctx:FunxParser.IfstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Ifelsest.
    def visitIfelsest(self, ctx:FunxParser.IfelsestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#While.
    def visitWhile(self, ctx:FunxParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Div.
    def visitDiv(self, ctx:FunxParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Sub.
    def visitSub(self, ctx:FunxParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Mod.
    def visitMod(self, ctx:FunxParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Mult.
    def visitMult(self, ctx:FunxParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Var.
    def visitVar(self, ctx:FunxParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Value.
    def visitValue(self, ctx:FunxParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Sum.
    def visitSum(self, ctx:FunxParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#ParentExp.
    def visitParentExp(self, ctx:FunxParser.ParentExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Exp.
    def visitExp(self, ctx:FunxParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#VarFunc.
    def visitVarFunc(self, ctx:FunxParser.VarFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Assi.
    def visitAssi(self, ctx:FunxParser.AssiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Lt.
    def visitLt(self, ctx:FunxParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Gt.
    def visitGt(self, ctx:FunxParser.GtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Ge.
    def visitGe(self, ctx:FunxParser.GeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Le.
    def visitLe(self, ctx:FunxParser.LeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Eq.
    def visitEq(self, ctx:FunxParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Neq.
    def visitNeq(self, ctx:FunxParser.NeqContext):
        return self.visitChildren(ctx)



del FunxParser