data Tree a = Empty | Node a (Tree a) (Tree a)

inOrder :: Show a => Tree a -> String
inOrder Empty = "()"
inOrder (Node x tl tr) = "(" ++ inOrder tl ++ "," ++ show x ++ "," ++ inOrder tr ++ ")"

instance Show a => Show (Tree a) where
  show a = inOrder a

instance Functor Tree where
    fmap f Empty = Empty
    fmap f (Node x fe fd) = Node (f x) (fmap f fe) (fmap f fd)

doubleT :: Num a => Tree a -> Tree a
doubleT = fmap (*2)

data Forest f = Forest [Tree f]
    deriving(Show)
 
-- Comentar Jordi
instance Functor Forest where
    fmap f (Forest xs) = Forest $ fmap (fmap f) xs

doubleF :: Num a => Forest a -> Forest a
doubleF = fmap (*2)