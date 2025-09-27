def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_not_recursive(n):
    if n <= 2:
        return 1
    else:
        prev_1 = 1
        prev_2 = 1
        for _ in range(3, n+1, 1):
            prev_1, prev_2 = prev_2, prev_1 + prev_2
        return prev_2


if __name__ == '__main__':
    print(fibonacci(4))
    print(fibonacci(55))
    print(fib_not_recursive(55))
