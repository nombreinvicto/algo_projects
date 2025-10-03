def binary_search(arr: list, target: int):
    left_ptr = 0
    right_ptr = len(arr) - 1

    while left_ptr <= right_ptr:
        search_ptr = (left_ptr + right_ptr) // 2
        if left_ptr == right_ptr and target == arr[search_ptr]:
            return left_ptr
        if left_ptr == right_ptr and target != arr[search_ptr]:
            return -1
        if target == arr[search_ptr]:
            return search_ptr
        elif target < arr[search_ptr]:
            right_ptr = search_ptr - 1
        else:
            left_ptr = search_ptr + 1

if __name__ == '__main__':
    print(binary_search([1,2,3,4,5],2))
    print(binary_search([1,2,3,4,5],3))
    print(binary_search([1,2,3,4,5],5))
    print(binary_search([1,2,3,4,5],6))
