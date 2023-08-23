/*
 * integer_square_root is *like* a function. X and Y are
 * technically called variables, but they are not like
 * variables which you have seen before. The code after the
 * :- is like the body of the function. The , can be read
 * as "and". The "is" is a special way to assign a value
 * to the variable X (in the sense that variables can be
 * "assigned" values in Prolog).
 */
integer_square_root(X, Y) :- between(0, X, Y), X is Y*Y.
