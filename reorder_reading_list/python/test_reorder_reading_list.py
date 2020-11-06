import pytest

from .reorder_reading_list import reorder

reading_list = """2009

The Tempest - William Shakespeare

Of Mice and Men - John Steinbeck

Titus Andronicus - William Shakespeare

To Kill a Mockingbird - Harper Lee

The God Delusion - Richard Dawkins

2010

The Selfish Gene - Richard Dawkins

The Sense of an Ending - Julian Barnes

A Brief History of Time - Stephen Hawking

"""

ordered_list = """2010

A Brief History of Time - Stephen Hawking

The Sense of an Ending - Julian Barnes

The Selfish Gene - Richard Dawkins

2009

The God Delusion - Richard Dawkins

To Kill a Mockingbird - Harper Lee

Titus Andronicus - William Shakespeare

Of Mice and Men - John Steinbeck

The Tempest - William Shakespeare
"""


@pytest.mark.parametrize(
    "method, reading_list, ordered_list",
    [
        [reorder, reading_list, ordered_list],
    ],
)
def test_reorder(method, reading_list, ordered_list):
    assert method(reading_list) == ordered_list
