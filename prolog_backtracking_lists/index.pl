idx(X, [X|_], StartIndex, StartIndex).
idx(X, [_|Xs], StartIndex, FoundIndex) :- 
	NewStartIndex is StartIndex + 1,
	idx(X, Xs, NewStartIndex, FoundIndex).
