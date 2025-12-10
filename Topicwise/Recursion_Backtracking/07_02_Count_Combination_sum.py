# Combination Sum - count all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
# # # Leetcode Link: https://leetcode.com/problems/combination-sum-ii/

# # # Example: candidates = [1,2,3,4,5,6], target = 5
# # # Output: [[5], [1,4], [2,3], [1,2,2], [1,1,3], [1,1,1,2], [1,1,1,1,1]]     

class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        def backtrack(index, sum, temp):
            if index == len(candidates) or sum > target:
                return 0
            if sum == target:
                ans.append(list(temp))
                return 1
            temp.append(candidates[index])
            l =  backtrack(index + 1, sum + candidates[index], temp)
            temp.pop()
            r = backtrack(index + 1, sum, temp)
            return l + r
        return backtrack(0, 0, [])

obj = Solution()
print(obj.combinationSum([1,2,3,4,5,6], 5))