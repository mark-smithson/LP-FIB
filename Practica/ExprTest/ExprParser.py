# Generated from Expr.g by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,112,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,2,1,2,3,2,26,8,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,52,8,3,1,4,1,4,1,4,3,4,57,8,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,5,4,77,8,4,10,4,12,4,80,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,3,6,110,8,6,1,6,0,1,8,7,0,2,4,6,8,10,12,0,
        0,121,0,14,1,0,0,0,2,20,1,0,0,0,4,25,1,0,0,0,6,51,1,0,0,0,8,56,1,
        0,0,0,10,81,1,0,0,0,12,109,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,
        1,1,0,0,0,17,19,3,4,2,0,18,17,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,
        0,20,21,1,0,0,0,21,3,1,0,0,0,22,20,1,0,0,0,23,26,3,10,5,0,24,26,
        3,6,3,0,25,23,1,0,0,0,25,24,1,0,0,0,26,5,1,0,0,0,27,28,5,20,0,0,
        28,52,3,8,4,0,29,30,5,15,0,0,30,31,3,12,6,0,31,32,5,18,0,0,32,33,
        3,2,1,0,33,34,5,19,0,0,34,52,1,0,0,0,35,36,5,15,0,0,36,37,3,12,6,
        0,37,38,5,18,0,0,38,39,3,2,1,0,39,40,5,19,0,0,40,41,5,17,0,0,41,
        42,5,18,0,0,42,43,3,2,1,0,43,44,5,19,0,0,44,52,1,0,0,0,45,46,5,16,
        0,0,46,47,3,12,6,0,47,48,5,18,0,0,48,49,3,2,1,0,49,50,5,19,0,0,50,
        52,1,0,0,0,51,27,1,0,0,0,51,29,1,0,0,0,51,35,1,0,0,0,51,45,1,0,0,
        0,52,7,1,0,0,0,53,54,6,4,-1,0,54,57,5,1,0,0,55,57,5,21,0,0,56,53,
        1,0,0,0,56,55,1,0,0,0,57,78,1,0,0,0,58,59,10,8,0,0,59,60,5,7,0,0,
        60,77,3,8,4,8,61,62,10,7,0,0,62,63,5,4,0,0,63,77,3,8,4,8,64,65,10,
        6,0,0,65,66,5,5,0,0,66,77,3,8,4,7,67,68,10,5,0,0,68,69,5,6,0,0,69,
        77,3,8,4,6,70,71,10,4,0,0,71,72,5,2,0,0,72,77,3,8,4,5,73,74,10,3,
        0,0,74,75,5,3,0,0,75,77,3,8,4,4,76,58,1,0,0,0,76,61,1,0,0,0,76,64,
        1,0,0,0,76,67,1,0,0,0,76,70,1,0,0,0,76,73,1,0,0,0,77,80,1,0,0,0,
        78,76,1,0,0,0,78,79,1,0,0,0,79,9,1,0,0,0,80,78,1,0,0,0,81,82,5,21,
        0,0,82,83,5,8,0,0,83,84,3,8,4,0,84,11,1,0,0,0,85,86,3,8,4,0,86,87,
        5,11,0,0,87,88,3,8,4,0,88,110,1,0,0,0,89,90,3,8,4,0,90,91,5,12,0,
        0,91,92,3,8,4,0,92,110,1,0,0,0,93,94,3,8,4,0,94,95,5,13,0,0,95,96,
        3,8,4,0,96,110,1,0,0,0,97,98,3,8,4,0,98,99,5,14,0,0,99,100,3,8,4,
        0,100,110,1,0,0,0,101,102,3,8,4,0,102,103,5,9,0,0,103,104,3,8,4,
        0,104,110,1,0,0,0,105,106,3,8,4,0,106,107,5,10,0,0,107,108,3,8,4,
        0,108,110,1,0,0,0,109,85,1,0,0,0,109,89,1,0,0,0,109,93,1,0,0,0,109,
        97,1,0,0,0,109,101,1,0,0,0,109,105,1,0,0,0,110,13,1,0,0,0,7,20,25,
        51,56,76,78,109
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'", "'<-'", "'='", "'!='", "'<'", "'>'", 
                     "'>='", "'<='", "'if'", "'while'", "'else'", "'{'", 
                     "'}'", "'write'" ]

    symbolicNames = [ "<INVALID>", "NUM", "SUM", "SUB", "MULT", "DIV", "MOD", 
                      "EXP", "ASSIGN", "EQ", "NEQ", "LT", "GT", "GE", "LE", 
                      "IF", "WHILE", "ELSE", "KEYL", "KEYR", "WRITE", "IDVAR", 
                      "WS" ]

    RULE_root = 0
    RULE_block = 1
    RULE_instr = 2
    RULE_statement = 3
    RULE_expr = 4
    RULE_assign = 5
    RULE_condition = 6

    ruleNames =  [ "root", "block", "instr", "statement", "expr", "assign", 
                   "condition" ]

    EOF = Token.EOF
    NUM=1
    SUM=2
    SUB=3
    MULT=4
    DIV=5
    MOD=6
    EXP=7
    ASSIGN=8
    EQ=9
    NEQ=10
    LT=11
    GT=12
    GE=13
    LE=14
    IF=15
    WHILE=16
    ELSE=17
    KEYL=18
    KEYR=19
    WRITE=20
    IDVAR=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.block()
            self.state = 15
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.InstrContext)
            else:
                return self.getTypedRuleContext(ExprParser.InstrContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 3244032) != 0:
                self.state = 17
                self.instr()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(ExprParser.AssignContext,0)


        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_instr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = ExprParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instr)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.assign()
                pass
            elif token in [15, 16, 20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WriteContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(ExprParser.WRITE, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class IfelsestContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)
        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)

        def KEYL(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.KEYL)
            else:
                return self.getToken(ExprParser.KEYL, i)
        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BlockContext)
            else:
                return self.getTypedRuleContext(ExprParser.BlockContext,i)

        def KEYR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.KEYR)
            else:
                return self.getToken(ExprParser.KEYR, i)
        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelsest" ):
                return visitor.visitIfelsest(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)
        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)

        def KEYL(self):
            return self.getToken(ExprParser.KEYL, 0)
        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)

        def KEYR(self):
            return self.getToken(ExprParser.KEYR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class IfstContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)
        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)

        def KEYL(self):
            return self.getToken(ExprParser.KEYL, 0)
        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)

        def KEYR(self):
            return self.getToken(ExprParser.KEYR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfst" ):
                return visitor.visitIfst(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ExprParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(ExprParser.WRITE)
                self.state = 28
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.IfstContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(ExprParser.IF)
                self.state = 30
                self.condition()
                self.state = 31
                self.match(ExprParser.KEYL)
                self.state = 32
                self.block()
                self.state = 33
                self.match(ExprParser.KEYR)
                pass

            elif la_ == 3:
                localctx = ExprParser.IfelsestContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(ExprParser.IF)
                self.state = 36
                self.condition()
                self.state = 37
                self.match(ExprParser.KEYL)
                self.state = 38
                self.block()
                self.state = 39
                self.match(ExprParser.KEYR)
                self.state = 40
                self.match(ExprParser.ELSE)
                self.state = 41
                self.match(ExprParser.KEYL)
                self.state = 42
                self.block()
                self.state = 43
                self.match(ExprParser.KEYR)
                pass

            elif la_ == 4:
                localctx = ExprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(ExprParser.WHILE)
                self.state = 46
                self.condition()
                self.state = 47
                self.match(ExprParser.KEYL)
                self.state = 48
                self.block()
                self.state = 49
                self.match(ExprParser.KEYR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def SUB(self):
            return self.getToken(ExprParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class ModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MOD(self):
            return self.getToken(ExprParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDVAR(self):
            return self.getToken(ExprParser.IDVAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ValueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)


    class SumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def SUM(self):
            return self.getToken(ExprParser.SUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)


    class ExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def EXP(self):
            return self.getToken(ExprParser.EXP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ExprParser.ValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 54
                self.match(ExprParser.NUM)
                pass
            elif token in [21]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(ExprParser.IDVAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExpContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 59
                        self.match(ExprParser.EXP)
                        self.state = 60
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MultContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 62
                        self.match(ExprParser.MULT)
                        self.state = 63
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.DivContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 64
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 65
                        self.match(ExprParser.DIV)
                        self.state = 66
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ModContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 68
                        self.match(ExprParser.MOD)
                        self.state = 69
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.SumContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 70
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 71
                        self.match(ExprParser.SUM)
                        self.state = 72
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.SubContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 73
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 74
                        self.match(ExprParser.SUB)
                        self.state = 75
                        self.expr(4)
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_assign

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssiContext(AssignContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AssignContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDVAR(self):
            return self.getToken(ExprParser.IDVAR, 0)
        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssi" ):
                return visitor.visitAssi(self)
            else:
                return visitor.visitChildren(self)



    def assign(self):

        localctx = ExprParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign)
        try:
            localctx = ExprParser.AssiContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(ExprParser.IDVAR)
            self.state = 82
            self.match(ExprParser.ASSIGN)
            self.state = 83
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LtContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def LT(self):
            return self.getToken(ExprParser.LT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLt" ):
                return visitor.visitLt(self)
            else:
                return visitor.visitChildren(self)


    class LeContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def LE(self):
            return self.getToken(ExprParser.LE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLe" ):
                return visitor.visitLe(self)
            else:
                return visitor.visitChildren(self)


    class NeqContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def NEQ(self):
            return self.getToken(ExprParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeq" ):
                return visitor.visitNeq(self)
            else:
                return visitor.visitChildren(self)


    class EqContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)


    class GtContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def GT(self):
            return self.getToken(ExprParser.GT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGt" ):
                return visitor.visitGt(self)
            else:
                return visitor.visitChildren(self)


    class GeContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def GE(self):
            return self.getToken(ExprParser.GE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGe" ):
                return visitor.visitGe(self)
            else:
                return visitor.visitChildren(self)



    def condition(self):

        localctx = ExprParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ExprParser.LtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.expr(0)
                self.state = 86
                self.match(ExprParser.LT)
                self.state = 87
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.GtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.match(ExprParser.GT)
                self.state = 91
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = ExprParser.GeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(ExprParser.GE)
                self.state = 95
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = ExprParser.LeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.expr(0)
                self.state = 98
                self.match(ExprParser.LE)
                self.state = 99
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = ExprParser.EqContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.expr(0)
                self.state = 102
                self.match(ExprParser.EQ)
                self.state = 103
                self.expr(0)
                pass

            elif la_ == 6:
                localctx = ExprParser.NeqContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.expr(0)
                self.state = 106
                self.match(ExprParser.NEQ)
                self.state = 107
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




