route(cvg, bwi).
route(cvg, mdw).
route(cvg, den).
route(cvg, rsw).
route(cvg, mco).
route(cvg, phx).
route(cvg, srq).
route(cvg, tpa).

route(bwi, atl).
route(bwi, bos).
route(bwi, las).

route(phx, pdx).
route(phx, okc).
route(phx, hnl).

route(las, lax).
route(las, lih).

reaches(X, Y, Y) :- route(X, Y).
reaches(X, Y, A) :- route(X, A), reaches(A, Y, _).
