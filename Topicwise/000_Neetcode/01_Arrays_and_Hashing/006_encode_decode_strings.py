"""
Problem: Encode and Decode Strings
Link: https://leetcode.com/problems/encode-and-decode-strings/

Description:
    Design an algorithm to encode a list of strings to a single string.
    The encoded string is then sent over the network and decoded back
    to the original list of strings. Implement encode and decode.

Examples:
    Input:  ["neet", "code", "love", "you"]
    Encode: "4#neet4#code4#love3#you"
    Decode: ["neet", "code", "love", "you"]

    Input:  ["we", "say", ":", "yes"]
    Encode: "2#we3#say1#:3#yes"
    Decode: ["we", "say", ":", "yes"]

Constraints:
    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains any possible characters including special characters.
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # prefix each word with "<length>#" so decode knows exactly how many
        # chars to read — handles strings that contain "#" or any special char
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#", i)          # find the delimiter after the length digits
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length           # jump past the word we just read
        return result
