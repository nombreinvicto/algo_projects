def bubble_sort(arr):
    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    print(arr)
    for i in range(len(arr) - 1, -1, -1):
        # lets increment j from 0 upto 1 step before ith position
        # because j+1 will be the ith position
        for j in range(0, i, 1):
            print(i, j)
            print(f"comparing : {arr[j]} - {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                print("swap called")
            print(f"[INFO] array after pass: {arr}......")
            print("=" * 50)


if __name__ == '__main__':
    print(bubble_sort([29, 10, 9, 5, 37, 18]))
