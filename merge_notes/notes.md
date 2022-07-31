## Deciphering The Notes About Merge

I had a great discussion with several of you at a recent office hours about implementing merge sort in Haskell. We talked about how the real workhorse of the implementation of merge sort is, in reality, the merge function! We wrote down an implementation of the function very quickly. Perhaps it will help to go through and expand on that notation (you can see it in the `notes.pdf` in this directory). 

### John Hancock

Start by thinking about the "signature" of the `merge` function. Let's rewrite it so that it's a little more verbose and readable:

```Haskell
merge in_progress_result comparator (left_head:left_rest) (right_head:right_rest)
```

### Examples Make the Heart Grow Fonder
If we wanted to merge two in-order lists to generate an in-order list that contained the elements from each of the given lists, we would make this function call:

```Haskell
merge [] (\l r -> l < r) [1,4,5] [2,3,6]
```

### Back to Signatures
Before going further, think about the "anonymous" function that we gave `merge` for the `comparator` parameter: That function is going to take two parameters (we call them `l` and `r` (for left and right)) and we return `True` if `l` is less than `r` -- in other words, we return `True` if the left parameter compares less than the right parameter.

### The Business of Merge
The definition of the `merge` function will be recursive so perhaps it makes sense to look at one of the calls to `merge` that happens during the evaluation of the invocation of `merge` that we hypothesized above. At some point during the evaluation, the following invocation of `merge` will be called:

```Haskell
merge [1,2] (\l r -> l < r) [4,5] [3,6]
```

Awesome! How does that break down according to our function's parameters:
`in_progress_result`: `[1,2]`

`comparator`: `(\l r -> l < r)`

`left_head`: `4`

`left_rest`: `[5]`

`right_head`: `3`

`right_rest`: `[6]`

The goal of `merge` on any invocation is to determine which of the elements at the front of the two lists at the end of the invocation go next in the merged list. We can use `comparator` to make that determination. If 

```Haskell
(comparator left_head right_head)
```
 returns `True`, then `left_head` should go in the merged list next. Otherwise, `right_head` should go in the merged list next. What does that look like in *this* particular case:

```Haskell
(comparator left_head right_head)
(comparator 4 right_head)
(comparator 4 3)
((\l r -> l < r) 4 3)
((\r -> 4 < r) 3)
(4 < 3)
(False)
```

### Sign the Contract
Okay! So, we have applied `comparator` and we know that the `right_head` is the one that goes next in the merged list. In order to continue the merge, we will call ourselves recursively. What, exactly does that invocation look like? Well, we want to update the values in the in-progress merged list, and the values in the two lists that we are merging. We do not want to change the `comparator` function. So, we essentially want to make a call that looks like:

```Haskell
merge [1,2,3] (\l r -> l < r) [4,5] [6]
```

Great! Now, what happens in the case when we get down to a situation where either (or both) of the lists that we are going to merge contain no values? Well, if the left list contains no values, then the result of the merge is just the in-progress list plus the values remaining in the right list. If the right list contains no values, then the result of the merge is just the in-progress list plus the values remaining in the left list. Those are the base cases for the recursion!

For example,

```Haskell
merge [1,2,3,4,5] (\l r -> l < r) [] [6] = [1,2,4,5] ++ [6]
```
Wow!

### Big Things in the Pipeline
Couple what we said above with the meaning of the `|` and I hope that helps you grok what we wrote! The `|` puts an additional constraint on Haskell's pattern matching. For instance, let's write a simple function that takes two values and returns `True` when the first of those given values is less than the second and `False` *otherwise*. We could write that function like

```Haskell
less_than x y = if x < y then True else False
```

However, that's pretty verbose (and `if` is frowned upon in the world of Haskell). So, let's rewrite it using |:

```Haskell
less_than x y | x < y = True
              | otherwise = False
```

Because the variables `x` and `y` will pattern match any arguments given for those parameters, we know that the pattern match succeeds. So, that doesn't help Haskell choose which of the bodies to execute. To determine which body to execute, Haskell finds recourse in the conditions after the `|` and when `x` is less than `y`, then Haskell will execute the body that evaluates to `True`. Otherwise (literally!), Haskell will execute the body that returns `False`.