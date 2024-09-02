# 1025. Divisor Game
# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
#
#     Choosing any x with 0 < x < n and n % x == 0.
#     Replacing the number n on the chalkboard with n - x.
#
# Also, if a player cannot make a move, they lose the game.
#
# Return true if and only if Alice wins the game, assuming both players play optimally.
import math


class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

    def divisorGame_dp(self, n: int) -> bool:
        def dp(n: int) -> int:
            if n == 1:
                return False

            if memo[n] != -1:
                return memo[n] == 1

            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    if not dp(n - i):
                        memo[n] = 1
                        memo[n - i] = 0
                        return True

            memo[n] = 0
            return False

        memo = [-1] * (n + 1)
        return dp(n)


if __name__ == "__main__":
    n = 50
    solution = Solution()
    print(f"divisor game - {solution.divisorGame(n)}")
