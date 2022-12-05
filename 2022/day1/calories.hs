module Calories where

  import System.IO
  import Data.List


  main = do
    handle <- openFile "input.txt" ReadMode
    contents <- hGetContents handle
    let linesOfFile =  lines contents

    let backpacks_sorted_desc = reverse $ sort $ backpacks linesOfFile [] []
    putStrLn $ "Part 1 - Maximum calories in a single backpack: " ++ show (head backpacks_sorted_desc)
    putStrLn $ "Part 2 - Maximum calories in three backpacks: " ++ show (sum (take 3 backpacks_sorted_desc))
    hClose handle

  type Calories = Integer
  type InputText = String

  backpacks :: [InputText] -> [Calories] -> [Calories] -> [Calories]
  backpacks [] b bs = ((sum b):bs)
  backpacks ("":xs) b bs = backpacks xs [] ((sum b):bs)
  backpacks (x:xs) b bs = backpacks xs (calories:b) bs
    where calories = read x :: Calories
