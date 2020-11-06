(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
	(car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond 
	((< num 0) -1)
        ((= num 0) 0)
        (else 1))
)


(define (square x) (* x x))

(define (pow x y) ;ok
  
   (cond ((= y 0) 1)
        ((even? y) (square (pow x (/ y 2))))  
        (else (* x (pow x (- y 1)))))
)

 
(define (unique s) ; ok
  'YOUR-CODE-HERE
  (if (null? s) nil
      (cons (car s)
      	    (unique (filter (lambda (x) (not (eq? (car s) x))) (cdr s)))))
)


(define (replicate x n) ; ok
  'YOUR-CODE-HERE
  (define (helper x list_so_far k)
         (if (= k 0) list_so_far
             (helper x (append list_so_far (list x)) (- k 1))))
  (helper x nil n)
)


(define (accumulate combiner start n term) ; Ok my god, one time pass
  'YOUR-CODE-HERE
  (if (= n 1) (combiner start (term n))
      (combiner (term n) (accumulate combiner start (- n 1) term)))
)


(define (accumulate-tail combiner start n term) ; ok
  'YOUR-CODE-HERE
   (define (helper x so_far)
           (if (= x 0) so_far
               (helper (- x 1) (combiner (term x) so_far))))
   (helper n start)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)

