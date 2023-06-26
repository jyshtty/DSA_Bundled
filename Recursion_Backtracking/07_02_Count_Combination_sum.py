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