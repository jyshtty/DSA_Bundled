# BACKTRACKING

## Trick
1. For most of the probelm will have index as parameter, decide what to pass as index. For N queen, Row number is index.
2. Usually base case will have index == something. As we are incrementing index for every funtion call.
3. A data_structure is carried along function call as another parameter. We append a value to be before the backtracking call and pop the value after backtracking call. This data structure is usually printed once base case is met.
       1. In case of permutation, this data structure is curr = [-1] * len(s)
       2. In case of subsets, this data structure is curr = []
4. After 1-3 is taken care, decide upon the number of parameter that you need to pass to function.
5. Decide how many function calls

## Print Decreasing Number from 5 to 1
>Expectation
>Input - print_decreasing(5)
Output -
5
4
3
2
1
>Faith - Let us assume print_decreasing(4) works fine.
>
```python

def print_decresing(n):
     if n == 0:
         return
      
     print(n)
     return print(n-1)
```

## Print Increasing Number from 1 to 5
>Expectation
>Input - print_increasing(5)
>Output -
>1
>2
>3
>4
>5
>Faith - Let us assume print_increasing(4) works fine.
>
```python

def print_increasing(n):
     if n == 0:
         return
      
     return print(n-1)
     print(n)
```

```python
def A():
     line1
     B()
     line2

def B():
     line3
     C()
     line4

def C():
     line5
```


>when function A is called, Output is 
line1
line3
line5
line4
line2

# Two ways how recursion is called.
1. PARAMETERISED
```python
def sum_(n, sum):
    if n < 1:
        return sum
    return sum_(n-1, sum+n)

print(sum_(5,0))
```

2. FUNCTIONAL
```python
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

print(sum(5))
```

## Simple Fibonacci 
### Multiple recussion calls example

```python
 def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

n = 6
dp = [0] * (n+1)
def fibo(n):
    if n <= 1:
        return n
    if dp[n]:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]
  ```

## check palindrome 

```python
 def palin(i):
        if i >= n//2:
            return True
        if s[i] != s[n-i-1]: # instead of using 2 pointer this is an optimization. that is by using only one variable
             return False
        return palin(i+1)

i = 0
n = len(s)
s = "MADAM"
  ```

## reverse String

```python
 def reverse(i):
        if i >= n//2:
            return 
        s[i], s[n-i-1] = s[n-i-1], s[i] 
        reverse(i+1)
  ```


>Note - If you don't want to pop changed variable after backtracking call is returned simple change the variable in func call itself.
for Ex -
See generate parenthesis code.
```python
class Solution:
    def generateParenthesis(self, n):
        stack = []
        left = right = n
        result = []
        self.generate(stack, left, right, result)
        return result

    def generate(self, stack, left, right, result):
        if left == 0 and right == 0:
            result.append("".join(stack))
            return
        if left != 0:
            stack.append("(")
            self.generate(stack, left - 1, right, result)
            stack.pop()
        if right < left:
            stack.append(")")
            self.generate(stack, left, right - 1, result)
            stack.pop()
```

1. stack.append(")")
backtracking(open, closed+1) # last time when execution of this line is done, stack will look like [( ( ( ) ) )], and when last time execution of this line is done it prints.  This line was called by bactracking (3, 2)
stack.pop()

2. self.generate(stack + ["("], left - 1, right, result)

It works because when you get back the control to the calling function, the stack value is still the same.
You are changing it only for the called function i.e in its parameter.


# 3 Pattern of Backtracking Problem - Very Important while solving DP problems.
Taking example of combination sum problem.

1. Find all subsets whose sum is equal to the given target.
```python
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
```

> backtrack(target, data_structure, sum)
> 
>      if condition satisfies >> print data_structure
>
>      pick  >> backtrack = add elem to data_structure
>  
>      unpick  >> backtrack do not elem to data_structure


2. Return only one subset whose sum is equal to given target or return true.

```python
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
```
### Rand and the maze - return when one solution is found
```python
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        mat = [[0 for i in range(n)] for j in range(n)]


        def backtrack(mat, i, j):
            if i == n - 1 and j == n - 1:
                mat[n - 1][n - 1] = 1
                return True
            
            if A[i][j] == 1:
                mat[i][j] = 1
                if i + 1 < n:
                    if backtrack(mat, i + 1, j):
                        return True

                if j + 1 < n:
                    if  backtrack(mat, i, j + 1):
                        return True
                mat[i][j] = 0

            else:
                return False
        if backtrack(mat, 0, 0):
               return mat
```
> backtrack(target, data_structure, sum)
> 
>      if condition satisfies >> return true
>
>      if  backtrack = (pick  >> add elem to data_structure) == true return true
>  
>      if true - backtrack = (unpick do not elem to data_structure == true return true

3. Count the number of subset whose sum is equal to target

```python
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
```

> backtrack(target, data_structure, sum)
> 
>      if condition satisfies >> return 1 else 0
>
>      r = backtrack = (pick  >> add elem to data_structure) 
>  
>      l = unpick  >> backtrack = do not elem to data_structure
> 
>      return l + r
> 
>      N Queen Pattern
>
>      s = 0
> 
>      for i in arr:
> 
>      s+= 1
>
>      return s


