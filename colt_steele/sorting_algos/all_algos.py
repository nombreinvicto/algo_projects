def bubble_sort(arr):
    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    print(arr)
    for i in range(len(arr) - 1, -1, -1):
        called_swap = False
        for j in range(0, i, 1):
            print(i, j)
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                called_swap = True
                print("swap called")
            print(f"[INFO] array after pass: {arr}......")
            print("=" * 50)
        if not called_swap:
            return arr



if __name__ == '__main__':
    print(bubble_sort([29, 10, 9, 5, 37, 18]))
