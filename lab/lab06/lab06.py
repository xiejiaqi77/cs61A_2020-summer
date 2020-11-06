this_file = __file__


def make_adder_inc(a):  # ok
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def adder(b):
        nonlocal a
        results = a + b
        a = a + 1
        return results
    return adder



"""
adder1 = make_adder_inc(5)
adder2 = make_adder_inc(6)
print(adder1(2))
print(adder1(2))
"""


def make_fib(): # ok
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    a = 0
    b = 1
    c = 1
    def next_call():
        nonlocal a, b, c
        result = a
        a, b, c= b, c, b+c
        return result
    return next_call




def insert_items(lst, entry, elem, i=0):   # ok
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    if i == len(lst)-1:
        if lst[i] == entry:
            lst.append(elem)
            return lst
        else:
            return lst
    else:
        if lst[i] == entry:
            lst.insert(i+1, elem)
            i = i + 2
            return insert_items(lst, entry, elem, i)
        else:
            i = i + 1
            return insert_items(lst, entry, elem, i)

test_lst = [1, 5, 8, 5, 2, 3]
new_lst = insert_items(test_lst, 5, 7)
print(new_lst)


