#!/usr/bin/env python3
"""MRU Caching system demonstration"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A class for LFU (Least Frequently Used) caching system.

    Inherits from BaseCaching and implements LFU eviction strategy
    when the cache reaches its maximum capacity.

    Args:
        BaseCaching (class): Parent class template for caching.

    Attributes:
        access_frequency (dict): Keeps track of the access frequency of keys.
        access_order (list): Tracks the order of key accesses.

    Methods:
        __init__():
            Initializes the LFUCache instance.

        put(key, item):
            Adds or updates an item in the cache.
            Implements LFU eviction strategy when the cache is full.

        get(key):
            Retrieves an item from the cache based on the specified key.
            Updates the access frequency and order of the accessed key.
    """

    def __init__(self):
        """Initializes the LFUCache instance."""
        super().__init__()
        self.frequency = {}  # Frequency counter for each key
        self.usage_order = {}  # Tracks the order of usage for LRU fallback
        self.current_time = 0  # counter to keep track of the order of usage

    def put(self, key, item):
        """Adds or updates an item in the cache.

        If the cache is full (reaches BaseCaching.MAX_ITEMS):
        - Discards the least frequently used item (LFU).
        - If multiple items have the same frequency, uses LRU to decide.

        Args:
            key (str): The key to add or update in the cache.
            item (any): The item to add or update in the cache.
        """
        if key is None or item is None:
            return

        # Add or update the item in the cache
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order[key] = self.current_time
            self.current_time += 1
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the least frequently used item
            lfu_key = min(self.frequency,
                          key=lambda k: (self.frequency[k],
                                         self.usage_order[k]))
            print(f"DISCARD: {lfu_key}")
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            del self.usage_order[lfu_key]

        self.cache_data[key] = item
        self.frequency[key] = 1
        self.usage_order[key] = self.current_time
        self.current_time += 1

    def get(self, key):
        """Retrieves an item from the cache based on the specified key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            any: The item associated with the key,
            or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.usage_order[key] = self.current_time
        self.current_time += 1
        return self.cache_data[key]
