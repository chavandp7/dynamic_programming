# 931. Minimum Falling Path Sum
# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
#
# A falling path starts at any element in the first row and chooses the element in the next row that is
# either directly below or diagonally left/right. Specifically, the next element from position (row, col)
# will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0:
                    dp[row][col] = matrix[row][col]
                    continue

                ans = dp[row - 1][col]
                if col > 0:
                    ans = min(ans, dp[row - 1][col - 1])

                if col < n - 1:
                    ans = min(ans, dp[row - 1][col + 1])

                dp[row][col] = ans + matrix[row][col]

        result = float('infinity')
        for col in range(n):
            result = min(result, dp[m - 1][col])

        return result


if __name__ == "__main__":
    # matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    matrix = [[-19, 57], [-40, -5]]
    solution = Solution()
    print(f"min falling path sum - {solution.minFallingPathSum(matrix)}")
