#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns list of lists of integers representing
    the Pascal's triangle of `n`.
    """
    triangle = []

    if n <= 1:
        return triangle

    for i in range(1, n + 1):
        triangle.append([])
        for j in range(1, i + 1):
            if j == 1 or i == 1 or j == i:
                triangle[i - 1].append(1)
            else:
                triangle[i - 1].append(triangle[i - 2][j - 2] + triangle[i - 2][j - 1])

    return triangle
