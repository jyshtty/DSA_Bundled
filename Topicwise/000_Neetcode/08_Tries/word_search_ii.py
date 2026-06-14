"""
Problem: Word Search II
Link: https://leetcode.com/problems/word-search-ii/

Description:
    Given an m x n board of characters and a list of words, return all
    words that can be found in the board. Words can be formed by sequentially
    adjacent cells (horizontally or vertically). No cell may be reused.

Examples:
    Input:  board = [["o","a","a","n"],["e","t","a","e"],
                     ["i","h","k","r"],["i","f","l","v"]],
            words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

Constraints:
    1 <= board.length, board[i].length <= 12
    1 <= words.length <= 3 * 10^4
    1 <= words[i].length <= 10
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores the full word at the end node to avoid reconstructing it


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            next_node = node.children[ch]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # prevent duplicate results

            board[r][c] = '#'  # mark visited in-place to avoid a separate visited set
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
            board[r][c] = ch  # restore

            # prune exhausted trie nodes to speed up future searches
            if not next_node.children:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
