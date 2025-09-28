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

if __name__ == '__main__':

    print(reverse("awesome"))
    print(reverse("rithmschool"))

