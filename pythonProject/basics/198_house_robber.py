# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on
# the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum
# amount of money you can rob tonight without alerting the police.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        # base cases
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[1], dp[0])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[n - 1]


if __name__ == "__main__":
    # nums = [1, 2, 3, 1]
    # nums = [2, 7, 9, 3, 1]
    nums = [10, 2, 2, 25, 13]

    solution = Solution()
    print(f"maximum amount that can be robbed is {solution.rob(nums)}")
