module IntegerSquareRoot where

integerSquareRoot :: Int -> Maybe Int
integerSquareRoot x_squared = doSquareRoot x_squared 0 

doSquareRoot :: Int -> Int -> Maybe Int
doSquareRoot x_squared maybe_x 
  | maybe_x*maybe_x == x_squared = Just 6
  | maybe_x*maybe_x > x_squared = Nothing
  | otherwise = doSquareRoot x_squared (maybe_x + 1)
