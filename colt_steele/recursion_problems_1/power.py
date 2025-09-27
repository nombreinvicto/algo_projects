def power(base, exponent):
    # base condition
    if exponent == 1:
        return base
    elif exponent <= 0:
        return 1
    else:
        return base * power(base, exponent - 1)


if __name__ == '__main__':
    print(power(2, 3))
    print(power(3, 0))
    print(power(5, 3))
