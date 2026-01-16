# leetcode problem link: https://leetcode.com/problems/longest-repeating-character-replacement/
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "

# Approach: Sliding Window
# Use a sliding window to maintain a substring where we can replace at most k characters to make
# all characters the same. Keep track of the count of each character in the current window and the
# maximum frequency of any character in the window. If the size of the window minus the maximum
# frequency is greater than k, shrink the window from the left. Update the result with the


from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        res = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] += 1  # add current char to count
            maxf = max(maxf, count[s[r]])  # update max frequency char in current window

            if r - l + 1 - maxf > k:  # if current window size - max frequency char > k, shrink window from left
                count[s[l]] -= 1  # important to decrease count of char going out of window
                l += 1  # shrink window
            
            res = max(res, r - l + 1)  # update result with current window size - window size is r-l+1
        
        return res
        