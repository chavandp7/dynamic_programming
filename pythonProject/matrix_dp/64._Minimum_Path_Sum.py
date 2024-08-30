# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes
# the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [float('infinity')] * n
        dp[0] = 0

        for row in range(m):
            next_row = [0] * n
            for col in range(n):
                next_row[col] = dp[col]
                if col > 0:
                    next_row[col] = min(next_row[col], next_row[col - 1])
                next_row[col] = next_row[col] + grid[row][col]
            dp = next_row

        return dp[n - 1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # grid = [[1, 2, 3], [4, 5, 6]]
    solution = Solution()
    print(f"minimum path sum - {solution.minPathSum(grid)}")
