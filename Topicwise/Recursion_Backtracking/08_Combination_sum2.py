# Make sure you check target == sum before you check index == len(candidates).


# # Combination Sum II - each number can be used only once
# # # Example: candidates = [10,1,2,7,6,1,5], target = 8
# # # Output: [[1,1,6], [1,2,5], [1,7], [2,6]]  

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
            # In combinationSum2, we must ensure we never reuse the same number again at the same level.
            # therefor we use while
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
    
            backtrack(index + 1, sum, temp)

        backtrack(0, 0, [])
        return ans
