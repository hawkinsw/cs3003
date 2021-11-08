permutation([], []).
permutation(L, [H|T]) :- append(LL, [H|LR], L), append(LL, LR, LN), permutation(LN, T).
