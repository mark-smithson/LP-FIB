
myUnfoldr :: (b -> Maybe (a, b)) -> b -> [a]

myUnfoldr f x = case f x of
    Nothing -> []
    Just (m, n) -> m : myUnfoldr f n 


myReplicate :: a -> Int -> [a]

myReplicate x n = myUnfoldr f n
    where 
        f 0 = Nothing
        f c = Just (x, c - 1)


myIterate :: (a -> a) -> a -> [a]

myIterate f = myUnfoldr (\x -> Just (x, f x)) 


myMap :: (a -> b) -> [a] -> [b]

myMap f = myUnfoldr g
    where 
        g [] = Nothing
        g (y:ys) = Just (f y, ys)



data Bst a = Empty | Node a (Bst a) (Bst a)

add :: Ord a => a -> (Bst a) -> (Bst a)
add x Empty = Node x Empty Empty
add x (Node y l r)
    | x < y     = Node y (add x l) r
    | x > y     = Node y l (add x r)
    | otherwise = Node y l r

instance Show a => Show (Bst a) where
    show Empty = "."
    show (Node x l r) = "(" ++ show x ++ " " ++ show l ++ " " ++ show r ++ ")"

adder :: Ord a => (Bst a, [a]) -> Maybe (Bst a, (Bst a, [a]))

adder (_, []) = Nothing
adder (t, x:xs) = Just (t2, (t2, xs))
    where t2 = add x t

