#!/usr/bin/env python3
"""MRU Caching system demonstration"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A class for MRU (Most Recently Used) caching system.

    Inherits from BaseCaching and implements MRU eviction strategy
    when the cache reaches its maximum capacity.

    Args:
        BaseCaching (class): Parent class template for caching.

    Attributes:
        access_order (list): Keeps track of the access order of keys.

    Methods:
        __init__():
            Initializes the MRUCache instance.

        put(key, item):
            Adds or updates an item in the cache.
            If the cache is full, evicts the most recently used item.

        get(key):
            Retrieves an item from the cache based on the specified key.
            Updates the access order to mark the item as most recently used.
    """

    def __init__(self):
        """Initializes the MRUCache instance."""
        super().__init__()
        self.access_order = []  # Track access order of keys

    def put(self, key, item):
        """Adds or updates an item in the cache.

        If the cache is full (reaches BaseCaching.MAX_ITEMS),
        removes the most recently used item based on access order.

        Args:
            key (str): The key to add or update in the cache.
            item (any): The item to add or update in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the most recently used item
                mru_key = self.access_order.pop()  # Get the last accessed key
                del self.cache_data[mru_key]  # Remove from cache
                print("DISCARD: {}".format(mru_key))  # Print discarded key

            self.cache_data[key] = item  # Add or update item in cache
            self.access_order.append(key)  # Update access order

    def get(self, key):
        """Retrieves an item from the cache based on the specified key.

        Updates the access order to mark the item as most recently used.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            any: The item associated with the key,
            or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            # Update access order: Move key to the end (most recent)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
