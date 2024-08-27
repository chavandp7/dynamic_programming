# 322. Coin Change
# You are given an integer array coins representing coins of different denominations and an integer amount
# representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
# any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = len(coins)
        infinity = float('infinity')
        dp = [infinity] * (amount + 1)

        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(n):
                value = coins[j]
                if i >= value:
                    dp[i] = min(dp[i], dp[i - value] + 1)

        return dp[amount] if dp[amount] != infinity else -1


if __name__ == "__main__":
    # coins, amount = [1, 2, 5], 11
    # coins, amount = [2], 3
    coins, amount = [1], 0
    solution = Solution()
    print(f"minimum coins required are - {solution.coinChange(coins, amount)}")
