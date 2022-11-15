myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl _ x [] = x
myFoldl f i (x:xs) = myFoldl f (f i x) xs

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr _ x [] = x
myFoldr f i (x:xs) = f x (myFoldr f i xs)

myIterate :: (a -> a) -> a -> [a]
myIterate f x = x : myIterate f (f x)

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil c f x
    | c x = x
    | otherwise = myUntil c f (f x)

myMap :: (a -> b) -> [a] -> [b]
myMap f x = [f y | y <- x]

-- dubte no-recursivitat
myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f x = [y | y <- x, f y]

myAll :: (a -> Bool) -> [a] -> Bool
myAll f x = and $ map f x

myAny :: (a -> Bool) -> [a] -> Bool
myAny f x = or $ map f x

myZip :: [a] -> [b] -> [(a, b)]
myZip [] y = []
myZip x [] = []
myZip (x:xs) (y:ys) = [(x,y)] ++ myZip xs ys

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f a b = [f x y | (x,y) <- myZip a b]


