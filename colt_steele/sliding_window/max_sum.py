def max_subbarray_sum(arr: list, num: int) -> float:
    i = 0
    max_sum = 0
    # loop is O(n)
    while i < len(arr):
        # slicing is O(k)
        subset = arr[i:i + num]
        loop_sum = sum(subset)
        if loop_sum > max_sum:
            max_sum = loop_sum
        i += 1
    return max_sum

# time complexity = n X k = n2
if __name__ == '__main__':
    result = max_subbarray_sum([], 4)
    print(result)
