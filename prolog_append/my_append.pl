my_append([], List, List).
my_append([H|T], List, [H|AppendedList]) :- my_append(T, List, AppendedList).
