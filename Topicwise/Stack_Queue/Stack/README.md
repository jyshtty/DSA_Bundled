1. NEAREST SMALLEST LEFT

``` python

def nearest_smallest_left(arr):
    stack = []
    result = []

    for num in arr:
        while stack and stack[-1] >= num:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(num)

    return result
```

``` python

array = [4, 5, 2, 10, 8]
result = nearest_smallest_left(array)
print(result)

```

``` python
[-1, 4, -1, 2, 2]
```

2. NEAREST SMALLEST RIGHT

``` python
def nearest_smallest_right(arr):
    stack = []
    result = []
    
    # Iterate through the array in reverse order
    for i in range(len(arr)-1, -1, -1):
        num = arr[i]
        
        while stack and stack[-1] >= num:
            stack.pop()
        
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        
        stack.append(num)
    
    # Reverse the result to obtain the correct order
    result.reverse()
    
    return result

```

``` python
array = [4, 5, 2, 10, 8]
result = nearest_smallest_right(array)
print(result)
```

``` python
[2, 2, -1, 8, -1]
```

3. Next Greater number on right



``` python
# PROBLEM:
# For each element in the array, find the next greater element to its right.
# If no greater element exists to the right, use -1.

# monotonous decreasing stack is used -
# maintain decreasing order in the stack i.e top of stack has the next greater element i.e higher number on top of smaller numbers.

# APPROACH (using a stack, O(n) time):
# - Iterate the array from right to left.
# - Maintain a stack of candidate next-greater elements (strictly greater values).
# - For current element x, pop from the stack while stack[-1] <= x.
# - If stack is empty after popping, the next greater is -1; otherwise it's stack[-1].
# - Push x onto the stack and continue.

def next_greater_right(arr):
    stack = []          # will store candidates (values)
    result = [0] * len(arr)

    # iterate from right to left
    for i in range(len(arr)-1, -1, -1):
        x = arr[i]
        # remove elements that are <= current element
        while stack and stack[-1] <= x:
            stack.pop()

        # top of stack is the next greater element if exists
        result[i] = stack[-1] if stack else -1

        # push current element as a candidate for elements to its left
        stack.append(x)

    return result

# Example:
array = [4, 5, 2, 10, 8]
print(next_greater_right(array))  # output: [5, 10, 10, -1, -1]
```

**Complexity:** Time: O(n), Space: O(n)

4. Next Greater number on left

``` python
# PROBLEM:
# For each element in the array, find the next greater element to its left.
# If no greater element exists to the left, use -1.

# APPROACH (using a stack, O(n) time):
# - Iterate the array from left to right.
# - Maintain a stack of candidate greater elements (strictly greater values).
# - For current element x, pop from the stack while stack[-1] <= x.
# - If stack is empty after popping, the next greater to left is -1; otherwise it's stack[-1].
# - Push x onto the stack and continue.

def next_greater_left(arr):
    stack = []
    result = [0] * len(arr)

    # iterate from left to right
    for i in range(len(arr)):
        x = arr[i]
        # remove elements that are <= current element
        while stack and stack[-1] <= x:
            stack.pop()

        # top of stack is the next greater element to the left if exists
        result[i] = stack[-1] if stack else -1

        # push current element as a candidate for elements to its right
        stack.append(x)

    return result

# Example:
array = [4, 5, 2, 10, 8]
print(next_greater_left(array))  # output: [-1, -1, 5, -1, 10]
```

**Complexity:** Time: O(n), Space: O(n)

