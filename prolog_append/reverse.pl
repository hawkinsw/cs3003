reverse([], []).
reverse([X|Xs], XsX) :- reverse(Xs, Sx), append(Sx, [X], XsX).
