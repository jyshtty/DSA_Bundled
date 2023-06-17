# same as binary search with follwoing changes.False

# 1. check arr[mid-1], ,arr[mid], arr[mid+1] ,     if you find elem return
# 2 remaining condition are same but
# high = mid - 2
# low = mid + 2


#  handle out of bound error ---- when mid is 0, mid - 1 is not possible.

if arr[mid] == target:
    return mid

if mid > low and arr[mid - 1] == target:
    return mid-1

if mid < high and arr[mid + 1] == target:
    return mid + 1