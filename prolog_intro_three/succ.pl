add(X, 0, X).
add(X, succ(Y), succ(Z)) :- add(X, Y, Z).

mult(succ(0), Y, Y).
mult(succ(X), Y, Z) :- mult(X, Y, Zp), add(Y, Zp, Z).

subt(A, B, C) :- add(B, C, A).
div(A, B, C) :- mult(B, C, A).
