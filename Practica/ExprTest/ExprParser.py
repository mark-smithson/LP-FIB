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
        4,1,25,148,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,5,1,27,8,1,10,
        1,12,1,30,9,1,1,2,1,2,1,2,1,2,1,2,3,2,37,8,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,5,5,5,49,8,5,10,5,12,5,52,9,5,1,6,5,6,55,8,6,10,
        6,12,6,58,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,84,8,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,93,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,113,8,8,10,8,12,8,116,
        9,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,146,8,10,1,10,0,1,16,11,0,2,4,6,8,10,12,14,16,18,
        20,0,0,159,0,22,1,0,0,0,2,28,1,0,0,0,4,36,1,0,0,0,6,38,1,0,0,0,8,
        44,1,0,0,0,10,50,1,0,0,0,12,56,1,0,0,0,14,83,1,0,0,0,16,92,1,0,0,
        0,18,117,1,0,0,0,20,145,1,0,0,0,22,23,3,2,1,0,23,24,5,0,0,1,24,1,
        1,0,0,0,25,27,3,4,2,0,26,25,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,
        28,29,1,0,0,0,29,3,1,0,0,0,30,28,1,0,0,0,31,37,3,18,9,0,32,37,3,
        14,7,0,33,37,3,6,3,0,34,37,3,8,4,0,35,37,3,16,8,0,36,31,1,0,0,0,
        36,32,1,0,0,0,36,33,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,5,1,0,
        0,0,38,39,5,24,0,0,39,40,3,10,5,0,40,41,5,18,0,0,41,42,3,2,1,0,42,
        43,5,19,0,0,43,7,1,0,0,0,44,45,5,24,0,0,45,46,3,12,6,0,46,9,1,0,
        0,0,47,49,5,23,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,
        51,1,0,0,0,51,11,1,0,0,0,52,50,1,0,0,0,53,55,3,16,8,0,54,53,1,0,
        0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,13,1,0,0,0,58,56,
        1,0,0,0,59,60,5,22,0,0,60,84,3,16,8,0,61,62,5,15,0,0,62,63,3,20,
        10,0,63,64,5,18,0,0,64,65,3,2,1,0,65,66,5,19,0,0,66,84,1,0,0,0,67,
        68,5,15,0,0,68,69,3,20,10,0,69,70,5,18,0,0,70,71,3,2,1,0,71,72,5,
        19,0,0,72,73,5,17,0,0,73,74,5,18,0,0,74,75,3,2,1,0,75,76,5,19,0,
        0,76,84,1,0,0,0,77,78,5,16,0,0,78,79,3,20,10,0,79,80,5,18,0,0,80,
        81,3,2,1,0,81,82,5,19,0,0,82,84,1,0,0,0,83,59,1,0,0,0,83,61,1,0,
        0,0,83,67,1,0,0,0,83,77,1,0,0,0,84,15,1,0,0,0,85,86,6,8,-1,0,86,
        87,5,20,0,0,87,88,3,16,8,0,88,89,5,21,0,0,89,93,1,0,0,0,90,93,5,
        1,0,0,91,93,5,23,0,0,92,85,1,0,0,0,92,90,1,0,0,0,92,91,1,0,0,0,93,
        114,1,0,0,0,94,95,10,8,0,0,95,96,5,7,0,0,96,113,3,16,8,8,97,98,10,
        7,0,0,98,99,5,4,0,0,99,113,3,16,8,8,100,101,10,6,0,0,101,102,5,5,
        0,0,102,113,3,16,8,7,103,104,10,5,0,0,104,105,5,6,0,0,105,113,3,
        16,8,6,106,107,10,4,0,0,107,108,5,2,0,0,108,113,3,16,8,5,109,110,
        10,3,0,0,110,111,5,3,0,0,111,113,3,16,8,4,112,94,1,0,0,0,112,97,
        1,0,0,0,112,100,1,0,0,0,112,103,1,0,0,0,112,106,1,0,0,0,112,109,
        1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,17,1,
        0,0,0,116,114,1,0,0,0,117,118,5,23,0,0,118,119,5,8,0,0,119,120,3,
        16,8,0,120,19,1,0,0,0,121,122,3,16,8,0,122,123,5,11,0,0,123,124,
        3,16,8,0,124,146,1,0,0,0,125,126,3,16,8,0,126,127,5,12,0,0,127,128,
        3,16,8,0,128,146,1,0,0,0,129,130,3,16,8,0,130,131,5,13,0,0,131,132,
        3,16,8,0,132,146,1,0,0,0,133,134,3,16,8,0,134,135,5,14,0,0,135,136,
        3,16,8,0,136,146,1,0,0,0,137,138,3,16,8,0,138,139,5,9,0,0,139,140,
        3,16,8,0,140,146,1,0,0,0,141,142,3,16,8,0,142,143,5,10,0,0,143,144,
        3,16,8,0,144,146,1,0,0,0,145,121,1,0,0,0,145,125,1,0,0,0,145,129,
        1,0,0,0,145,133,1,0,0,0,145,137,1,0,0,0,145,141,1,0,0,0,146,21,1,
        0,0,0,9,28,36,50,56,83,92,112,114,145
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'", "'<-'", "'='", "'!='", "'<'", "'>'", 
                     "'>='", "'<='", "'if'", "'while'", "'else'", "'{'", 
                     "'}'", "'('", "')'", "'write'" ]

    symbolicNames = [ "<INVALID>", "NUM", "SUM", "SUB", "MULT", "DIV", "MOD", 
                      "EXP", "ASSIGN", "EQ", "NEQ", "LT", "GT", "GE", "LE", 
                      "IF", "WHILE", "ELSE", "KEYL", "KEYR", "LP", "RP", 
                      "WRITE", "IDVAR", "IDFUNC", "WS" ]

    RULE_root = 0
    RULE_block = 1
    RULE_instr = 2
    RULE_createFunction = 3
    RULE_invokeFunction = 4
    RULE_paramsCreateFunction = 5
    RULE_paramsInvokeFunction = 6
    RULE_statement = 7
    RULE_expr = 8
    RULE_assign = 9
    RULE_condition = 10

    ruleNames =  [ "root", "block", "instr", "createFunction", "invokeFunction", 
                   "paramsCreateFunction", "paramsInvokeFunction", "statement", 
                   "expr", "assign", "condition" ]

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
    LP=20
    RP=21
    WRITE=22
    IDVAR=23
    IDFUNC=24
    WS=25

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
            self.state = 22
            self.block()
            self.state = 23
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
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 30507010) != 0:
                self.state = 25
                self.instr()
                self.state = 30
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


        def createFunction(self):
            return self.getTypedRuleContext(ExprParser.CreateFunctionContext,0)


        def invokeFunction(self):
            return self.getTypedRuleContext(ExprParser.InvokeFunctionContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


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
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.createFunction()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.invokeFunction()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_createFunction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CreateFuncContext(CreateFunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.CreateFunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDFUNC(self):
            return self.getToken(ExprParser.IDFUNC, 0)
        def paramsCreateFunction(self):
            return self.getTypedRuleContext(ExprParser.ParamsCreateFunctionContext,0)

        def KEYL(self):
            return self.getToken(ExprParser.KEYL, 0)
        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)

        def KEYR(self):
            return self.getToken(ExprParser.KEYR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateFunc" ):
                return visitor.visitCreateFunc(self)
            else:
                return visitor.visitChildren(self)



    def createFunction(self):

        localctx = ExprParser.CreateFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_createFunction)
        try:
            localctx = ExprParser.CreateFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ExprParser.IDFUNC)
            self.state = 39
            self.paramsCreateFunction()
            self.state = 40
            self.match(ExprParser.KEYL)
            self.state = 41
            self.block()
            self.state = 42
            self.match(ExprParser.KEYR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvokeFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_invokeFunction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InvFuncContext(InvokeFunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InvokeFunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDFUNC(self):
            return self.getToken(ExprParser.IDFUNC, 0)
        def paramsInvokeFunction(self):
            return self.getTypedRuleContext(ExprParser.ParamsInvokeFunctionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvFunc" ):
                return visitor.visitInvFunc(self)
            else:
                return visitor.visitChildren(self)



    def invokeFunction(self):

        localctx = ExprParser.InvokeFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_invokeFunction)
        try:
            localctx = ExprParser.InvFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ExprParser.IDFUNC)
            self.state = 45
            self.paramsInvokeFunction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsCreateFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_paramsCreateFunction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParamsCreateFuncContext(ParamsCreateFunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ParamsCreateFunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDVAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.IDVAR)
            else:
                return self.getToken(ExprParser.IDVAR, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamsCreateFunc" ):
                return visitor.visitParamsCreateFunc(self)
            else:
                return visitor.visitChildren(self)



    def paramsCreateFunction(self):

        localctx = ExprParser.ParamsCreateFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramsCreateFunction)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.ParamsCreateFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 47
                self.match(ExprParser.IDVAR)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsInvokeFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_paramsInvokeFunction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParamsInvFuncContext(ParamsInvokeFunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ParamsInvokeFunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamsInvFunc" ):
                return visitor.visitParamsInvFunc(self)
            else:
                return visitor.visitChildren(self)



    def paramsInvokeFunction(self):

        localctx = ExprParser.ParamsInvokeFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramsInvokeFunction)
        try:
            localctx = ExprParser.ParamsInvFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 53
                    self.expr(0) 
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ExprParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(ExprParser.WRITE)
                self.state = 60
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.IfstContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(ExprParser.IF)
                self.state = 62
                self.condition()
                self.state = 63
                self.match(ExprParser.KEYL)
                self.state = 64
                self.block()
                self.state = 65
                self.match(ExprParser.KEYR)
                pass

            elif la_ == 3:
                localctx = ExprParser.IfelsestContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.match(ExprParser.IF)
                self.state = 68
                self.condition()
                self.state = 69
                self.match(ExprParser.KEYL)
                self.state = 70
                self.block()
                self.state = 71
                self.match(ExprParser.KEYR)
                self.state = 72
                self.match(ExprParser.ELSE)
                self.state = 73
                self.match(ExprParser.KEYL)
                self.state = 74
                self.block()
                self.state = 75
                self.match(ExprParser.KEYR)
                pass

            elif la_ == 4:
                localctx = ExprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.match(ExprParser.WHILE)
                self.state = 78
                self.condition()
                self.state = 79
                self.match(ExprParser.KEYL)
                self.state = 80
                self.block()
                self.state = 81
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


    class ParentExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LP(self):
            return self.getToken(ExprParser.LP, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def RP(self):
            return self.getToken(ExprParser.RP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentExp" ):
                return visitor.visitParentExp(self)
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = ExprParser.ParentExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 86
                self.match(ExprParser.LP)
                self.state = 87
                self.expr(0)
                self.state = 88
                self.match(ExprParser.RP)
                pass
            elif token in [1]:
                localctx = ExprParser.ValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.match(ExprParser.NUM)
                pass
            elif token in [23]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.match(ExprParser.IDVAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 112
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExpContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 95
                        self.match(ExprParser.EXP)
                        self.state = 96
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MultContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 98
                        self.match(ExprParser.MULT)
                        self.state = 99
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.DivContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 101
                        self.match(ExprParser.DIV)
                        self.state = 102
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ModContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 104
                        self.match(ExprParser.MOD)
                        self.state = 105
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.SumContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 106
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 107
                        self.match(ExprParser.SUM)
                        self.state = 108
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.SubContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 109
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 110
                        self.match(ExprParser.SUB)
                        self.state = 111
                        self.expr(4)
                        pass

             
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_assign)
        try:
            localctx = ExprParser.AssiContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ExprParser.IDVAR)
            self.state = 118
            self.match(ExprParser.ASSIGN)
            self.state = 119
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
        self.enterRule(localctx, 20, self.RULE_condition)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = ExprParser.LtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.expr(0)
                self.state = 122
                self.match(ExprParser.LT)
                self.state = 123
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.GtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.expr(0)
                self.state = 126
                self.match(ExprParser.GT)
                self.state = 127
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = ExprParser.GeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.expr(0)
                self.state = 130
                self.match(ExprParser.GE)
                self.state = 131
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = ExprParser.LeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.expr(0)
                self.state = 134
                self.match(ExprParser.LE)
                self.state = 135
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = ExprParser.EqContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.expr(0)
                self.state = 138
                self.match(ExprParser.EQ)
                self.state = 139
                self.expr(0)
                pass

            elif la_ == 6:
                localctx = ExprParser.NeqContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                self.expr(0)
                self.state = 142
                self.match(ExprParser.NEQ)
                self.state = 143
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
        self._predicates[8] = self.expr_sempred
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
         




