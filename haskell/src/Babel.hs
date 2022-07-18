module Babel where

data Language = Functional [Char] | Imperative [Char]

instance Show Language where
  show (Functional x) = x ++ " is a functional language."
  show (Imperative x) = x ++ " is an imperative language."
  
