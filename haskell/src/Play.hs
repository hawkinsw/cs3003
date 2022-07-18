module Play where

data MyBoolean = MyTrue | MyFalse

instance Show MyBoolean where
  show MyTrue = "True"
  show MyFalse = "False"

class JsTruthy a where
  truthy :: a -> Bool

instance JsTruthy [a] where
  truthy [] = False
  truthy _ = True
