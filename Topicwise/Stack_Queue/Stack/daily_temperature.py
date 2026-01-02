# monotonic decreasing stack approach - next greater element to the right
# Time: O(n)
# Space: O(n)



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            
            while stack and temperatures[stack[-1]] <= temperatures[i]: # maintain decreasing order in the stack i.e top of stack has the next greater element i.e higher number on top of smaller numbers.
                stack.pop()
            
            if stack:
                ans[i] = stack[-1] - i # index difference between current and next greater element gives number of days.
            
            stack.append(i)
        
        return ans
        
        