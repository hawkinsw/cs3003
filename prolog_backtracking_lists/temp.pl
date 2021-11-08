membership(Element, [Element|_]).
membership(Element, [_|Tail]) :- membership(Element, Tail).
