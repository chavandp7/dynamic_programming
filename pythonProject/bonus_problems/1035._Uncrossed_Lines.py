# 1035. Uncrossed Lines
# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2
# (in the order they are given) on two separate horizontal lines.
#
# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
#
#     nums1[i] == nums2[j], and
#     the line we draw does not intersect any other connecting (non-horizontal) line.
#
# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).
#
# Return the maximum number of connecting lines we can draw in this way.
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for index_1 in range(m):
            for index_2 in range(n):
                ans = 0
                if nums1[index_1] == nums2[index_2]:
                    ans = 1 + dp[index_1][index_2]

                ans = max(ans, dp[index_1][index_2 + 1])
                ans = max(ans, dp[index_1 + 1][index_2])

                dp[index_1 + 1][index_2 + 1] = ans

        return dp[m][n]


def maxUncrossedLines_top_down(self, nums1: List[int], nums2: List[int]) -> int:
    def dp(index_1, index_2):
        if index_1 == len(nums1) or index_2 == len(nums2):
            return 0

        if memo[index_1][index_2] != float('-infinity'):
            return memo[index_1][index_2]

        ans = 0
        if nums1[index_1] == nums2[index_2]:
            ans = 1 + dp(index_1 + 1, index_2 + 1)

        ans = max(ans, dp(index_1, index_2 + 1))
        ans = max(ans, dp(index_1 + 1, index_2))

        memo[index_1][index_2] = ans
        return ans

    m = len(nums1)
    n = len(nums2)

    memo = [[float('-infinity')] * n for _ in range(m)]
    return dp(0, 0)


if __name__ == "__main__":
    # nums1, nums2 = [1, 4, 2], [1, 2, 4]
    # nums1, nums2 = [2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]
    nums1, nums2 = [1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]

    solution = Solution()
    print(f"max uncrossed lines - {solution.maxUncrossedLines(nums1, nums2)}")
