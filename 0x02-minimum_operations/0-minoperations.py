#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    In a text file, there is a single character `H`. The text editor
    can execute only two operations in this file: `Copy All` and `Paste`.
    Given a number `n`, it calculates the fewest number of operations needed
    to result in exactly `n` `H` characters in the file.
    If `n` is impossible to achieve, it returns 0.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n /= factor
        factor += 1

    return operations
