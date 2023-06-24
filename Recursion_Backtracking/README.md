# BACKTRACKING

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

```python
 def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
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

