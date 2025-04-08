from functools import lru_cache
import datetime


def fibonacci_recursion(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


memo = {0: 0, 1: 1}


def fibonacci_memo(n):
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]


@lru_cache(maxsize=128)
def fibonacci_cache(n):
    return fibonacci_recursion(n)


print(datetime.datetime.now())
print(fibonacci_recursion(35))
print(datetime.datetime.now())
print(fibonacci_recursion(35))
print(datetime.datetime.now())
print(fibonacci_memo(900))
print(datetime.datetime.now())
print(fibonacci_cache(35))
print(datetime.datetime.now())
print(fibonacci_cache(35))
print(datetime.datetime.now())

