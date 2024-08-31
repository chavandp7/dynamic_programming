# 1218. Longest Arithmetic Subsequence of Given Difference
# Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which
# is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
#
# A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order
# of the remaining elements.
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        if n == 1:
            return 1

        dp = dict()
        result = float('-infinity')
        for element in arr:
            prev_seq = dp.get(element - difference, 0)
            dp[element] = prev_seq + 1
            result = max(result, dp[element])

        return result


if __name__ == "__main__":
    # arr, difference = [1, 2, 3, 4], 1
    # arr, difference = [1, 3, 5, 7], 1
    arr, difference = [1, 5, 7, 8, 5, 3, 4, 2, 1], -2

    solution = Solution()
    print(f"longest subsequence - {solution.longestSubsequence(arr, difference)}")
