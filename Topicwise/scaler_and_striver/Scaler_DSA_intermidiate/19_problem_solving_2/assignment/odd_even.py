### Count ways to make sum of odd and even indexed elements equal by removing an array element
"""
Problem Description

Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Problem Constraints
1<=n<=1e5
-1e5<=A[i]<=1e5


Input Format
First argument contains an array A of integers of size N


Output Format
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Example Input
Input 1:
A=[2, 1, 6, 4]
Input 2:

A=[1, 1, 1]


Example Output
Output 1:
1
Output 2:

3


Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1].
Therefore, the required output is 1.
Explanation 2:

 Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Therefore, the required output is 3.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def prefix_odd_even(self, A, n):
        prefix_even = [0] * (n+1) # plus 1 is hack to handle prefix_even[i-1]
        prefix_odd = [0] * (n+1) # plsu 1 is hack to handle prefix_odd[i-1]
        for i in range(n):
            if i % 2 == 0:
                prefix_even[i] = prefix_even[i - 1] + A[i]
                prefix_odd[i] = prefix_odd[i - 1]
            else:
                prefix_odd[i] = prefix_odd[i - 1] + A[i]
                prefix_even[i] = prefix_even[i - 1]
        return prefix_odd, prefix_even

    def solve(self, A):
        n = len(A)
        prefix_odd, prefix_even = self.prefix_odd_even(A,n)
        count = 0
        for i in range(n):
            even = prefix_even[i-1] + (prefix_odd[n-1] - prefix_odd[i])d
            odd = prefix_odd[i-1] + (prefix_even[n-1] - prefix_even[i])
            if even == odd:
                count += 1
        return count

if __name__ == '__main__':
    A = [1, 1, 1]
    obj = Solution()
    print(obj.solve(A))


