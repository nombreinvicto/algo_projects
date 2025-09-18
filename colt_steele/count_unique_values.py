def count_unique_values(arr: list):
    # assuming the input array is sorted
    count = 0
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1

    count += 1
    left_pointer = 0
    right_pointer = 1

    while right_pointer < len(arr):
        left_value = arr[left_pointer]
        right_value = arr[right_pointer]
        if left_value != right_value:
            count += 1
        right_pointer += 1
        left_pointer += 1
    print(count)
    return count


# %% ##################################################################

count_unique_values([1, 1, 1, 1, 1, 2])
count_unique_values([1,2,3,4,4,4,7,7,12,12,13])
count_unique_values([])
count_unique_values([-2,-1,-1,0,1])
count_unique_values([1,2,3,1,4])
