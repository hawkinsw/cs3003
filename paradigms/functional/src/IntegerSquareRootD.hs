{-|
  Module: IntegerSquareRootD
  Description: Functionality for calculating the integer square root of a number.
-}
module IntegerSquareRootD where

{-|
    The 'integerSquareRoot' function calculates the integer square root 
    of a given number.
-}
integerSquareRoot :: Int -- ^ The number for which to calculate the integer square root.
  -> Maybe Int -- ^ The integer square root or Nothing, if one cannot be found.
integerSquareRoot x_squared = doSquareRoot x_squared 0  -- integerSquareRoot simply calls the doSquareRoot function.

{-|
  Finds the integer square root of a given number.
  Starts by calculating whether the guess (second argument)
  is an integer square root of the given number (first argument).
  Calls itself recursively if it is not.
-}
doSquareRoot :: Int -- ^ The number for which to calculate the integer square root
  -> Int -- ^ The current "guess"
  -> Maybe Int -- ^ The integer square root or Nothing, if one cannot be found.
doSquareRoot x_squared maybe_x 
  | maybe_x*maybe_x == x_squared = Just maybe_x -- Using guards to determine which of the code to execute.
                                                -- We have a success here and have found an integer square root.
  | maybe_x*maybe_x > x_squared = Nothing       -- We are too high -- there is no integer square root so we return Nothing.
  | otherwise = doSquareRoot x_squared (maybe_x + 1) -- Otherwise, we'll try again with the next highest guess.
