# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
# where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
# of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:
# Input: candidates = [2], target = 1
# Output: []    

class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def backtrack(index, sum, temp):
            if index == len(candidates) or sum > target:
                return
            if sum == target:
                ans.append(temp.copy())
                return
            temp.append(candidates[index])
            backtrack(index, sum + candidates[index], temp) # not index + 1 coz we can reuse same element
            temp.pop()
            backtrack(index + 1, sum, temp) # move to next element - unpicking

        backtrack(0, 0, [])
        return ans
    
    
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        def aux(ans, cur, A, B):
            if sum(cur) > B:
                return
            elif sum(cur) == B:
                if cur not in ans:
                    ans.append(cur)
                return
            # try for all possible next candidate
            for i in A:
                aux(ans, sorted(cur + [i]), A, B)
            return

        A.sort()
        ans = []
        aux(ans, [], A, B)
        return ans
