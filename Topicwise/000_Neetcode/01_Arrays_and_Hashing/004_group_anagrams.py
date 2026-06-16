"""
Problem: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/

Description:
    Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.

Examples:
    Input:  strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Input:  strs = [""]      Output: [[""]]
    Input:  strs = ["a"]     Output: [["a"]]

Constraints:
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            # sorted chars form a canonical key shared by all anagrams of a word
            key = tuple(sorted(word))
            groups[key].append(word)

        return list(groups.values())
