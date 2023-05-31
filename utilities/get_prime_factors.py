import math

"""
Prime factor generator.

Generates a list of the prime factors of x.
"""
def primeFactors(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            while x % i == 0:
                x //= i
            yield i
    if x != 1:
        yield x