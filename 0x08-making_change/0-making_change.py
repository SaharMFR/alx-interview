#!/usr/bin/python3
""" Defines `makeChange` function that uses DP """
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """ Determine the fewest number of coins needed to make the change """
    if total <= 0:
        return 0

    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1
