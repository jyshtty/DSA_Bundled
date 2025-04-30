"""
Problem Description

You are given two strings A and B of size N and M respectively.

You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.



Problem Constraints
1 <= N < M <= 105



Input Format
Given two argument, A and B of type String.



Output Format
Return a single Integer, i.e number of permutations of A present in B as a substring.



Example Input
Input 1:

 A = "abc"
 B = "abcbacabc"
Input 2:

 A = "aca"
 B = "acaa"


Example Output
Output 1:

 5
Output 2:

 2


Example Explanation
Explanation 1:

 Permutations of A that are present in B as substring are:
    1. abc
    2. cba
    3. bac
    4. cab
    5. abc
    So ans is 5.
Explanation 2:

 Permutations of A that are present in B as substring are:
    1. aca
    2. caa
"""

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        if len(A) > len(B):
            return 0
        s1 = [0] * 26
        s2 = [0] * 26
        for i in range(len(A)):
            s1[ord(A[i]) - ord('a')] += 1
            s2[ord(B[i]) - ord('a')] += 1

        i = len(A) - 1
        j = 0
        count = 0

        while i < len(B):
            if s1 == s2:
                count += 1
            i += 1
            if i != len(B):
                s2[ord(B[i]) - ord("a")] += 1
            s2[ord(B[j]) - ord("a")] -= 1
            j += 1
        return count

if __name__ == "__main__":
    A = "abc"
    B = "abcbacabc"
    obj = Solution()
    print(obj.solve(A,B))

