multEq :: Int -> Int -> [Int]
multEq x y = iterate (\z -> z*x*y) 1

belongs :: Int -> [Int] -> Bool
belongs _ [] = False
belongs x (y:ys)
    | x == y = True
    |otherwise = belongs x ys

--retorna la posicio de l'integer a la llista
position :: Int -> [Int] -> Int
position x (y:ys)
    | x == y = 1
    | otherwise = 1 + position x ys

--retorna els elements de l1 que apareixen a l2 en una 
--posicio menor estricte que a l3
selectFirst :: [Int] -> [Int] -> [Int] -> [Int]
selectFirst [] _ _ = []
selectFirst _ [] _ = []
--agafarem el valor de l1, anirem mirant l2 i l3, 
--si el trobem a l2 abans que a l3 l'afegim a la llista
selectFirst xs ys zs = [x | x <- xs, belongs x ys && (not (belongs x zs) || (position x ys < position x zs))]

myIterate :: (a -> a) -> a -> [a]
myIterate f n = scanl (\x _ -> f x) n [1..]

type SymTab a = String -> Maybe a

empty :: SymTab a
empty a = Nothing

get :: SymTab a -> String -> Maybe a
get a s = a s

set :: SymTab a -> String -> a -> SymTab a
set st s val c 
    | s == c = Just val
    | otherwise = st c

data Expr a
    = Val a
    | Var String
    | Sum (Expr a) (Expr a)
    | Sub (Expr a) (Expr a)
    | Mul (Expr a) (Expr a)
    deriving Show

eval :: (Num a) => SymTab a -> Expr a -> Maybe a
eval st (Val a) = Just a
eval st (Var a) = st a
eval st (Sum n n2) = do 
    x <- eval st n
    y <- eval st n2
    return $ x + y 
eval st (Sub n n2) = do 
    x <- eval st n
    y <- eval st n2
    return $ x - y 
eval st (Mul n n2) = do 
    x <- eval st n
    y <- eval st n2
    return $ x*y 
