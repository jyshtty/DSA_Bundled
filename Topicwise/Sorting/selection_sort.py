# Selection Sort
# Sort an array in ascending order using selection sort.
# Approach: For each position, find the minimum in the remaining array and swap.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Implementation:

arr = [5,4,3,2,1]
def selection_sort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1,len(arr)):
            if arr[mini] > arr[j]:
                mini = j
        if mini != i:
            arr[i], arr[mini] = arr[mini], arr[i]
    return arr

print(selection_sort(arr))
