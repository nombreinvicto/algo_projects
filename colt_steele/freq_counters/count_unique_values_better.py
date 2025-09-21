def count_unique_values(arr: list):
    # assuming the input array is sorted
    count = 0
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1

    val_set = set()
    for val in arr:
        val_set.add(val)

    print(len(val_set))
    return len(val_set)


# %% ##################################################################

count_unique_values([1, 1, 1, 1, 1, 2])
count_unique_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13])
count_unique_values([])
count_unique_values([-2, -1, -1, 0, 1])
count_unique_values([1, 2, 3, 1, 4])
