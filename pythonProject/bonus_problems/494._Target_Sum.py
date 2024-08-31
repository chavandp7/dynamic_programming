# 494. Target Sum
# You are given an integer array nums and an integer target.
#
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and
# then concatenate all the integers.
#
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them
# to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.
from typing import List
from unittest import removeResult


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dp(nums, index, sum, target, total):
            if index == len(nums):
                if sum == target:
                    return 1
                return 0

            if memo[index][sum + total] != float('-infinity'):
                return memo[index][sum + total]

            add = dp(nums, index + 1, sum + nums[index], target, total)
            sub = dp(nums, index + 1, sum - nums[index], target, total)

            memo[index][sum + total] = add + sub
            return add + sub

        total = sum(nums)
        n = len(nums)
        memo = [[float('-infinity')] * (2 * total + 1) for _ in range(n)]
        return dp(nums, 0, 0, target, total)


if __name__ == "__main__":
    nums, target = [1, 1, 1, 1, 1], 3
    # nums, target = [1], 1
    solution = Solution()
    print(f"target sum ways - {solution.findTargetSumWays(nums, target)}")
