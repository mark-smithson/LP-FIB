from functools import reduce


def count_unique(L):
    return len(set(L))


def remove_duplicates(L):
    return set(L)


def flatten(L):
    def concat(L1, L2): return L1 + L2
    return reduce(concat, L, [])


def flatten_rec(L):
    if len(L) == 0:
        return L
    if isinstance(L[0], list):
        return flatten_rec(L[0]) + flatten_rec(L[1:])
    return L[:1] + flatten_rec(L[1:])