"""
Problem: Word Ladder
Link: https://leetcode.com/problems/word-ladder/

Description:
    Given beginWord, endWord, and a wordList, return the length of the
    shortest transformation sequence where each adjacent pair differs by
    one letter. Return 0 if no sequence exists.

Examples:
    Input:  beginWord = "hit", endWord = "cog",
            wordList = ["hot","dot","dog","lot","log","cog"]    Output: 5
    Input:  same setup but wordList = ["hot","dot","dog","lot","log"]    Output: 0

Constraints:
    1 <= beginWord.length <= 10
    beginWord, endWord, and words in wordList consist of lowercase English letters.
    1 <= wordList.length <= 5000
"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # precompute pattern -> [words] to avoid O(n*26) per-word scan
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                for neighbor in pattern_map[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))

        return 0
