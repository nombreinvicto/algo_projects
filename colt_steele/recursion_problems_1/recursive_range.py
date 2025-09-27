def recursive_range(num: int) -> int:
    if num == 0:
        return 0
    else:
        return num + recursive_range(num - 1)
if __name__ == '__main__':
    print(recursive_range(6))
    print(recursive_range(10))
