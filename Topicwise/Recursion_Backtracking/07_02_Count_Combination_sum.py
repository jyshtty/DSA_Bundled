# Combination Sum - return all possible combinations
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