#!/usr/bin/env python3
"""Simple Pagination"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a requested page index

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The page size. Defaults to 10.

        Returns:
            List[List]: Returns a list of data with respect
            to requested index and page no
        """
        # Assert that page and page_size are integers and greater than 0
        assert isinstance(page, int)
        assert page > 0

        assert isinstance(page_size, int)
        assert page_size > 0

        # get the data range
        data_range = index_range(page, page_size)
        # get data set from method
        dataset = self.dataset()

        try:
            # get data range into data set
            paginated_data_set = dataset[data_range[0]:data_range[1]]

            return paginated_data_set
        except IndexError:
            return []
