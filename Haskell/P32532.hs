divisors :: Int -> [Int]
divisors n = [x | x <- [1..n], mod n x == 0]

nbDivisors :: Int -> Int
nbDivisors = length . divisors

moltCompost :: Int -> Bool
moltCompost n = and [nbDivisors x < nbDivisors n | x <- [1..n-1]]