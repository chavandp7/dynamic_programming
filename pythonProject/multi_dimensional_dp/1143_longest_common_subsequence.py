# 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence.
# If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string with some characters
# (can be none) deleted without changing the relative order of the remaining characters.
#
#     For example, "ace" is a subsequence of "abcde".
#
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len1][len2]


if __name__ == "__main__":
    # text1, text2 = "abcde", "ace"
    # text1, text2 = "abc", "abc"
    text1, text2 = "abc", "def"

    solution = Solution()
    print(f"LCS for {text1} and {text2} is - {solution.longestCommonSubsequence(text1, text2)}")
