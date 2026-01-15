# leetcode 560: Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# https://leetcode.com/problems/subarray-sum-equals-k/
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

# Approach: Prefix Sum + Hashmap
# We can use a hashmap to store the frequency of prefix sums.
# For each element in the array, we calculate the current prefix sum.
# We then check if there exists a prefix sum that when subtracted from the current prefix sum gives k.
# If such a prefix sum exists, we add its frequency to our count of subarrays.
# Finally, we update the frequency of the current prefix sum in the hashmap.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Implementation:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        l = len(nums)
        
        from collections import defaultdict

        freq = defaultdict(int)
        freq[0] = 1

        count = 0
        prefix = 0

        for i in nums: 
            prefix += i # current prefix sum

            if (prefix - k) in freq: # check if there is a prefix sum that when subtracted from current prefix gives k
                count += freq[prefix - k] # add the frequency of that prefix sum to count
            freq[prefix] += 1 # update the frequency of current prefix sum
        
        return count
