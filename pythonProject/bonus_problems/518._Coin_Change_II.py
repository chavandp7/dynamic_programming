# 518. Coin Change II
# You are given an integer array coins representing coins of different denominations and an integer amount representing
# a total amount of money.
#
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by
# any combination of the coins, return 0.
#
# You may assume that you have an infinite number of each kind of coin.
#
# The answer is guaranteed to fit into a signed 32-bit integer.
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 0

        dp = [0] * (amount + 1)
        dp[0] = 0

        for value in range(1, amount + 1):
            for coin in coins:
                if value >= coin:
                    dp[value] = dp[value] + 1 + dp[value - coin]

        return dp[amount]
