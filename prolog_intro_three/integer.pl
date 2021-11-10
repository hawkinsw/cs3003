generate_integer(0).
generate_integer(X) :- generate_integer(Y), X is Y + 1.

generate_integer_tr(X) :- next_integer(0,X).

next_integer(J, J).
next_integer(J, L) :- K is J + 1, next_integer(K, L).
