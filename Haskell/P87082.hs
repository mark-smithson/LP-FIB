inter :: Double -> Double -> String
inter w h
    | imc < 18 = "magror"
    | imc >= 18 && imc < 25 = "corpulencia normal"
    | imc >= 25 && imc < 30 = "sobrepes"
    | imc >= 30 && imc < 40 = "obesitat"
    | otherwise = "obesitat morbida"

    where
        imc = w/(h*h)

getImc :: [String] -> String
getImc ls = name ++ ": " ++ inter (read (ls!!1)::Double) (read (ls!!2)::Double)
    where
        name = head ls

compute :: String -> String
compute s = getImc s'
    where
        s' = words s
main = do
    line <- getLine
    if line /= "*" then do
        putStrLn $ compute line
        main
    else
        return ()