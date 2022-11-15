calcul :: [String] -> [Int] -> [Int]
calcul [] stack = stack
calcul ("+":xs) (x1:x2:stack) = calcul xs ((x2 + x1):stack)
calcul ("-":xs) (x1:x2:stack) = calcul xs ((x2 - x1):stack)
calcul ("/":xs) (x1:x2:stack) = calcul xs (div x2 x1:stack)
calcul ("*":xs) (x1:x2:stack) = calcul xs ((x2 * x1):stack)

calcul (x:xs) stack = calcul xs (read x:stack)

eval1 :: String -> Int
eval1 str = head $ calcul (words str) []

calcul2 :: [Int] -> String -> [Int]
calcul2 (x1:x2:xs) "+" = (x2 + x1):xs
calcul2 (x1:x2:xs) "-" = (x2 - x1):xs
calcul2 (x1:x2:xs) "*" = (x2 * x1):xs
calcul2 (x1:x2:xs) "/" = (div x2 x1):xs
calcul2 xs x           = (read x):xs

eval2 :: String -> Int
eval2 str = head (foldl calcul2 [] (words str))

fsmap :: a -> [a -> a] -> a
fsmap = foldl (\ x f -> f x)

divideNconquer::(a -> Maybe b) -> (a -> (a,a)) -> (a -> (a,a) -> (b,b) -> b) -> a -> b
divideNconquer base divide conquer x
    | f (base x) = conquer x (divide x) (divideNconquer base divide conquer (fst $ divide x),divideNconquer base divide conquer (snd $ divide x))
    --cas del problema trivial
    | otherwise = (\(Just y) -> y) (base x)
        where
        --no es trivial quan es Nothing
        f Nothing = True
        f _ = False

quickSort::[Int]->[Int]
quickSort = divideNconquer base divide conquer
    where
    base [] = Just []
    base [x] = Just [x]
    base _ = Nothing
    divide x = (filter ((x!!div (length x) 2)>) x,filter ((x!!div (length x) 2)<) x)
    conquer x _ con = fst con++filter ((x!!div (length x) 2)==) x++snd con


data Racional = Racional Integer Integer

racional :: Integer -> Integer -> Racional
racional num den = Racional (div num mcd) (div den mcd)
  where
    mcd = gcd num den

numerador :: Racional -> Integer
numerador (Racional n d) = n

denominador :: Racional -> Integer
denominador  (Racional n d) = d

instance Eq Racional where
    Racional n1 d1 == Racional n2 d2 = n1 == n2 && d1 == d2

instance Show Racional where
    show (Racional n d) = show n ++ "/" ++ show d


data Tree a = Node a (Tree a) (Tree a)
recXnivells :: Tree a -> [a]
recXnivells t = recXnivells' [t]
    where recXnivells' ((Node x fe fd):ts) = x:recXnivells' (ts ++ [fe, fd])

racionalsTree :: Racional -> Tree Racional
racionalsTree (Racional a b) = Node (Racional a b) tl tr
    where
        tl = racionalsTree (Racional a (a+b))
        tr = racionalsTree (Racional (a+b) b)

racionals :: [Racional]
racionals = recXnivells (racionalsTree (Racional 1 1))
