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

    minOp = [float('inf')] * (n + 1)
    minOp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                minOp[i] = min(minOp[i], minOp[j] + (i // j))

    return minOp[n]
