module Demos where

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
doubleList (head:[]) = [head*2]
doubleList (head:tail) = head*2 : doubleList tail

-- Let's write a function that triples each
-- element in the list.
tripleList (head:[]) = [head*3]
tripleList (head:tail) = head*3 : tripleList tail

-- Ugh, that's repetitive!
pleList (head:[]) f = [f*head]
pleList (head:tail) f = f*head : pleList tail f

-- What if we wanted to do something else?
fList (head:[]) f = [f head]
fList (head:tail) f = (f head) : fList tail f
