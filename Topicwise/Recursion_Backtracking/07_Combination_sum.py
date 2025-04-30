# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
# where the chosen numbers sum to target. You may return the combinations in any order.



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
