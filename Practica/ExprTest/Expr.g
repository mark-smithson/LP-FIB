grammar Expr;

root : block EOF ;

block: instr* ;

instr : assign
    | statement
    ;

statement: WRITE expr # Write;

expr : <assoc=right> expr EXP expr # Exp
    | expr MULT expr # Mult
    | expr DIV expr # Div
    | expr MOD expr # Mod
    | expr SUM expr # Sum
    | expr SUB expr # Sub
    | NUM # Value
    | IDVAR # Var
    ;

assign : IDVAR ASSIGN expr # Assi ;


NUM : [0-9]+ ;
SUM : '+' ;
SUB : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
EXP : '^' ;
ASSIGN: '<-' ;
EQ: '=' ;
NEQ: '!=' ;
LT: '<' ;
GT: '>' ;
GE: '>=' ;
LE: '<=' ;
WRITE : 'write' ;
IDVAR : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
WS : [ \n]+ -> skip ;