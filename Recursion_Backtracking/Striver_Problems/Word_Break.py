# Use DP Solution

class Solution:
    def wordBreak(self, s, wordDict):
        def wordBreakRecur(s: str, word_dict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True
            return False

        return wordBreakRecur(s, set(wordDict), 0)