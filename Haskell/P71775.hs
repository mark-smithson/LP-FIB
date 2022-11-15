countIf :: (Int -> Bool) -> [Int] -> Int
countIf f x = length (filter f x)

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam x = map (`map` x)

-- pam2 [1,2,3] [(+1),(*2),(^2)] -> [[2,2,1],[3,4,4],[4,6,9]]
pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 a f = map (\x -> map ($x) f) a

