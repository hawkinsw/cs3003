## Curry-me Timbers

Just how much time does Curry-ing cost in Python? I think that we might be able to find out.

### Three Versions of Addition

Let's take a simple addition function in Python:

```Python
def addition(i: int, j: int) -> int:
    return i + j
```

Just to confirm: If we wanted to call that function, we wouldn't have to do anything special:

```Python
addition(1, 5)
```

Okay, that looks like what we would expect. But, let's make another version where we take advantage of Currying:

```Python
def single_addition(i: int)-> Callable[[int], int]:
    def local_addition(j: int) -> int:
        return i + j
    return local_addition
```

Great. But, just how would we call that function?

```Python
single_addition(1)(5)
```

That's a little odd, of course, because we have to invoke `single_addition` in order to get access to the inner function that takes the second parameter. So, we could write the same thing using a temporary variable and it might make a little more sense:


```Python
temp = single_addition(1)
temp(5)
```

> Note: What about the third version? Well, hold that thought!

### The Final Countdown

There is a neat little library in Python called `timeit` that we can use to time snippets of Python. Let's use that to take the measure of the speed. First, we will need to write an additional wrapper function that invokes our Curryd and non-Curryd `addition` function repeatedly:

```Python
def time_single_addition(low: int, high: int) -> int:
    result: int = 0
    for i in range(low, high):
        result += single_addition(low)(i)

def time_addition(low: int, high: int) -> int:
    result: int = 0
    for i in range(low, high):
        result += addition(low,i)
```

The `timeit` interface makes it difficult to time anything other than very simple statements. So, we will use an _additional_ wrapper around those functions:

```Python
def actually_time_addition() -> int:
    return time_addition(1, 100)

def actually_time_single_addition() -> int:
    return time_single_addition(1, 100)
```

Now, let's use `timeit` to, well, _time it_:

```Python
if __name__=="__main__":
    print(timeit.timeit("actually_time_single_addition()", setup="from __main__ import actually_time_single_addition"))
    print(timeit.timeit("actually_time_addition()", setup="from __main__ import actually_time_addition"))
```

### The Envelope Please ...

The results are in ...

| actually_time_single_addition | actually_time_addition |
| -- | -- |
| 15.46426754631102 | 3.3092930521816015 |

Well, there you have it. There _is_ significant overhead.

### Where Is That Third Implementation?

Well, where did that third implementation go that we referenced above? We could implement an optimization for the Curryd version. How could we do that? Well, instead of calling `single_addition` every time through the body of the loop in `time_single_addition`, we could invoke it _one time_ and then reuse it. Will that work? I think that it will because `low` is _always_ the value of the first parameter. Generating a function that takes one parameter from a function that takes two parameters and has the value of its first parameter fixed is _exactly_ where Currying is supposed to shine.

```Python
def time_single_addition_cached(low: int, high: int) -> int:
    result: int = 0
    saved = single_addition(low)
    for i in range(low, high):
        result += saved(i)
```

Now, let's wrap that up again:

```Python
def actually_time_single_addition_cached() -> int:
    return time_single_addition_cached(1, 100)
```

I don't think that there is any slight-of-hand here, but keep me honest.

### Let's Get A Recount

Well, now that we have another contender, let's rerun those tests:

| actually_time_single_addition | actually_time_single_addition_cached | actually_time_addition |
| -- | -- | -- |
| 14.697342087514699 | 4.129309005104005 | 3.287275522015989 |
