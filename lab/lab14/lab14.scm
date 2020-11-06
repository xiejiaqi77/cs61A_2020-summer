(define (split-at lst n)
  'YOUR-CODE-HERE
  (cond ((= n 0) (cons nil lst))
        ((null? lst) (cons lst nil))
		(else (let ((rec (split-at (cdr lst) (- n 1))))
		         (cons (cons (car lst) (car rec)) (cdr rec)))))
)

(define-macro (switch expr cases)
	(cons 'cond
		(map (lambda (case) (cons `(equal? ,expr (quote ,(car case))) (cdr case)))
    			cases))
)
