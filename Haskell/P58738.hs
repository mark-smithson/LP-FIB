{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
data STree t = Nil | Node Int t (STree t) (STree t)
    deriving (Show)

talla :: STree a -> Int
talla Nil = 0
talla (Node _ _ tl tr) = 1 + talla tl + talla tr

isOk :: STree a -> Bool
isOk Nil = True
isOk (Node x _ tl tr) = isOk' x && isOk tl && isOk tr
    where
        isOk' x = x == talla tl + talla tr + 1

-- not O(h)
nthElement :: STree a -> Int -> Maybe a
nthElement Nil _ = Nothing
nthElement (Node t x tl tr) n
  | pos == n        = Just x
  | pos < n         = nthElement tr (n-pos)
  | otherwise       = nthElement tl n
      where
        tE = getTalla tl
        tR = getTalla tr
        pos = tE + 1
        getTalla Nil = 0
        getTalla (Node t _ _ _) = t

mapToElements :: (a -> b) -> STree a -> [Int] -> [Maybe b]
mapToElements f t = map apply
    where
        apply l' = nthElement t l' >>= \el -> return (f el)

instance Functor STree where
    fmap f Nil = Nil
    fmap f (Node x n tl tr) = Node x (f n) (fmap f tl) (fmap f tr)
