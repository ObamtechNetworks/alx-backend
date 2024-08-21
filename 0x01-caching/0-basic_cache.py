#!/usr/bin/env python3
"""Basoc Caching Illustration"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A Basic Caching System

    Args:
        BaseCaching (type: base class): Base caching model
    """
    def __init__(self):
        """Use the Baseclass constructor to initialize class
        """
        super().__init__()  # inherits self.cache_data

    def put(self, key, item):
        """Updates or Adds values to the cache

        Args:
            key (str): A string or pointer for values in a dictionary
            item (any): values to be put in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets a specific item based on key in a cache

        Args:
            key (str): pointer to the item to get
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
