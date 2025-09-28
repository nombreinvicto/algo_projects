def flatten(array: list) -> list:
    ret_list = []

    def recursive_inner(array: list) -> list:
        if len(array) == 0:
            return

        # O-1
        element = array.pop()
        if isinstance(element, int):
            ret_list.append(element)
            # On
            recursive_inner(array)
        if isinstance(element, list):
            # On
            recursive_inner(element)

            # On
            recursive_inner(array)

    recursive_inner(array)
    ret_list.reverse()
    return ret_list
if __name__ == '__main__':
    print(flatten([1, 2, 3, [4, 5] ]))
    print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))
    print(flatten([1, [2, [3, 4], [[5]]]]))
