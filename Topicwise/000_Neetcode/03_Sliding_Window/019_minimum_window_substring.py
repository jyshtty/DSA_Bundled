from collections import Counter, defaultdict

# Minimum Window Substring (sliding window, two pointers)
# Time: O(|s| + |t|)   Space: O(|s| + |t|)

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Edge case: nothing to search in, or nothing to look for
        if not s or not t:
            return ""

        # need: how many of each character the window must contain
        need = Counter(t)
        # window: how many of each character the current window contains
        window = defaultdict(int)

        # required: number of distinct characters in t that must be satisfied
        required = len(need)
        # formed: number of distinct characters whose count in window >= need
        formed = 0

        # l is the left edge of the window; r (below) is the right edge
        l = 0
        # Track the smallest valid window found so far
        min_len = float("inf")
        ans = ""

        # Expand the window by moving the right pointer
        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            # This character just reached its required count
            if char in need and window[char] == need[char]:
                formed += 1

            # While the window is valid, shrink it from the left to minimize it
            while formed == required:

                # Record the window if it is smaller than the best so far
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l:r+1]

                # Remove the leftmost character from the window
                left_char = s[l]
                window[left_char] -= 1

                # Removing it dropped a needed character below its required count,
                # so the window is no longer valid
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                l += 1

        # ans stays "" if no valid window exists
        return ans
