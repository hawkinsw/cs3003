module Curry where


-- Using an odd syntax to make a function that multiplies by 5
multiplyByFive = \x -> (*) 5 x

-- Now, let's make a function that takes in a user-specified "Five"
-- and generates something like a multiplyByF:
multiplyByF = \f -> (\x -> (*) f x)

-- We could write a function named multiplyBySix like this:
multiplyBySix = \x -> (*) 6 x

-- We could do the same for seven:
multiplyBySeven = \x -> (*) 7 x

-- And we could continue going like this ... or, there's a better way:
multiplyByEight = multiplyByF 8
multiplyByNine = multiplyByF 8

-- Compare the type of multiplyByF with the type of myMultiply:
myMultiply x y = (*) x y