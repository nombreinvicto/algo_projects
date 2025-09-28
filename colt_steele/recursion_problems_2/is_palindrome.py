def reverse(astring):
    # O(n)
    alist = list(astring)

    if len(alist) == 0:
        return ""

    if len(alist) == 1:
        return alist[0]
    else:
        # O(n)
        return alist.pop() + reverse(alist)


def is_palindrome(word: str) -> bool:
    reversed_string = reverse(word)
    return reversed_string == word

if __name__ == '__main__':
    print(is_palindrome('amanaplanacanalpanama'))
    print(is_palindrome('amanaplanacanalpandemonium'))
    print(is_palindrome('tacocat'))
