# top down approach = recursion + memoization-

memo = {}


def top_down_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo.keys():
        return memo[n]

    memo[n] = top_down_fibonacci(n - 1) + top_down_fibonacci(n - 2)
    return memo[n]


if __name__ == "__main__":
    n = 10
    print(f"{n}th fibonacci number is {top_down_fibonacci(n)}")
