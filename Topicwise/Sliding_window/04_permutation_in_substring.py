# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26

        # initialize counts
        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1

        # sliding window
        for i in range(len(s2) - len(s1)):
            if counts1 == counts2:
                return True
            # slide the window: remove left char, add right char
            counts2[ord(s2[i]) - ord('a')] -= 1
            counts2[ord(s2[i + len(s1)]) - ord('a')] += 1

        return counts1 == counts2
