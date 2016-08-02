def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

# >>> for n in fib(1000):
#     print(n, end=' ')

    
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
# >>> list(fib(1000))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]