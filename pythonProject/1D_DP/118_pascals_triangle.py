# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = list()
        row = [1]

        result.append(row)
        if numRows == 1:
            return result

        row = [1, 1]
        result.append(row)
        if numRows == 2:
            return result

        prev = list(row)
        for i in range(3, numRows + 1):
            row = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    row.append(1)
                else:
                    row.append(prev[j] + prev[j - 1])
            result.append(row)
            prev = list(row)

        return result


if __name__ == "__main__":
    numRows = 5
    solution = Solution()
    print(f"Pascal triangles for {numRows} is {solution.generate(numRows)}")
