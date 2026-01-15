# Bubble Sort
# Sort an array in ascending order using bubble sort.
# Approach: Repeatedly swap adjacent elements if they are in wrong order.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Implementation:

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, (len(arr)-1-i)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr

print(bubble_sort([5,4,3,2,1]))
