import pytest

from .reverse_list_of_chars import recursive_reverse, loop_reverse


@pytest.mark.parametrize(
    "method, list_of_chars, reversed_list_of_chars",
    [
        [recursive_reverse, [], []],
        [recursive_reverse, ["A"], ["A"]],
        [recursive_reverse, ['A', 'B', 'C', 'D', 'E'], ['E', 'D', 'C', 'B', 'A']],
        [loop_reverse, [], []],
        [loop_reverse, ["A"], ["A"]],
        [loop_reverse, ['A', 'B', 'C', 'D', 'E'], ['E', 'D', 'C', 'B', 'A']]
    ]
)
def test_reverse(method, list_of_chars, reversed_list_of_chars):
    assert method(list_of_chars) == reversed_list_of_chars
