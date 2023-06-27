# Use DP Solution

# Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details. 
# This is a famous Google interview question, also being asked by many other companies now a days.

# Consider the following dictionary 
# { i, like, sam, sung, samsung, mobile, ice, 
#   cream, icecream, man, go, mango}

# Input:  ilike
# Output: Yes 
# The string can be segmented as "i like".

# Input:  ilikesamsung
# Output: Yes
# The string can be segmented as "i like samsung" 
# or "i like sam sung".



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
