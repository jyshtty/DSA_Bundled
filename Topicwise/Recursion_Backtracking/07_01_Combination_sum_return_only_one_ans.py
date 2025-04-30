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