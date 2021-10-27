module TailRecursion where

-- Non tail-recursive implementation of factorial
factorial 0 = 1
factorial x = x * (factorial x-1)

-- Driver function for actual implementation of tail-recursive factorial
factorialTail = factorialTailImpl 1 
-- Actual worker-bee function for doing the tail-recursive factorial calculation
factorialTailImpl runningTotal 0 = runningTotal
factorialTailImpl runningTotal x = factorialTailImpl (runningTotal*x) (x-1)

-- Non tail-recursive implementation of myLen
myLen [] = 0
myLen (x:xs) = (myLen xs) + 1

-- Driver function for the actual implementation tail-recursive myLen
myLenTail list = myLenTailImpl list 0
-- Actual worker-bee function for doing the tail-recursive myLen calculation
myLenTailImpl [] acc = acc
myLenTailImpl (x:xs) acc = myLenTailImpl xs (1 + acc)
