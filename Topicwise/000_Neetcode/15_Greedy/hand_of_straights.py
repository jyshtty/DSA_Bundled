"""
Problem: Hand of Straights
Link: https://leetcode.com/problems/hand-of-straights/

Description:
    Given an integer array hand of card values and an integer groupSize,
    return true if cards can be rearranged into groups of consecutive cards
    each of size groupSize.

Examples:
    Input:  hand = [1,2,3,6,2,3,4,7,8], groupSize = 3   Output: True
    Input:  hand = [1,2,3,4,5], groupSize = 4            Output: False

Constraints:
    1 <= hand.length <= 10^4
    0 <= hand[i] <= 10^9
    1 <= groupSize <= hand.length
"""

from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            # if this card still has remaining copies, it must start a new group
            if count[card] > 0:
                times = count[card]
                for i in range(groupSize):
                    count[card + i] -= times
                    if count[card + i] < 0:
                        return False

        return True
