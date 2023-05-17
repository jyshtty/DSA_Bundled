"""
Problem Description

Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".



Problem Constraints
0 <= sum of length of all strings <= 1000000



Input Format
The only argument given is an array of strings A.



Output Format
Return the longest common prefix of all strings in A.



Example Input
Input 1:

A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:

A = ["abab", "ab", "abcd"];


Example Output
Output 1:

"a"
Output 2:

"ab"


Example Explanation
Explanation 1:

Longest common prefix of all the strings is "a".
Explanation 2:

Longest common prefix of all the strings is "ab".
"""

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        common_prefix = ''
        max_len = float('inf')

        if len(A) == 1:
            return A[0]

        for i in range(len(A)):
            max_len = min(max_len, len(A[i]))

        for i in range(max_len):
            for j in range(len(A)-1):
                if A[j][i] != A[j+1][i]:
                    return common_prefix
            common_prefix = common_prefix + A[j][i]
        return common_prefix

if __name__ == "__main__":
    A = [ "ABCD" ]
    obj = Solution()
    print(obj.longestCommonPrefix(A))


