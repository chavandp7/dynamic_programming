# 213. House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money
# you can rob tonight without alerting the police.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_house(nums: List[int]) -> int:
            n = len(nums)
            if n == 1:
                return nums[0]

            dp = [float('-infinity')] * n

            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])

            for index in range(2, n):
                dp[index] = max(dp[index - 1], dp[index - 2] + nums[index])

            return dp[n - 1]

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(rob_house(nums[0: n - 1]), rob_house(nums[1:n]))


if __name__ == "__main__":
    # nums = [2, 3, 2]
    # nums = [1, 2, 3, 1]
    nums = [1, 2, 3]
    solution = Solution()
    print(f"result - {solution.rob(nums)}")
