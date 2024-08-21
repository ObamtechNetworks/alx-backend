#!/usr/bin/env python3
"""LRU Caching system demonstration"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A class for LRU caching system

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
                # Find the least recently used item and remove it
                lru_key = next(iter(self.cache_data))  # get first_key obj
                print("DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]  # rm lru item
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
            # move the accessed item to the end (most recent) of the cache
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
        return None
