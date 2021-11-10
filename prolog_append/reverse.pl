reverse([], []).
reverse([X|Xs], XsX) :- reverse(Xs, Sx), append(Sx, [X], XsX).

reverse_acc(ToReverse, Reversed) :- reverse_acc_do(ToReverse, [], Reversed).

reverse_acc_do([], Reversed, Reversed).
reverse_acc_do([X|Xs], SoFar, Reversed) :- reverse_acc_do(Xs, [X|SoFar], Reversed).

time_reverse_acc(X, Reversed) :- length(List, X), reverse_acc(List, Reversed).
time_reverse(X, Reversed) :- length(List, X), reverse(List, Reversed).
