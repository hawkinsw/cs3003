my_append([], List, List).
my_append([H|T], List, [H|AppendedList]) :- my_append(T, List, AppendedList).

permute([], []).
permute(List, [X|Xs]) :- append(W, [X|U], List),
append(W, U, ListWithoutX),
permute(ListWithoutX, Xs).
