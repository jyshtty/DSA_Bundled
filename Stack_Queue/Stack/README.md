
1.  NEAREST SMALLEST LEFT

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


