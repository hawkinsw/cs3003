"""
A quintessentially imperative program.
"""

# The defining form of abstraction in an imperative programming
# language is procedural (a.k.a. process) abstraction: a way to
# specify a process without providing the details of how the process is performed.
def sum_evens(low, high):

    # Variable + assignment statement: The imperative way of updating state
    # in an imperative program.
    sum = 0

    # Loops are the imperative way of defining repeated execution of a series
    # of statements.
    for i in range(low, high):
        # The typical form of selection statement (Sebesta: A selection statement
        # provides the means of choosing between two or more execution paths in a
        # program). The if statement is a two-way selection statement (per Sebesta).
        if i % 2 == 0:
            # sum + i is an expression - the fundamental means of specifying computations
            # in a programming language (Sebesta).
            sum = sum + i
    return sum


if __name__ == "__main__":
    # 2 + 4
    sum_of_evens_bw_one_five = sum_evens(1, 5)
    print(f"{sum_of_evens_bw_one_five=}")
