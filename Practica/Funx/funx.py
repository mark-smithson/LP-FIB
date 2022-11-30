from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from TreeVisitor import TreeVisitor

print("Welcome to Funx!: ")

input_stream = StdinStream()
lexer = FunxLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = FunxParser(token_stream)
tree = parser.root()

eval = TreeVisitor()
eval.visitRoot(tree)