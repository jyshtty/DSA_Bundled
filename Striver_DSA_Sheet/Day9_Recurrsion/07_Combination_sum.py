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
            backtrack(index, sum + candidates[index], temp)
            temp.pop()
            backtrack(index + 1, sum, temp)

        backtrack(0, 0, [])
        return ans