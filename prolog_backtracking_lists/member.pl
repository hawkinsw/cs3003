my_member(X, [X|_]).
my_member(X, [_|T]) :- my_member(X, T).
