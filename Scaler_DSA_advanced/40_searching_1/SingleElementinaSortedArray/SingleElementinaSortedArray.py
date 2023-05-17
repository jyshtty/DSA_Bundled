"""
Problem Description

Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return the single element that appears only once.



Example Input
Input 1:

A = [1, 1, 7]
Input 2:

A = [2, 3, 3]


Example Output
Output 1:

 7
Output 2:

 2


Example Explanation
Explanation 1:

 7 appears once
Explanation 2:

 2 appears once
"""

class Solution:
    def solve(self, A):
        n = len(A)
        if A[n-1] != A[n-2]:
            return A[n-1]
        if A[0] !=  A[1]:
            return A[0]
        low = 0
        high = len(A)-1

        while(low <= high):
            mid = low + (high - low)/2
            if A[mid] != A[mid-1] and A[mid] != A[mid+1]:
                return A[mid]
                if A[mid] == A[mid-1]:
                mid = mid -1 # first occurance
            if mid & 1 == 0:
                low = mid + 2
            else:
                high = mid -1
        return -1

obj = Solution()
A = [1, 1, 7]
print(obj.solve(A))


