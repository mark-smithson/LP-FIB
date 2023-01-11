all:
	antlr4 -Dlanguage=Python3 -no-listener -visitor funx.g4
clean:
	rm -f funxLexer.py
	rm -f funxParser.py
	rm -f funxVisitor.py
	rm -f *.interp
	rm -f *.tokens
	rm -rf __pycache__