"""
Problem: LRU Cache
Link: https://leetcode.com/problems/lru-cache/

Description:
    Design a data structure that follows Least Recently Used (LRU) cache
    eviction policy with O(1) get and put operations.
    - get(key): return value if key exists, else -1.
    - put(key, value): insert/update the key. Evict the LRU key if capacity exceeded.

Examples:
    LRUCache cache = new LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)     -> 1
    cache.put(3, 3)  (evicts key 2)
    cache.get(2)     -> -1
    cache.get(3)     -> 3

Constraints:
    1 <= capacity <= 3000
    0 <= key, value <= 10^4
    At most 2 * 10^5 calls to get and put.
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # OrderedDict maintains insertion order; move_to_end() marks recently used
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # mark as most recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # evict the least recently used (front of dict)
