flatten :: [[Int]] -> [Int]
flatten = foldl (++) []

myLength :: String -> Int 
myLength = foldr (+) 0 . map (const 1)

myReverse :: [Int] -> [Int]
myReverse = foldl (flip(:)) []

countIn :: [[Int]] -> Int -> [Int]
countIn x y = map count x
    where 
        count :: [Int] -> Int
        count  = length . (filter (==y))

firstWord :: String -> String
firstWord = takeWhile (/= ' ') . dropWhile(== ' ')