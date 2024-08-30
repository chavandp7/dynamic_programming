# 63. Unique Paths II
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner
# (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include
# any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to 2 * 109.
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if row + col == 0:
                    obstacleGrid[0][0] = 1
                    continue

                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                    continue

                if row > 0:
                    obstacleGrid[row][col] += obstacleGrid[row - 1][col]

                if col > 0:
                    obstacleGrid[row][col] += obstacleGrid[row][col - 1]

        return obstacleGrid[m - 1][n - 1]


if __name__ == "__main__":
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # obstacleGrid = [[0, 1], [0, 0]]
    solution = Solution()
    print(f"unique paths with obstacles - {solution.uniquePathsWithObstacles(obstacleGrid)}")
