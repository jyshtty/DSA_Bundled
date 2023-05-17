"""
Noble Integer
Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p If such an integer is found return 1 else return -1
"""

def noble_element(arr):

    for i in range(len(arr)):
        if i+1 < len(arr):
            if arr[i] == arr[i+1]:
                continue
        if arr[i] == len(arr)-1-i:
            return 1
        else:
            continue
    return -1

arr = [1,1,2,2,3,3]

print(noble_element(arr))
