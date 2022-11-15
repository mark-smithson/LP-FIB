{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
data Tree a = Node a (Tree a) (Tree a) | Empty
    deriving (Show)

size :: Tree a -> Int
size Empty = 0
size (Node _ tl tr) = 1 + size tl + size tr

height :: Tree a -> Int
height Empty = 0
height (Node _ tl tr) = 1 + max (height tl) (height tr)

equal :: Eq a => Tree a -> Tree a -> Bool
equal Empty Empty = True
equal (Node x1 tl1 tr1) (Node x2 tl2 tr2) = x1 == x2 && equal tl1 tl2 && equal tr1 tr2
equal _ _ = False

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic Empty Empty = True
isomorphic (Node x1 tl1 tr1) (Node x2 tl2 tr2) = x1 == x2 && (isomorphic tl1 tl2 && isomorphic tr1 tr2) || 
                                                                (isomorphic tl1 tr2 && isomorphic tr1 tl2)
isomorphic _ _ = False

preOrder :: Tree a -> [a]
preOrder Empty = []
preOrder (Node x tl tr) = [x] ++ preOrder tl ++ preOrder tr

postOrder :: Tree a -> [a]
postOrder Empty = []
postOrder (Node x tl tr) = postOrder tl ++ postOrder tr ++ [x]

inOrder :: Tree a -> [a]
inOrder Empty = []
inOrder (Node x tl tr) = inOrder tl ++ [x] ++ inOrder tr

-- Implement queue
breadthFirst :: Tree a -> [a]
breadthFirst t = bf [t]
  where
    bf [] = []
    bf (Empty : xs) = bf xs
    bf ((Node x tl tr) : xs) = x : bf (xs ++ [tl,tr])

build :: Eq a => [a] -> [a] -> Tree a
build [] [] = Empty
build (h:pre) ind = Node h (build tl tlL) (build tr trL)
    where
        tlL = takeWhile (/= h) ind
        lastl = last tlL
        trL = tail $ dropWhile (/= h) ind
        tl = takeWhile (/= lastl) pre ++ [lastl]
        tr = tail $ dropWhile (/= lastl) pre

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap _ a Empty = a
overlap _ Empty b = b
overlap f (Node ax al ar) (Node bx bl br) = Node (f ax bx) (overlap f al bl) (overlap f ar br)