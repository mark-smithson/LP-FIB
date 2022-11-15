fizzBuzz :: [Either Int String]
fizzBuzz = [fizzBuzz3 m3 m5 x | x <- [0..], let m3 = mod x 3 == 0, let m5 = mod x 5 == 0]
    where 
        fizzBuzz3 :: Bool -> Bool -> Int -> Either Int String
        fizzBuzz3 m3 m5 x 
            | m3 && m5 = Right "FizzBuzz"
            | m3 = Right "Fizz"
            | m5 = Right "Buzz"
            | otherwise = Left x

