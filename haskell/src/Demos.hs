module Demos where

import qualified Data.Map as Map

-- trueFalseTo10
-- This function accepts a Bool and returns 1
-- if that parameter is True; 0, otherwise.

-- We can be explicit, or not. Let's be explicit
-- This says that trueFalseTo10's parameter
-- is a Bool and that it returns an Int.
trueFalseTo10 :: Bool -> Int

trueFalseTo10 tf = if tf then 1 else 0
--trueFalseTo10 tf = trueFalseToNum tf 1 0

-- trueFalseToNum
trueFalseToNum :: Bool -> Int -> Int -> Int

-- trueFalseToNum tf t f = if tf then t else f

trueFalseToNum True t _ = t
trueFalseToNum False _ f = f

infinity = [x | x <- [0..]]
evens = [x | x <- infinity, even x]
odds = [x | x <- infinity, odd x]

first100Odds = take 100 odds

overUnder ou v | v > ou = True
               | otherwise = False

first100OddsOver100 = filter (\x -> overUnder 100 x) first100Odds
-- first100OddsOver100 = filter (overUnder 100) first100Odds
first100OddsUnder100 = filter (\x -> not (overUnder 100 x)) first100Odds

-- Let's write a function that returns the last element
-- in the list.
myTail (x:[]) = x
myTail (_:y) = myTail y

-- Let's write a function that doubles each
-- element in the list.
doubleList [] = []
doubleList (head:tail) = head*2 : doubleList tail

-- Let's write a function that triples each
-- element in the list.
tripleList [] = []
tripleList (head:tail) = head*3 : tripleList tail

-- Ugh, that's repetitive!
pleList [] f = []
pleList (head:tail) f = f*head : pleList tail f

-- What if we wanted to do something else?
fList [] f = []
fList (head:tail) f = (f head) : fList tail f

myif :: Bool -> a -> a -> a
myif True t _ = t
myif False _ f = f

-- call = let x = myif True 1 (div 1 0) in
--       let y = myif False 1 (div 1 0) in
--       (x,y)
--
instance (Show a) => Show (MyMaybe a) where
  show (Some l) = foldr (((++) . show)) "" l
  show (None) = "Nothing passed the filter!"

data MyMaybe a = Some [a] | None
doMyFilter output f [] | not ((length output) == 0) = Some output
                      | otherwise = None
-- doMyFilter output f [] = output
doMyFilter output f (x:xs) | f x = doMyFilter (output++[x]) f xs
                           | otherwise = doMyFilter output f xs
myFilter = doMyFilter []
