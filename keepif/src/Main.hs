module Main where

import KeepIf

main :: IO ()
main = let result = keepIfB odd [1..10] in putStrLn $ show result
