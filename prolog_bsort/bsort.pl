bsort(Unsorted, Sorted):- 
  append(Left, [A, B | Right], Unsorted),
  B<A,
  append(Left, [B, A | Right], MoreSorted),
  bsort(MoreSorted, Sorted).
bsort(Sorted, Sorted).
