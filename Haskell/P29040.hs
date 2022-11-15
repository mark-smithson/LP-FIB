insert :: [Int] -> Int -> [Int]
insert [] x = [x]
insert (y:ys) x
    | y < x = y : insert ys x
    | otherwise = x : y : ys

isort :: [Int] -> [Int]
isort = foldl insert []

-- change
remove :: [Int] -> Int -> [Int]
remove [] x = []
remove (y:ys) x
    | y == x = ys
    | otherwise = y : remove ys x

ssort :: [Int] -> [Int]
ssort [] = []
ssort xs = mini : ssort rest
    where
        mini = minimum xs
        rest = remove xs mini

merge :: [Int] -> [Int] -> [Int]
merge [] xs = xs
merge xs [] = xs
merge (x:xs) (y:ys)
    | x <= y = x : merge xs (y:ys)
    | otherwise = y : merge (x:xs) ys

msort :: [Int] -> [Int]
msort [] = []
msort [x] = [x]
msort xs = merge (msort $ take n xs) (msort $ drop n xs)
    where n = div (length xs) 2 

qsort :: [Int] -> [Int]
qsort [] = []
qsort (x:xs) = (qsort $ filter (<x) xs ) ++ [x] ++ (qsort $ filter (>= x) xs )

genQsort :: Ord a => [a] -> [a]
genQsort [] = []
genQsort (x:xs) = (genQsort $ filter (<x) xs ) ++ [x] ++ (genQsort $ filter (>= x) xs )
