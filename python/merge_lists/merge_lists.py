def merge_lists_slow(list_a, list_b):
    return sorted(list_a + list_b)


def merge_lists_fast(list_a, list_b):
    merged_list = [None] * (len(list_a) + len(list_b))
    len_a, len_b, merged_len = len(list_a), len(list_b), len(merged_list)
    ind_a, ind_b, merged_ind = 0, 0, 0
    while merged_ind < merged_len:
        if ind_a < len_a and ind_b < len_b:
            if list_a[ind_a] <= list_b[ind_b]:
                merged_list[merged_ind] = list_a[ind_a]
                ind_a += 1
            else:
                merged_list[merged_ind] = list_b[ind_b]
                ind_b += 1
            merged_ind += 1
        elif ind_a < len_a:
            merged_list[merged_ind:] = list_a[ind_a:]
            return merged_list
        elif ind_b < len_b:
            merged_list[merged_ind:] = list_b[ind_b:]
            return merged_list
    return merged_list
