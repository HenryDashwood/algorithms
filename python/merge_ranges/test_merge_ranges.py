import pytest

from .merge_ranges import merge_ranges


@pytest.mark.parametrize(
    "meetings, merged_meetings",
    [
        [[(1, 3), (2, 4)], [(1, 4)]],
        [[(5, 6), (6, 8)], [(5, 8)]],
        [[(1, 8), (2, 5)], [(1, 8)]],
        [[(1, 3), (4, 8)], [(1, 3), (4, 8)]],
        [[(1, 4), (2, 5), (5, 8)], [(1, 8)]],
        [[(5, 8), (1, 4), (6, 8)], [(1, 4), (5, 8)]],
        [[(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)], [(1, 12)]],
        [[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)], [(0, 1), (3, 8), (9, 12)]]
    ]
)
def test_merge_ranges(meetings, merged_meetings):
    assert merge_ranges(meetings) == merged_meetings
