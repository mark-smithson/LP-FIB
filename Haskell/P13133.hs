sumMultiples35 :: Integer -> Integer
sumMultiples35 n = sumMultiples n 3 + sumMultiples n 5 - sumMultiples n 15

sumMultiples :: Integer -> Integer -> Integer
sumMultiples n x = x * z * (z + 1) `div` 2
    where z = div (n - 1) x

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

fibonacci :: Int -> Integer
fibonacci n = fibs !! n

sumEvenFibonaccis :: Integer -> Integer
sumEvenFibonaccis n = sum[x | x<- takeWhile (< n) (map fibonacci [1..]), even x]

isPrime :: Int -> Bool
isPrime k = (k > 1) && null [ x | x <- [2..k-1], k `mod` x == 0]

largestPrimeFactor :: Int -> Int
largestPrimeFactor 1 = 1
largestPrimeFactor n = maximum [x | x <- [2..n], mod n x == 0, isPrime x]

isPalindromic :: Integer -> Bool
isPalindromic n = show n == reverse (show n)