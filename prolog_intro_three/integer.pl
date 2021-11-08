generate_integer(0).
generate_integer(X) :- generate_integer(Y), X is Y + 1.
