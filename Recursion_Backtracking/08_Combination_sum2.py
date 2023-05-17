# Make sure you check target == sum before you check index == len(candidates)

class Solution:
    def combinationSum2(self, candidates, target):
        ans = []
        candidates.sort()

        def backtrack(index, sum, temp):
            if sum == target:
                ans.append(temp.copy())
                return

            if index == len(candidates) or sum > target:
                return

            temp.append(candidates[index])
            backtrack(index + 1, sum + candidates[index], temp)
            temp.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, sum, temp)

        backtrack(0, 0, [])
        return ans