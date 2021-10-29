"""
Rotated Sorted Array Search
Problem Description

Given a sorted array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints
1 <= N <= 1000000

1 <= A[i] <= 10^9

all elements in A are disitinct.



Input Format
The first argument given is the integer array A.

The second argument given is the integer B.



Output Format
Return index of B in array A, otherwise return -1



Example Input
Input 1:

A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4
Input 2:

A = [1]
B = 1


Example Output
Output 1:

 0
Output 2:

 0


Example Explanation
Explanation 1:


Target 4 is found at index 0 in A.
Explanation 2:


Target 1 is found at index 0 in A.


"""
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def binary_search(self, A, x):
        low = 0
        high = len(A)-1
        while low <= high:
            mid = low + (high-low)/2
            if A[mid] == x:
                return mid
            elif A[mid] > x:
                high = mid-1
            else:
                low = mid + 1
        return -1

    def find_index(self ,A ,low ,high):
        while low <= high:
            mid = low + (high-low)/2
            if A[mid] < A[mid-1]:
                return mid
            elif A[mid] > A[0]:
                low = low + 1
            else:
                high = high -1
        return

    def search(self, A, B):
        if len(A) ==  1:
            if A[0] == B:
                return 0
            else:
                return -1

        low = 0
        high = len(A) - 1
        index = self.find_index(A, low, high)
        res = self.binary_search(A[:index], B)
        if res != -1:
            return res
        res = self.binary_search(A[index:], B)
        if res != -1:
            return res + index
        return res

obj = Solution()
print(obj.search([ 180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64, 67, 69, 72, 73, 75, 77, 78, 79, 83, 85, 87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149, 152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177 ], 42))







