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

   


