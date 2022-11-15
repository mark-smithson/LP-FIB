import math


def absValue(x):
    if x < 0:
        return -x
    else:
        return x


def power(x, p):
    res = 1
    for i in range(0, p):
        res *= x
    return res


def isPrime(x):
    if x <= 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def slowFib(n):
    if n < 2:
        return n
    else:
        return slowFib(n-1) + slowFib(n-2)


def quickFib(n):
    if n < 2:
        return n

    n1 = 0
    n2 = 1

    for i in range(2,n):
        n1a = n1
        n1 = n2
        n2 += n1a

    return n1 + n2
