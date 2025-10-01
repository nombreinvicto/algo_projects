def capitalize_first(arr: list):
    # stop condition
    if len(arr) == 1:
        return [arr[0].capitalize()]

    element = arr.pop(0)
    return [element.capitalize()] + capitalize_first(arr)


# %% ##################################################################
obj1 = {
    'outer': 2,
    'obj': {
        'inner': 2,
        'otherObj': {
            'superInner': 2,
            'notANumber': True,
            'alsoNotANumber': "yup"}
    }
}

obj2 = {
    'a': 2,
    'b': {'b': 2, 'bb': {'b': 3, 'bb': {'b': 2}}},
    'c': {'c': {'c': 2}, 'cc': 'ball', 'ccc': 5},
    'd': 1,
    'e': {'e': {'e': 2}, 'ee': 'car'}
}


# %% ##################################################################
def nested_even_sum(obj: dict) -> int:
    global_sum = 0

    def inner(obj: dict):
        nonlocal global_sum
        # stopping criteria
        if len(obj) != 0:
            # recursive call with new input
            _, v = obj.popitem()
            if isinstance(v, int) and not isinstance(v, bool):
                global_sum = global_sum + v
                inner(obj)
            if isinstance(v, dict):
                inner(obj)
                inner(v)
            else:
                inner(obj)

    inner(obj)
    return global_sum


if __name__ == '__main__':
    # print(capitalize_first(['car', 'taco', 'banana']))
    print(nested_even_sum(obj2))
