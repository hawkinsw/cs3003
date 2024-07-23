module MyError where

import Data.List

data ErrorResult a = Error String | Result a

safeDivision :: Integer -> Integer -> ErrorResult Integer

safeDivision x 0 = Error "Cannot divide by zero"
safeDivision x y = Result (x `div` y)

checkSafeDivision :: ErrorResult Integer -> String
checkSafeDivision (Result res) = "Phew, our division was safe! (result: " ++ show res ++ ")"
checkSafeDivision (Error err) = "Oh no, there was an error: " ++ err ++ "!"

instance (Show a) => Show (ErrorResult a) where
  show (Result res) = "Result: " ++ show res
  show (Error err) = "Error: " ++ err

f = Result (7 `div` 2)

functionThatTakesList :: [a] -> Bool
functionThatTakesList _ = True

myMultipli a b = (*) a b

myCMultipli a = (\b -> (*) a b)

needler n h = case (elemIndex n h) of 
  Nothing -> "Nothing"
  (Just a) -> "Got a " ++ (show a)