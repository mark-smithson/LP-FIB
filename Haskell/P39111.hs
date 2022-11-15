import Data.List

type Pos = (Int, Int)       -- la casella inferior esquerra és (1,1)

dins :: Pos -> Bool
dins (x,y) = x >= 1 && x <= 8 && y >= 1 && y <= 8

moviments :: Pos -> [Pos]
moviments (x,y) = [(x+z, y+k) | (z,k) <- moves, dins (x+z,y+k)]
    where
        moves = [(1,2), (-1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2, 1), (-2,-1)]
        
movimentsList :: [Pos] -> [Pos]
movimentsList = concatMap moviments

potAnar3 :: Pos -> Pos -> Bool
potAnar3 i f = f `elem` movimentsList (movimentsList (movimentsList [i]))

potAnar3' :: Pos -> Pos -> Bool
potAnar3' i f = f `elem` ((moviments i >>= moviments) >>= moviments)
