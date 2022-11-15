def my_map(f, L):
    return [f(value) for value in L]


def my_filter(f, L):
    return [value for value in L if f(value)]


def factors(n):
    return [value for value in range(1, n + 1) if n % value == 0]


def triplets(n):
    return [(a, b, c) for a in range(1, n + 1) for b in range(1, n + 1) for c in range(1, n + 1)
                                                                                if a ** 2 + b ** 2 == c ** 2]
