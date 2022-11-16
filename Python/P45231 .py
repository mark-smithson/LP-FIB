def fibs():
    a = 0
    yield a
    b = 1
    while True:
        yield b
        a, b = b, a + b


def roots(x):
    a = x
    yield a
    b = 0.5*(a + x/a)
    while True:
        yield b
        a, b = b, 0.5*(b + x/b)


def isPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False

        return True


def primes():
    x = 2
    yield x

    while True:
        x += 1
        if isPrime(x):
            yield x


def isHamming(x):
    if x == 1:
        return True
    elif not (x%2 == 0 or x%3 == 0 or x%5 == 0):
        return False
    else:
        return isHamming(x/2) or isHamming(x/3) or isHamming(x/5)


def hammings():
    x = 1
    yield x

    while True:
        x += 1
        if isHamming(x):
            yield x