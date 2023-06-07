"""
Flips the i-th bit in num and return the result.

For example flipBit(5, 0) = 4 since 101 -> 100.
"""
def flipBit(num, i):
    return num ^ 1 << i

"""
Checks if the i-th bit in num is set.

For example checkBit(5, 0) = True since 101 (0-th bit is 1).
"""
def checkBit(num, i):
    return (num & 1 << i) != 0