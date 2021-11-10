prefix([], _).
prefix([H|Xs], [H|Ys]) :- prefix(Xs, Ys).

prefix_append(Xs, Ys) :- append(Xs, _, Ys).

suffix(Xs, Xs).
suffix(Xs, [_|Ys]) :- suffix(Xs, Ys).

suffix_append(Xs, Ys) :- append(_, Xs, Ys).
