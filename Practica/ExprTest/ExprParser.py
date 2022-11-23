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
        4,1,17,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,2,1,2,3,2,24,8,2,1,3,1,3,
        1,3,1,4,1,4,1,4,3,4,32,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,52,8,4,10,4,12,4,55,9,4,1,
        5,1,5,1,5,1,5,1,5,0,1,8,6,0,2,4,6,8,10,0,0,63,0,12,1,0,0,0,2,18,
        1,0,0,0,4,23,1,0,0,0,6,25,1,0,0,0,8,31,1,0,0,0,10,56,1,0,0,0,12,
        13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,17,3,4,2,0,16,15,1,0,0,
        0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,3,1,0,0,0,20,18,1,
        0,0,0,21,24,3,10,5,0,22,24,3,6,3,0,23,21,1,0,0,0,23,22,1,0,0,0,24,
        5,1,0,0,0,25,26,5,15,0,0,26,27,3,8,4,0,27,7,1,0,0,0,28,29,6,4,-1,
        0,29,32,5,1,0,0,30,32,5,16,0,0,31,28,1,0,0,0,31,30,1,0,0,0,32,53,
        1,0,0,0,33,34,10,8,0,0,34,35,5,7,0,0,35,52,3,8,4,8,36,37,10,7,0,
        0,37,38,5,4,0,0,38,52,3,8,4,8,39,40,10,6,0,0,40,41,5,5,0,0,41,52,
        3,8,4,7,42,43,10,5,0,0,43,44,5,6,0,0,44,52,3,8,4,6,45,46,10,4,0,
        0,46,47,5,2,0,0,47,52,3,8,4,5,48,49,10,3,0,0,49,50,5,3,0,0,50,52,
        3,8,4,4,51,33,1,0,0,0,51,36,1,0,0,0,51,39,1,0,0,0,51,42,1,0,0,0,
        51,45,1,0,0,0,51,48,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,
        0,0,0,54,9,1,0,0,0,55,53,1,0,0,0,56,57,5,16,0,0,57,58,5,8,0,0,58,
        59,3,8,4,0,59,11,1,0,0,0,5,18,23,31,51,53
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'", "'<-'", "'='", "'!='", "'<'", "'>'", 
                     "'>='", "'<='", "'write'" ]

    symbolicNames = [ "<INVALID>", "NUM", "SUM", "SUB", "MULT", "DIV", "MOD", 
                      "EXP", "ASSIGN", "EQ", "NEQ", "LT", "GT", "GE", "LE", 
                      "WRITE", "IDVAR", "WS" ]

    RULE_root = 0
    RULE_block = 1
    RULE_instr = 2
    RULE_statement = 3
    RULE_expr = 4
    RULE_assign = 5

    ruleNames =  [ "root", "block", "instr", "statement", "expr", "assign" ]

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
    WRITE=15
    IDVAR=16
    WS=17

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
            self.state = 12
            self.block()
            self.state = 13
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
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 15
                self.instr()
                self.state = 20
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
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.assign()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
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



    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            localctx = ExprParser.WriteContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(ExprParser.WRITE)
            self.state = 26
            self.expr(0)
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
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ExprParser.ValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 29
                self.match(ExprParser.NUM)
                pass
            elif token in [16]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(ExprParser.IDVAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExpContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 34
                        self.match(ExprParser.EXP)
                        self.state = 35
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MultContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 37
                        self.match(ExprParser.MULT)
                        self.state = 38
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.DivContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 40
                        self.match(ExprParser.DIV)
                        self.state = 41
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ModContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 43
                        self.match(ExprParser.MOD)
                        self.state = 44
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.SumContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 46
                        self.match(ExprParser.SUM)
                        self.state = 47
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.SubContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 49
                        self.match(ExprParser.SUB)
                        self.state = 50
                        self.expr(4)
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            self.state = 56
            self.match(ExprParser.IDVAR)
            self.state = 57
            self.match(ExprParser.ASSIGN)
            self.state = 58
            self.expr(0)
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
         




