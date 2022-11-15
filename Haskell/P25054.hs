myLength :: [Int] -> Int 
myLength [] = 0
myLength (x:xs) = 1 + myLength xs 

myMaximum :: [Int] -> Int
myMaximum [x] = x
myMaximum (x:xs) 
    | x > max = x
    | otherwise = max

    where max = myMaximum xs

intToFloat::Int -> Float
intToFloat n = fromInteger (toInteger n)

average :: [Int] -> Float
average [x] = intToFloat x
average (x:xs) = intToFloat (x+sum xs) / intToFloat (1 + myLength xs)
    where 
        sum :: [Int] -> Int
        sum [] = 0
        sum (x:xs) = x + sum xs

buildPalindrome :: [Int] -> [Int]
buildPalindrome [] = []
buildPalindrome x = reverse x ++ x
    where
        reverse :: [Int] -> [Int]
        reverse [x] = [x]
        reverse (x:xs) = reverse xs ++ [x]

inside :: [Int] -> Int -> Bool
inside [y] x = y == x
inside (y:ys) x = (y == x) || inside ys x

remove :: [Int] -> [Int] -> [Int]
remove [] [] = []
remove [] y = []
remove x [] = x
remove (x:xs) y
    | not (inside y x)  = (x:(remove xs y))
    | otherwise = remove xs y

flatten :: [[Int]] -> [Int]
flatten [] = []
flatten (x:xs) = x ++ flatten xs

odds :: [Int] -> [Int]
odds [] = []
odds (x:xs)
    | mod x 2 == 0 = odds xs
    | otherwise = (x:(odds xs))

evens :: [Int] -> [Int]
evens [] = []
evens (x:xs)
    | mod x 2 == 1 = evens xs
    | otherwise = (x:(evens xs))

oddsNevens :: [Int] -> ([Int],[Int]) 
oddsNevens [] = ([],[]) 
oddsNevens x = (odds x, evens x)

isPrimeRec :: Int -> Int -> Bool
isPrimeRec n div
    | div == 1 = True
    | mod n div == 0 = False
    | otherwise = isPrimeRec n (div-1)

isPrime :: Int -> Bool
isPrime n
    | n < 2 = False
    | n == 2 = True
    | otherwise = isPrimeRec n (n-1)

primeDivisors :: Int -> [Int]
primeDivisors 1 = []
primeDivisors n = primeDivisorsAux 2
  where
    primeDivisorsAux :: Int -> [Int]
    primeDivisorsAux d
      | d > n = []
      | ((mod n d) == 0) && isPrime d = (d:(primeDivisorsAux (d+1)))
      | otherwise = primeDivisorsAux (d+1)