data Tree a = Empty | Node a (Tree a) (Tree a)
        deriving (Show)

instance Foldable Tree where
  foldr f i Empty = i
  foldr f i (Node x tl tr) = f x (foldr f (foldr f i tr) tl)

avg :: Tree Int -> Double
avg t = fromIntegral (div (sum t) (length t))

cat :: Tree String -> String
cat = foldr (\x y -> if x == "" then y else x ++ " " ++ y) ""


