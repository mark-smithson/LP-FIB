grammar Funx;

root : block EOF ;

block: instr block
    |
    ;

instr : assign
    | statement
    | createFunction
    | expr
    ;

createFunction : IDFUNC paramsCreateFunction KEYL block KEYR # CreateFunc;
invokeFunction : IDFUNC paramsInvokeFunction # InvFunc;

paramsCreateFunction : IDVAR* # ParamsCreateFunc;
paramsInvokeFunction : expr* # ParamsInvFunc;

statement : WRITE expr # Write
    | IF condition KEYL block KEYR # Ifst
    | IF condition KEYL block KEYR ELSE KEYL block KEYR # Ifelsest
    | WHILE condition KEYL block KEYR # While
    ;

expr : LP expr RP # ParentExp
    |<assoc=right> expr EXP expr # Exp
    | expr MULT expr # Mult
    | expr DIV expr # Div
    | expr MOD expr # Mod
    | expr SUM expr # Sum
    | expr SUB expr # Sub
    | invokeFunction # InvokFunc
    | NUM # Value
    | IDVAR # Var
    | IDFUNC # VarFunc
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
WHILE: 'while' ;
ELSE : 'else' ;
KEYL : '{' ;
KEYR : '}' ;
LP : '(' ;
RP : ')' ;
WRITE : 'write' ;
IDVAR : [a-z][a-zA-Z0-9]* ;
IDFUNC : [A-Z][a-zA-Z0-9]* ;
WS : [ \n]+ -> skip ;