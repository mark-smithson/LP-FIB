grammar Expr;

root : expr EOF ;

expr : <assoc=right> expr EXP expr
    | expr (MULT|DIV) expr
    | expr (SUM|SUB) expr
    | NUM
    ;

cond : expr ('='|'!='|'<'|'>'|'<='|'>=') expr ;

NUM : [0-9]+ ;
SUM : '+' ;
SUB : '-' ;
MULT : '*' ;
DIV : '/' ;
EXP : '^' ;

WS : [ \n]+ -> skip ;