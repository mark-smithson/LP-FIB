absValue :: Int -> Int
absValue n
    | n >= 0 = n
    | otherwise = -n

power :: Int -> Int -> Int
power _ 0 = 1
power a b 
    | even b = x*x
    | otherwise = x*x*a
    where
        x = power a n_div
        n_div = div b 2

isPrimeRec :: Integer -> Integer -> Bool
isPrimeRec n div
    | div == 1 = True
    | mod n div == 0 = False
    | otherwise = isPrimeRec n (div-1)


isPrime :: Integer -> Bool
isPrime n
    | n < 2 = False
    | n == 2 = True
    | otherwise = isPrimeRec n (n-1)

slowFib :: Integer -> Integer
slowFib n
    | n <= 1 = n
    | otherwise = slowFib (n-1) + slowFib (n-2)

quickFib :: Int -> Int
quickFib 0 = 0
quickFib 1 = 1
quickFib n = quickFibSum 0 1 2
  where
    quickFibSum :: Int -> Int -> Int -> Int
    quickFibSum first second it
      | it == n = first + second
      | otherwise = quickFibSum second (first + second) (it + 1)
