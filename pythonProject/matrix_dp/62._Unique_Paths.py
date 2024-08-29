# 62. Unique Paths
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach
# the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dp(m: int, n: int):
            if m == 0 or n == 0:
                memo[m][n] = 1
                return 1

            if memo[m][n] != 0:
                return memo[m][n]

            memo[m][n] = dp(m, n - 1) + dp(m - 1, n)
            return memo[m][n]

        memo = [[0] * n for _ in range(m)]
        return dp(m - 1, n - 1)


if __name__ == "__main__":
    # m, n = 3, 7
    m, n = 3, 2
    solution = Solution()
    print(f"unique paths - {solution.uniquePaths(m, n)}")
