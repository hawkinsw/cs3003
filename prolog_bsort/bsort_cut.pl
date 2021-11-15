bsort_cut(Unsorted, Sorted):- 
  append(Left, [A, B | Right], Unsorted),
  B<A,
  !,
  append(Left, [B, A | Right], MoreSorted),
  bsort_cut(MoreSorted, Sorted).
bsort_cut(Sorted, Sorted).
