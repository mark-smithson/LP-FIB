from functools import reduce


def evens_product(L):
    evens = [x for x in L if x % 2 == 0]
    return reduce((lambda x, y: x * y), evens, 1)


def reverse(L):
    def invertir(x, y): return [y] + x
    return reduce(invertir, L, [])


def zip_with(f, L1, L2):
    return [f(a, b) for (a,b) in zip(L1,L2)]


def count_if (f, L):
    return len([x for x in L if f(x)])
