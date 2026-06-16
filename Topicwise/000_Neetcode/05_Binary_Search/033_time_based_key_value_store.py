"""
Problem: Time Based Key-Value Store
Link: https://leetcode.com/problems/time-based-key-value-store/

Description:
    Design a time-based key-value store that can store multiple values
    for the same key at different timestamps and retrieve the value at
    a specific timestamp.
    - set(key, value, timestamp): stores the key-value pair.
    - get(key, timestamp): returns the value set at the largest timestamp
      <= given timestamp. Returns "" if none exists.

Examples:
    set("foo", "bar", 1)
    get("foo", 1)  -> "bar"
    get("foo", 3)  -> "bar"
    set("foo", "bar2", 4)
    get("foo", 4)  -> "bar2"
    get("foo", 5)  -> "bar2"

Constraints:
    1 <= key.length, value.length <= 100
    1 <= timestamp <= 10^7
    set timestamps are strictly increasing per key.
"""

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> [(timestamp, value), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store.get(key, [])
        # binary search for the largest timestamp <= given timestamp
        left, right = 0, len(entries) - 1
        result = ""

        while left <= right:
            mid = left + (right - left) // 2
            if entries[mid][0] <= timestamp:
                result = entries[mid][1]  # valid candidate; try to find a later one
                left = mid + 1
            else:
                right = mid - 1

        return result
