# Uses python3
# memoization

cache = {}

def fib(n):
    if n in cache:
        
        return cache[n]
    if n == 0:
        value = 0

    elif n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n>2:
        value = fib(n-1) + fib(n-2)
    
        cache[n] = value
    return value


n = int(input())
print(fib(n))