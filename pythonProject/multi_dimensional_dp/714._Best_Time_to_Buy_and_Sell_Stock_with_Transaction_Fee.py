# 714. Best Time to Buy and Sell Stock with Transaction Fee
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day,
# and an integer fee representing a transaction fee.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like,
# but you need to pay the transaction fee for each transaction.
#
# Note:
#
#     You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#     The transaction fee is only charged once for each stock purchase and sale.
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        buy = [0] * n
        sell = [0] * n

        # base case
        buy[0] = -prices[0]
        sell[0] = 0

        for i in range(1, n):
            # 2 options for buy - do nothing or buy
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])

            # 2 options for sell - do nothing or sell
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)

        return sell[n - 1]


if __name__ == "__main__":
    prices, fee = [1, 3, 2, 8, 4, 9], 2
    # prices, fee = [1, 3, 7, 5, 10, 3], 3
    solution = Solution()
    print(f"profit is - {solution.maxProfit(prices, fee)}")
