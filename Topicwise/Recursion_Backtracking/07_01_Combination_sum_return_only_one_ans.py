# Combination Sum - return only one answer
# # # Example: candidates = [1,2,3,4,5,6], target = 5
# # # Output: [[2,3]]   <--- only one combination is needed as output
# # # Explanation: The combination [2,3] is the only one that adds up to 5.

class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def backtrack(index, sum, temp):
            if index == len(candidates) or sum > target:
                return False
            if sum == target:
                ans.append(list(temp))
                return True
            temp.append(candidates[index])
            if backtrack(index + 1, sum + candidates[index], temp):
                return True
            temp.pop()
            if backtrack(index + 1, sum, temp):
                return True

        if backtrack(0, 0, []):
            return ans

obj = Solution()
print(obj.combinationSum([1,2,3,4,5,6], 5))