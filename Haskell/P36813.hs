{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
import Data.List

-- Bool is an instance of Enum: you can enumerate the two values of a Bool: False, and then True
-- As a result, it implements the fromEnum :: Enum a => a -> Int, a function that maps a value of an 
--                                          Enum type to an Int: for a Bool, it maps False to 0, and True to 1

degree :: Eq a => [(a, a)] -> a -> Int
degree [] x = 0
degree ((a,b):l) x = fromEnum (a == x || b == x) + degree l x

degree' :: Eq a => [(a, a)] -> a -> Int
degree' l z = length ([(x,y) | (x,y) <- l, x == z || y == z])

chooseNeigh :: Ord a => (a,a) -> a -> a
chooseNeigh (x,y) z = if z == x then y else x

neighbors :: Ord a => [(a, a)] -> a -> [a]
neighbors l x = [chooseNeigh (z,k) x | (z,k) <- l, x == z || x == k]
