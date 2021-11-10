natural_number(0).
natural_number(succ(X)) :- natural_number(X).

lt(0, succ(_)).
lt(succ(X), succ(Y)) :- lt(X, Y).

add(X, 0, X).
add(X, succ(Y), succ(Z)) :- add(X, Y, Z).

mult(0, _, 0).
mult(succ(X), Y, Z) :- mult(X, Y, Zp), add(Y, Zp, Z).

subt(A, B, C) :- add(B, C, A).
div(A, B, C) :- mult(B, C, A).
