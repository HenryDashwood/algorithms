import pytest

from .merge_lists import merge_lists_slow, merge_lists_fast


@pytest.mark.parametrize(
    "method, list1, list2, merged_list",
    [
        [merge_lists_slow, [], [], []],
        [merge_lists_slow, [], [1, 2, 3], [1, 2, 3]],
        [merge_lists_slow, [5, 6, 7], [], [5, 6, 7]],
        [merge_lists_slow, [2, 4, 6], [1, 3, 7], [1, 2, 3, 4, 6, 7]],
        [merge_lists_slow, [2, 4, 6, 8], [1, 7], [1, 2, 4, 6, 7, 8]],
        [merge_lists_fast, [], [], []],
        [merge_lists_fast, [], [1, 2, 3], [1, 2, 3]],
        [merge_lists_slow, [5, 6, 7], [], [5, 6, 7]],
        [merge_lists_fast, [2, 4, 6], [1, 3, 7], [1, 2, 3, 4, 6, 7]],
        [merge_lists_fast, [2, 4, 6, 8], [1, 7], [1, 2, 4, 6, 7, 8]]
    ]
)
def test_merge_list(method, list1, list2, merged_list):
    assert method(list1, list2) == merged_list
