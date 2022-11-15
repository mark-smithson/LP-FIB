hanoi :: Int -> String -> String -> String -> IO ()
hanoi 0 _ _ _ = return ()
hanoi n source target intermediate = do
  hanoi (n - 1) source intermediate target
  putStrLn $ source ++ " -> " ++ target
  hanoi (n - 1) intermediate target source

main :: IO ()
main = do
  line <- getLine
  let items = words line
  let disks = (read $ head items) :: Int
  let [peg1, peg2, peg3] = tail items
  hanoi disks peg1 peg2 peg3
