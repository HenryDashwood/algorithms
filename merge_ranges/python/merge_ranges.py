def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)
    merged = [sorted_meetings[0]]
    for current_start, current_end in sorted_meetings[1:]:
        last_merged_start, last_merged_end = merged[-1]
        if current_start <= last_merged_end:
            merged[-1] = (last_merged_start, max(last_merged_end, current_end))
        else:
            merged.append((current_start, current_end))
    return merged
