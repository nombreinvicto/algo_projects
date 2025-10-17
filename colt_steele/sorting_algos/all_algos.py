def swap(arr, idx1, idx2):
    """
    :param arr: the array/list supplied
    :param idx1: element at idx1 to be swapped to idx2
    :param idx2: element at idx2 to be swapped to idx1
    :return: no need to return, list mutated inplace
    """
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


def bubble_sort(arr):
    # let start i from len(arr) which is 1 + max possible index
    # doing this so that j can go from 0 to i-2 inclusive
    # so j + 1 will be 1 to i-1 inclusive
    # we want the i-th position to be blocked off after every pass as it will be sorted
    called_swap = False
    for i in range(len(arr), -1, -1):
        for j in range(0, i - 1, 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                called_swap = True
        print(f"[INFO] completed 1 pass......")
        print(f"i : {i}, j : {j}")
        print(arr)
        print("=" * 50)

        if called_swap:
            print(f"[INFO] swap called in last pass......")
            called_swap = not called_swap
        else:
            # we did not call swap
            print(f"[INFO] swap NOT called in last pass......")
            break


def selection_sort(arr: list):
    print(f"starting with: {arr}")

    for i in range(0, len(arr), 1):

        for j in range(i, len(arr), 1):
            if j == 0:
                current_min_index = j
            if arr[current_min_index] > arr[j]:
                current_min_index = j
            elif arr[current_min_index] < arr[j]:
                current_min_index = current_min_index
            else:
                pass
        # after 1 pass swap
        print("one pass completed", i, j, current_min_index)
        if i != current_min_index:
            print("calling swap")
            swap(arr,idx1=i, idx2=current_min_index)
            print(arr)
            print("=" * 50)


if __name__ == '__main__':
    # print(bubble_sort([42, 7, 91, 3, 56, 12, 88, 25, 1, 67,
    #                    34, 73, 8, 54, 29, 15, 61, 2, 48, 90,
    #                    19, 33, 77, 5, 81, 26, 63, 14, 39, 11,
    #                    94, 23, 70, 6, 45, 32, 80, 27, 17, 99,
    #                    9, 68, 13, 58, 47, 36, 4, 65, 18, 53]))
    #print(selection_sort([5, 3, 4, 1, 2, 0, 9, 3, 2, 1]))

    print(selection_sort([42, 7, 91, 3, 56, 12, 88, 25, 1, 67,
                       34, 73, 8, 54, 29, 15, 61, 2, 48, 90,
                       19, 33, 77, 5, 81, 26, 63, 14, 39, 11,
                       94, 23, 70, 6, 45, 32, 80, 27, 17, 99,
                       9, 68, 13, 58, 47, 36, 4, 65, 18, 53]))
