module KeepIf where

keepIfA :: Ord a => (a -> Bool) -> [a] -> [a]

keepIfA _ [] = []
keepIfA f (x:xs) = if f x then
    x:(keepIfA f xs)
  else
    (keepIfA f xs)

keepIfB :: Ord a => (a -> Bool) -> [a] -> [a]
keepIfB _ [] = []
keepIfB f (x:xs) | f x = x:(keepIfB f xs)
                 | otherwise = keepIfB f xs

keepIfC f xs = foldl (\acc v -> case f v of
  True -> acc ++ [v]
  False -> acc) [] xs
