def recursive_reverse(list_of_chars):
    if list_of_chars == []:
        return list_of_chars
    return recursive_reverse(list_of_chars[1:]) + [list_of_chars[0]]


def loop_reverse(chars):
    l_ind, r_ind = 0, len(chars) - 1
    while l_ind < r_ind:
        chars[l_ind], chars[r_ind] = chars[r_ind], chars[l_ind]
        l_ind += 1
        r_ind -= 1
    return chars
