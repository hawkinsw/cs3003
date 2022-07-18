module Tries where

data Attempts a = MaxAttempts (a -> Bool) Int Int
data Try a = SuccessfulTry | FailTry | MoreTry (Attempts a) a | MaybeTry a

instance Monad Try where
  return a = SuccessfulTry
  (>>=) (MoreTry (MaxAttempts checker maxAttempts currentAttempts) lastValue) f = case (f lastValue) of
    MaybeTry a -> case (checker a) of
      True -> SuccessfulTry
      False -> if maxAttempts > currentAttempts then
                  FailTry
               else
                  MoreTry (MaxAttempts checker maxAttempts (currentAttempts+1)) a
  (>>=) SuccessfulTry f = SuccessfulTry
