#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i]
                                      for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination."""
        # Step 1: Ensure the index is within valid range
        assert index is not None and 0 <= index < len(self.indexed_dataset())

        # Step 2: Fetch the data
        indexed_dataset = self.indexed_dataset()
        data = []
        next_index = index

        for i in range(page_size):
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1

        # Step 3: Construct the response dictionary
        response = {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }

        return response
