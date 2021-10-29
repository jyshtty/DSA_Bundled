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
        j = 0
        n = len(A[0])
        longest_prefix = A[0]
        flag = 0
        while j < len(longest_prefix):
            try:
                for i in range(1, len(A)):
                    if A[i][j] != longest_prefix[j]:
                        flag = 1
                        break
                if flag == 1:
                    break
            except Exception as e:
                break
            j += 1
        return longest_prefix[:j]

A = [ "abcd", "abde", "abcf" ]

if __name__ == "__main__":
    obj = Solution()
    print(obj.longestCommonPrefix(A))



