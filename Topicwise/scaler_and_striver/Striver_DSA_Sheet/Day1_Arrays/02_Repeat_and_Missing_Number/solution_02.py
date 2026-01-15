# Repeat and Missing Number
# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.
# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# Example:
# Input: [3,1,2,5,3]
# Output: [3,4]
# Approach: Using XOR
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


def foo(A):
    n = len(A)
    prefix_even = [0] * n
    prefix_odd = [0] * n
    for i in range(n):
        if i % 2 == 0:
            prefix_even[i] = prefix_even[i-1] + A[i]
            prefix_odd[i] = prefix_odd[i-1]
        else:
            prefix_odd[i] = prefix_odd[i-1] + A[i]
            prefix_even[i] = prefix_even[i-1]
    return prefix_even, prefix_odd

A = [4,3,6,2,1]
print(foo(A))