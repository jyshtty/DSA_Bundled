# leetcode 88: Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums2 into nums1 as one sorted array.
# https://leetcode.com/problems/merge-sorted-array/
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Approach: Three pointers from end
# Time Complexity: O(m+n)
# Space Complexity: O(1)
# Implementation:


A = [1, 3, 3, 4, 7]
B = [4, 5]

def foo1(A, B):
    for i in range(len(A)):
        j = 0
        while (j < len(B)):
            if A[i] <= B[j]:
                j += 1
                continue
            else:
                A[i], B[j] = B[j], A[i]
                B.sort()
    return A + B

def foo2(A, B):
    j = 0
    i = 0
    while i < len(A):
        if A[i] > B[j]:
            temp = B[j]
            B[j] = A[i]
            A[i] = temp
            B.sort()
        i += 1
    return A + B

print(foo1(A, B))
