"""
Problem Description

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographicaly in this alien language else return 0.



Problem Constraints
1 <= N, length of each word <= 105

Sum of length of all words <= 2 * 106



Input Format
First argument is a string array A of size N.

Second argument is a string B of size 26 denoting the order.



Output Format
Return 1 if and only if the given words are sorted lexicographicaly in this alien language else return 0.



Example Input
Input 1:

 A = ["hello", "scaler", "interviewbit"]
 B = "adhbcfegskjlponmirqtxwuvzy"
Input 2:

 A = ["fine", "none", "no"]
 B = "qwertyuiopasdfghjklzxcvbnm"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 The order shown in string B is: h < s < i for the given words. So return 1.
Explanation 2:

 "none" should be present after "no". Return 0.


"""

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        alphabets = {}
        count = 0
        for char in B:
            alphabets[char] = count
            count += 1
        for i in range(len(A) - 1):
            if self.compare(A[i], A[i + 1], alphabets) > 0:
                return 0
        return 1

    def compare(self, word_1, word_2, alphabets):
        i = 0
        j = 0
        char_compare_value = 0

        while i < len(word_1) and j < len(word_2) and char_compare_value == 0:
            char_compare_value = alphabets.get(word_1[i]) - alphabets.get(word_2[j])
            i += 1
            j += 1

        if char_compare_value == 0:
            return len(word_1) - len(word_2)
        else:
            return char_compare_value


if __name__ == "__main__":
    A = ["hello", "scaler", "interviewbit"]
    B = "adhbcfegskjlponmirqtxwuvzy"
    obj = Solution()
    print(obj.solve(A, B))