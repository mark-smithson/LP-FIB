-- words: creates an array of string from the original one, white space characters serving as separators
-- show: converts its argument to a string
-- read: casts strings to another type
-- getContents: returns all user input as a single string
-- putStrLn: writes out a string and the newline character to the standard output

sumInp':: [String] -> Int
sumInp' = foldr ((+) . read) 0

sumInp:: String -> String
sumInp x = show (sumInp' y)
    where y = words x

main :: IO ()
main = do
    contents <- getContents
    putStrLn (sumInp contents)
    return ()