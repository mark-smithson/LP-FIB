grammar funx;

root : block EOF ;

block: instr block
    |
    ;

instr : assign
    | statement
    | createFunction
    | expr
    | createArray
    | appendToArray
    | popArray
    | condition
    ;

createFunction : IDFUNC paramsCreateFunction KEYL block KEYR # CreateFunc;
invokeFunction : IDFUNC paramsInvokeFunction # InvFunc;

paramsCreateFunction : IDVAR* # ParamsCreateFunc;
paramsInvokeFunction : expr* # ParamsInvFunc;

statement : IF condition KEYL block KEYR # Ifst
    | IF condition KEYL block KEYR ELSE KEYL block KEYR # Ifelsest
    | WHILE condition KEYL block KEYR # While
    | FOR assign COMMA condition COMMA assign KEYL block KEYR # For
    ;

expr : LP expr RP # ParentExp
    |<assoc=right> expr EXP expr # Exp
    | expr MULT expr # Mult
    | expr DIV expr # Div
    | expr MOD expr # Mod
    | expr SUM expr # Sum
    | expr SUB expr # Sub
    | SUB expr # Neg
    | invokeFunction # InvokFunc
    | LEN LP IDVAR RP #LenArr
    | IDVAR LC expr RC #AccArr
    | NUM # Value
    | IDVAR # Var
    | IDFUNC # VarFunc
    ;

createArray: IDVAR LISTC LC arrayParams RC #CreateArr;
arrayParams: expr* #ParamsArr;
appendToArray: IDVAR LISTARR expr #AppendArr;
popArray: LISTARR IDVAR #PopArr;

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
FOR: 'for' ;
ELSE : 'else' ;
KEYL : '{' ;
KEYR : '}' ;
LP : '(' ;
RP : ')' ;
LC : '[' ;
RC : ']' ;
COMMA: ',' ;
LISTC : '|=' ;
LISTARR : '<<' ;
LEN : 'len' ;
IDVAR : [a-z][a-zA-Z0-9]* ;
IDFUNC : [A-Z][a-zA-Z0-9]* ;
WS : [ \n]+ -> skip ;
COMMENT : '#' ~[\n]* -> skip ;