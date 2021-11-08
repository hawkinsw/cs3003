word(abalone,a,b,a,l,o,n,e).
word(abandon,a,b,a,n,d,o,n).
word(enhance,e,n,h,a,n,c,e).
word(anagram,a,n,a,g,r,a,m).
word(connect,c,o,n,n,e,c,t).
word(elegant,e,l,e,g,a,n,t).

crossword(V1, V2, V3, H1, H2, H3) :-
  word(V1, _, V1H1, _, V1H2, _, V1H3, _),
  word(V2, _, V2H1, _, V2H2, _, V2H3, _),
  word(V3, _, V3H1, _, V3H2, _, V3H3, _),
  word(H1, _, V1H1, _, V2H1, _, V3H1, _),
  word(H2, _, V1H2, _, V2H2, _, V3H2, _),
  word(H3, _, V1H3, _, V2H3, _, V3H3, _).
