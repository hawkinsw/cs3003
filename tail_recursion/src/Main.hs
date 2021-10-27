module Main where

import TailRecursion

main :: IO ()
main =
  do
    let result = factorial 1000000 in putStrLn $ show $ result
