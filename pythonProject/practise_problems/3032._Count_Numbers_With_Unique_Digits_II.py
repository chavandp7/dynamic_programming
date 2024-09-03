# 3032. Count Numbers With Unique Digits II
# Given two positive integers a and b, return the count of numbers having unique digits in the range [a, b] (inclusive).
class Solution:
    def numberCount(self, a: int, b: int) -> int:
        unique_numbers = 0

        for num in range(a, b + 1):
            is_unique = True
            digits = set()
            while num > int(0):
                last = num % 10
                if last in digits:
                    is_unique = False
                    break

                digits.add(last)
                num = int(num / 10)

            if is_unique:
                unique_numbers += 1

        return unique_numbers


if __name__ == "__main__":
    a, b = 1, 20
    solution = Solution()
    print(f"number count - {solution.numberCount(a, b)}")
