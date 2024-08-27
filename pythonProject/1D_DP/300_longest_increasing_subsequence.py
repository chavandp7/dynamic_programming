# 300. Longest Increasing Subsequence
# Given an integer array nums, return the length of the
# longest strictly increasing subsequence
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            lis = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    lis = max(lis, dp[j] + 1)
            dp[i] = lis

        maximum = float('-infinity')
        for i in range(n):
            maximum = max(maximum, dp[i])

        return maximum


if __name__ == "__main__":
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [0, 1, 0, 3, 2, 3]
    nums = [7, 7, 7, 7, 7, 7, 7]
    solution = Solution()
    print(f"LIS for input is {solution.lengthOfLIS(nums)}")
