def myLength(L):
    return len(L)


def myMaximum(L):
    return max(L)


def average(L):
    return sum(L) / len(L)


def buildPalindrome(L):
    return L[::-1] + L


def remove(L1, L2):
    return [value for value in L1 if value not in L2]


def flatten(L):
    if len(L) == 0:
        return L
    if isinstance(L[0], list):
        return flatten(L[0]) + flatten(L[1:])
    return L[:1] + flatten(L[1:])


def oddsNevens(L):
    evens = [value for value in L if value % 2 == 0]
    odds = [value for value in L if value % 2 != 0]

    return odds, evens


def primeDivisors(n):
    def isPrime(x):
        if x <= 1:
            return False

        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    return [value for value in list(range(1, n + 1)) if n % value == 0 and isPrime(value)]
