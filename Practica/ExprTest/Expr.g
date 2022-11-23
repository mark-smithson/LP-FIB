grammar Expr;

root : block EOF ;

block: instr* ;

instr : assign
    | statement
    ;

statement : WRITE expr # Write
    | IF condition KEYL block KEYR # Ifst
    | IF condition KEYL block KEYR ELSE KEYL block KEYR # Ifelsest
    ;

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
condition : expr LT expr # Lt
    | expr GT expr # Gt
    | expr GE expr # Ge
    | expr LE expr # Le
    | expr EQ expr # Eq
    | expr NEQ expr # Neq
    ;

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
IF: 'if' ;
ELSE : 'else' ;
KEYL : '{' ;
KEYR : '}' ;
WRITE : 'write' ;
IDVAR : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;
WS : [ \n]+ -> skip ;