# leetcode 31: Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# https://leetcode.com/problems/next-permutation/
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Approach: Find the first decreasing element from right, swap with next greater, reverse the rest
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


def next_permutation(a):
    s = str(a)
    r = 0
    while r < len(s)-1:
        if s[r] < s[r+1]:
            break_point = s[r+1]
            index1 = r+1
            c = 10
            break
        r = r + 1
    else:
        return ("It is the last number in permutation")
    r = len(s)-1
    while r > -1:
        if s[r] >= break_point:
            index2 = r
            break
        r = r -1

    ls = []
    ls[:0] = s

    ls[index1], ls[index2] = ls[index2], ls[index1]
    res = ''
    resultant = res.join(ls)
    return resultant

a = 321

print(next_permutation(a))



