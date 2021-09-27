"""
Find a peak element
Problem Description

Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.

For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return the peak element.



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
Input 2:

A = [5, 17, 100, 11]


Example Output
Output 1:

 5
Output 2:

 100


Example Explanation
Explanation 1:

 5 is the peak.
Explanation 2:

 100 is the peak.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.append(-float('inf'))
        l = 0
        h = len(A)-1
        while l <= h:
            mid = l + (h-l)/2
            if mid != 0:
                if A[mid] > A[mid -1] and A[mid] > A[mid + 1]:
                    return A[mid]
                elif A[mid] > A[mid - 1]:
                    l = mid + 1
                elif A[mid] < A[mid - 1]:
                    h = mid - 1
            else:
                if A[0] > A[1]:
                    return A[0]
                break
        return 'Not Found'

obj = Solution()
A = [5, 4, 3, 2, 1]
print(obj.solve(A))