# 338. Counting Bits
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number
# of 1's in the binary representation of i.
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = dp[int(i / 2)]
            else:
                dp[i] = dp[int(i / 2)] + 1

        return dp


if __name__ == "__main__":
    n = 7
    solution = Solution()
    print(f"countBits - {solution.countBits(n)}")
