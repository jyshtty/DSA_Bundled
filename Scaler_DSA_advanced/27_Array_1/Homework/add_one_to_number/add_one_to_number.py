"""
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, following are some good questions to ask :

Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if A == [0]: return [1]
        if sum(A) == len(A) * 9:
            return [1] + [0] * len(A)
        if A[-1] < 9:
            A[-1] = A[-1] + 1
        else:
            for i in range(len(A) - 1, -1, -1):
                if A[i] >= 9:
                    A[i] = 0
                else:
                    A[i] = A[i] + 1
                    break
        i = 0
        while A[i] == 0:
            i += 1
        return A[i:]
