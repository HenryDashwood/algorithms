import pytest

from .confirm_fcfs import confirm_fcfs


@pytest.mark.parametrize(
    "list1, list2, merged_list, result",
    [
        [[1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6], True],
        [[1, 5], [2, 3, 6], [1, 2, 6, 3, 5], False],
        [[], [2, 3, 6], [2, 3, 6], True],
        [[1, 5], [2, 3, 6], [1, 6, 3, 5], False],
        [[1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8], False],
        [[1, 9], [7, 8], [1, 7, 8], False],
        [[55, 9], [7, 8], [1, 7, 8, 9], False],
        [[27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18], True],
    ]
)
def test_confirm_fcfs(list1, list2, merged_list, result):
    assert confirm_fcfs(list1, list2, merged_list) == result
