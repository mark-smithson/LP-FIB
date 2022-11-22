grammar Expr;

root : expr EOF ;

expr : <assoc=right> expr '^' expr
    | expr ('*'|'/'|'+'|'-') expr
    | NUM
    ;

NUM : [0-9]+ ;
WS : [ \n]+ -> skip ;