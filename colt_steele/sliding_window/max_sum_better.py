def max_subbarray_sum(arr: list, num: int) -> float:
    if not arr:
        return None

    # get the intial sum
    # this is O(n)
    temp_sum = 0
    for i in range(0, num, 1):
        temp_sum += arr[i]
    max_sum = temp_sum
    j = i + 1

    # move the sliding window
    # this is also O(n)
    while True:
        if j >= len(arr):
            return max_sum
        else:
            temp_sum = temp_sum + arr[j] - arr[j - num]
            max_sum = max(temp_sum, max_sum)
            j = j + 1


# time complexity = n x k = n2
if __name__ == '__main__':
    result = max_subbarray_sum([4, 2, 1, 6, 2], 4)
    print(result)
