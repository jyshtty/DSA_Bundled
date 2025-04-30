"""
Problem Description

Find the contiguous subarray within an array, A of length N which has the largest sum.



Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000



Input Format
The first and the only argument contains an integer array, A.



Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.



Example Input
Input 1:

 A = [1, 2, 3, 4, -10]
Input 2:

 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


Example Output
Output 1:

 10
Output 2:

 6


Example Explanation
Explanation 1:

 The subarray [1, 2, 3, 4] has the maximum possible sum of 10.
Explanation 2:

 The subarray [4,-1,2,1] has the maximum possible sum of 6.
"""

"""
APPROACH 1
1. Find prefix sum
2. Iterate over prefix sum to find sum of element from ith element to   
"""
class Solution():
    def solve(self, A):
        sum = A[0]
        prefix_sum = [sum]
        for i in range(1,len(A)):
            sum = sum + A[i]
            prefix_sum.append(sum)
        maxi = max(prefix_sum)
        for i in range(len(prefix_sum)):





if __name__ == "__main__":
    A = [1,2,3,4,5]
    obj = Solution()
    print(obj.solve(A))

