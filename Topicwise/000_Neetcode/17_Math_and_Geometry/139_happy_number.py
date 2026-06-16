"""
Problem: Happy Number
Link: https://leetcode.com/problems/happy-number/

Description:
    A happy number reaches 1 when repeatedly replacing it with the sum of
    squares of its digits. Return true if n is happy, false if it loops forever.

Examples:
    Input:  n = 19    Output: True  (1² + 9² = 82 → 68 → 100 → 1)
    Input:  n = 2     Output: False

Constraints:
    1 <= n <= 2^31 - 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x):
            return sum(int(d) ** 2 for d in str(x))

        slow, fast = n, next_num(n)
        # Floyd's cycle detection: if n is unhappy, the sequence enters a cycle
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

        return fast == 1
