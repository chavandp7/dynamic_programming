# bottom up approach - tabulation

def bottom_up_fibonacci(n):
    # build base cases
    fib = [0] * (n + 1)
    fib[1] = 1

    # iterate and use tabulation to build for nth sequence
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


if __name__ == "__main__":
    n = 10
    print(f"{n}th fibonacci number is {bottom_up_fibonacci(n)}")
