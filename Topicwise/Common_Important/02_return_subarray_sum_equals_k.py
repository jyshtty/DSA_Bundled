# Return the first subarray found with sum equal to k
# Given an array A of integers and an integer B, find and return the first continuous subarray which adds to B.
# If the answer does not exist return an array with a single element -1.
# https://www.interviewbit.com/problems/return-subarray-sum-equals-k/
# Example 1:
# Input: A = [1, 2, 3, 4, 5], B = 5
# Output: [2, 3]
# Explanation: The first subarray found with sum 5 is [2, 3].
# Example 2:
# Input: A = [5, 10, 20, 100, 105], B = 110
# Output: -1    

# Approach: Prefix Sum + Hashmap
# We can use a hashmap to store the prefix sums and their corresponding indices.
# For each element in the array, we calculate the current prefix sum.
# We then check if there exists a prefix sum that when subtracted from the current prefix sum gives B.
# If such a prefix sum exists, we return the subarray from the index after that prefix sum to the current index.
# If no such subarray is found, we return [-1]. 
# Time Complexity: O(n)
# Space Complexity: O(n)

# Implementation: 


class Solution:
    def solve(self, A, B):
        prefix_map = {0: -1}
        curr_sum = 0

        for i in range(len(A)):
            curr_sum += A[i]

            if curr_sum - B in prefix_map:
                return A[prefix_map[curr_sum - B] + 1 : i + 1]

            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i

        return [-1]

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = 5
    obj = Solution()
    print(obj.solve(A, B))