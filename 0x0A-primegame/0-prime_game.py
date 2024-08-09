#!/usr/bin/python3
""" Defines `isWinner` and `isPrime` functions """


def isPrime(n):
    """ Check whether n is prime """
    if n <= 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True


def isWinner(x, nums):
    """ Prime Game """
    maria = 0
    ben = 0
    for i in range(0, x):
        m_or_b = True
        for j in range(1, nums[i] + 1):
            if isPrime(j):
                if m_or_b:
                    m_or_b = False
                else:
                    m_or_b = True
        if m_or_b:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
