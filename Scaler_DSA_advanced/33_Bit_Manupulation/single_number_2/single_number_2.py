"""
Single Number II
Problem Description

Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

NOTE: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?




Problem Constraints
2 <= A <= 5*106

0 <= A <= INTMAX



Input Format
First and only argument of input contains an integer array A.



Output Format
Return a single integer.



Example Input
Input 1:

 A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Input 2:

 A = [0, 0, 0, 1]


Example Output
Output 1:

 4
Output 2:

 1


Example Explanation
Explanation 1:

 4 occurs exactly once in Input 1.
 1 occurs exactly once in Input 2.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        count = 0
        ans = 0
        for i in range(32):
            count = 0
            for j in range(len(A)):
                x = A[j] >> i
                if (x & 1):
                    count += 1
            # print(count)
            if count % 3 == 1:
                ans = ans + (1 << i)
        return ans

if __name__ == "__main__":
    A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
    obj = Solution()
    print(obj.singleNumber(A))