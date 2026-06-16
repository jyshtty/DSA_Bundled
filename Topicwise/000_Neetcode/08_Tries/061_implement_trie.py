"""
Problem: Implement Trie (Prefix Tree)
Link: https://leetcode.com/problems/implement-trie-prefix-tree/

Description:
    Implement a trie with insert, search, and startsWith methods.

Examples:
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")      -> True
    trie.search("app")        -> False
    trie.startsWith("app")    -> True
    trie.insert("app")
    trie.search("app")        -> True

Constraints:
    1 <= word.length, prefix.length <= 2000
    word and prefix consist of lowercase English letters.
    At most 3 * 10^4 calls to insert, search, startsWith.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False  # marks whether a complete word ends here


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end  # must reach a complete-word marker, not just a prefix

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
