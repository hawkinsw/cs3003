is_sort([]).
is_sort([_]).
is_sort([X,Y|R]) :- X < Y, is_sort([Y|R]).

permute([],[]).
permute([H|T],S) :- permutation(T,P),append(X,Y,P),append(X,[H|Y],S).

my_sort(X, Y) :- permute(X, Y), is_sort(Y).
