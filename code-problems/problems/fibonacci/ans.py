def fib(n):
    first = 0
    second = 1

    while n > 0:
        third = first + second
        first = second
        second = third
        n -= 1

    return third

print fib(4)
    
