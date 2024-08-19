#!/usr/bin/env python3
"""Simple Pagination"""

import csv
import math
from typing import List, Tuple, Dict, Any


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
    start_index = (page - 1) * page_size
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
        assert isinstance(page, int) and page > 0

        assert isinstance(page_size, int) and page_size > 0

        # get the data range
        start, end = index_range(page, page_size)
        # get data set from method
        dataset = self.dataset()

        try:
            # get data range into data set
            paginated_data_set = dataset[start:end]

            return paginated_data_set
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns an hypermedia pagination of data

        Args:
            page (int, optional): the current page number. Defaults to 1.
            page_size (int, optional): the requested page number.
            Defaults to 10.

        Returns:
            Dict[str, Any]: Returns a dictionary with values as:
            page_size: the length of the returned dataset page
            page: the current pae number
            data: the dataset page (list of dataset requested)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """

        data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())

        total_pages = math.ceil(dataset_length / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        data_set_dictionary = {
            'page_size': len(data),  # length of the data (page) requested
            'page': page,
            'data': data if data else [],
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return data_set_dictionary
