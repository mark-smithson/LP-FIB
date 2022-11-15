euclidean :: (Float, Float) -> (Float, Float) -> Float
euclidean (x1, y1) (x2, y2) = sqrt $ (x1 - x2)^2 + (y1 - y2)^2

closest :: [(Float,Float)] -> Float
closest (x:y:[]) = euclidean x y
closest (p:l) = minimum (map (\x -> euclidean x p) l ++ [closest l])