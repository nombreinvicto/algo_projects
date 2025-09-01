def valid_anagram(astr: str, bstr: str) -> bool:
    if len(astr) != len(bstr):
        return False

    # initialise the frequency counter dicts and then populate them
    astr_freq_dict = {}
    bstr_freq_dict = {}
    for char in astr:
        astr_freq_dict[char] = astr_freq_dict.get(char, 0) + 1
    for char in bstr:
        bstr_freq_dict[char] = bstr_freq_dict.get(char, 0) + 1

    for char, freq in astr_freq_dict.items():
        if not bstr_freq_dict.get(char):
            return False
        if freq != bstr_freq_dict.get(char):
            return False
    return True


if __name__ == '__main__':
    print(valid_anagram("texttwisttime", "timetwisttext"))
