#lang racket
(define a 0)
(define (myif c t f) (cond (c t) (else f)))
; (define (myif c t f) (cond (c (force t)) (else (force f))))
; (myif #t 1 (/ 1 a))
; (myif #f 1 (/ 1 a))
; (myif #t 1 (delay (/ 1 a)))
; (myif #f 1 (delay (/ 1 a)))
