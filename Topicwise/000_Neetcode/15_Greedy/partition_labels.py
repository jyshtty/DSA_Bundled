"""
Problem: Partition Labels
Link: https://leetcode.com/problems/partition-labels/

Description:
    Partition string s into as many parts as possible so each letter
    appears in at most one part. Return the sizes of the parts.

Examples:
    Input:  s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]

    Input:  s = "eccbbbbdec"    Output: [10]

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}  # last occurrence of each character
        result = []
        start = end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])  # extend the current partition to cover this char's last occurrence
            if i == end:
                result.append(end - start + 1)
                start = end + 1

        return result
