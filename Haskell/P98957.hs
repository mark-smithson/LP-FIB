ones :: [Integer]
ones = 1 : ones

nats :: [Integer]
nats = 0 : map (+1) nats

-- [0,1,-1,2,-2,3,-3,4]
ints :: [Integer]
ints = 0 : concat [[x,-x] | x <- tail nats]

triangulars :: [Integer]
triangulars = scanl (+) 0 (tail nats)

-- [0!, 1!, 2!...]
factorials :: [Integer]
factorials = scanl (*) 1 (tail nats)

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

primes :: [Integer]
primes = garbell (drop 2 nats) -- use [2..] ? (problem restriction: "Can't use infinite enums as [1..]") 
    where
        garbell (p : xs) = p : garbell [x | x <- xs, x `mod` p /= 0]

-- hamming numbers multiplied by (2,3,5) give more hamming numbers (sort!!)
hammings :: [Integer]
hammings = 1 : merge (map (*2) hammings) (merge (map (*3) hammings) (map (*5) hammings))

-- given two sorted lists, return new one merging both of them with no repetitions
merge :: [Integer] -> [Integer] -> [Integer]
merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
    | x < y = x : merge xs (y:ys)
    | y < x = y : merge (x:xs) ys
    | otherwise = x : merge xs ys

-- [11] -> 2
look :: [Char] -> Int
look [] = 0 -- none
look [_] = 1 -- any but length = 1
look (c1:c2:s)
    | c1 == c2 = 1 + look (c2:s)
    | otherwise = 1

-- [11] -> [21]
say :: [Char] -> [Char]
say [] = []
say s = show (look s) ++ head s : say (drop (look s) s)

-- [1,11,21,1211,111221,312211,13112221,1113213211]
lookNsay :: [Integer]
lookNsay = iterate (read . say . show) 1

-- [["0",1,"0"],["0",1,1,"0"],["0",1,2,1,"0"],["0",1,3,3,1,"0"],..].
tartaglia :: [[Integer]]
tartaglia = iterate (\x -> zipWith (+) (0 : x) (x ++ [0])) [1]