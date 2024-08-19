#!/usr/bin/env python3
"""Python Pagination Backend"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A function that returns a tuple of size two
    containing a start index and an end index corresponding
    to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): The page number to get range
        page_size (int): The page size to return

    Returns:
        Tuple[int, int]: A tuple of size two containing
        start index and end index of the range of indexes
        to return in a list for the pagination parameters
    """
    # configure the page indexes (start and end)
    start_index = (page * page_size) - page_size
    end_index = page * page_size

    return (start_index, end_index)
