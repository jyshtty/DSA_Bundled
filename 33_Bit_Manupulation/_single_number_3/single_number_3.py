"""
Single Number III
Problem Description

Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Note: Output array must be sorted.



Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109



Input Format
First argument is an array of interger of size N.



Output Format
Return an array of two integers that appear only once.



Example Input
Input 1:

A = [1, 2, 3, 1, 2, 4]
Input 2:

A = [1, 2]


Example Output
Output 1:

[3, 4]
Output 2:

[1, 2]


Example Explanation
Explanation 1:

 3 and 4 appear only once.
Explanation 2:

 1 and 2 appear only once.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers

    def find_single_element(self, A):
        xor = 0
        for i in A:
            xor = xor ^ i
        return xor


    def solve(self, A):
        set_bit_index = []
        set_bit_not_index = []
        index = 0
        xor = 0
        for i in A:
            xor = xor ^ i
        for i in range(32):
            x = xor >> i
            k = x & 1
            if k == 1:
                index = i
                break
        for i in range(len(A)):
            x = A[i] >> index
            if x & 1:
                set_bit_index.append(A[i])
            else:
                set_bit_not_index.append(A[i])
        x = self.find_single_element(set_bit_index)
        y = self.find_single_element(set_bit_not_index)
        return x,y

if __name__ == "__main__":
    A = [ 186, 256, 102, 377, 186, 377 ]
    obj = Solution()
    print(obj.solve(A))
