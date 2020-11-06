def confirm_fcfs(list_a, list_b, merged_list):
    ind_a, ind_b = 0, 0
    len_a, len_b = len(list_a), len(list_b)
    for item in merged_list:
        if ind_a <= len_a-1 and item == list_a[ind_a]:
            ind_a += 1
        elif ind_b <= len_b-1 and item == list_b[ind_b]:
            ind_b += 1
        else:
            return False
    if ind_a != len_a or ind_b != len_b:
        return False
    return True
