"""
Problem: Alien Dictionary
Link: https://leetcode.com/problems/alien-dictionary/

Description:
    Given a sorted list of words in an alien language, derive the order of
    letters. Return any valid ordering, or "" if the order is invalid.

Examples:
    Input:  words = ["wrt","wrf","er","ett","rftt"]    Output: "wertf"
    Input:  words = ["z","x"]                          Output: "zx"
    Input:  words = ["z","x","z"]                      Output: ""  (cycle)

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # build adjacency list and in-degree count
        adj = defaultdict(set)
        in_degree = {ch: 0 for word in words for ch in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""  # w1 is a prefix of w2 but appears after — invalid
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        # topological sort (Kahn's BFS)
        queue = deque([ch for ch in in_degree if in_degree[ch] == 0])
        result = []
        while queue:
            ch = queue.popleft()
            result.append(ch)
            for nei in adj[ch]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return "".join(result) if len(result) == len(in_degree) else ""
