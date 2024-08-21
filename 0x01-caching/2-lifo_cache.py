#!/usr/bin/env python3
"""LIFO Caching system demonstration"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A class for LIFO caching system

    Args:
        BaseCaching (Base Class for caching):
        parent class template for caching
    """

    def __init__(self):
        """Constructor initialization
        """
        super().__init__()

    def put(self, key, item):
        """Updates the cache with the given key and item.

        Args:
            key (str): The key to add to the cache.
            item (any): The item to add to the cache.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last item put in cache (LIFO Algorithm)
                # get the last key of the key-val pair
                last_key = list(self.cache_data.keys())[-1]
                print("DISCARD: {}".format(last_key))  # Print DISCARD wt key
                del self.cache_data[last_key]  # Remove the first item
            self.cache_data[key] = item

    def get(self, key):
        """Returns an item from the cache based on the specified key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            any: The item associated with the key,
            or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
