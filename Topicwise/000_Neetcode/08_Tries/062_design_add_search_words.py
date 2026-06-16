"""
Problem: Design Add and Search Words Data Structure
Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

Description:
    Design a data structure that supports addWord and search.
    search(word) returns true if any string in the data structure matches word,
    where '.' can match any letter.

Examples:
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.search("pad")   -> False
    obj.search("bad")   -> True
    obj.search(".ad")   -> True
    obj.search("b..")   -> True

Constraints:
    1 <= word.length <= 25
    word consists of lowercase English letters or '.'.
    At most 10^4 calls to addWord and search.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == '.':
                # '.' matches any character — try all children
                return any(dfs(child, i + 1) for child in node.children.values())
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)
