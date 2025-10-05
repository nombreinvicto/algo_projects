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


def naive_string_search(long_str: str, short_str: str):
    for i, _ in enumerate(long_str):
        for j, _ in enumerate(short_str):
            try:
                if short_str[j] == long_str[i + j]:
                    continue
                else:
                    break
            except IndexError:
                # this will never happen
                return False
        else:
            # this will only happen if all characters have matched
            return True
    return False


if __name__ == '__main__':
    print(naive_string_search("lorie loled", "lol"))
    print(naive_string_search("lorie loled", "ed"))
    print(naive_string_search("lorie loled", "sucre"))
    print(naive_string_search("lorie loled", "d"))
    print(naive_string_search("lorie loled", "ie "))
