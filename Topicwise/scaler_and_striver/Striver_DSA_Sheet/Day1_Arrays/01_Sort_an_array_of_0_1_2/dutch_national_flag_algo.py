arr = [0,1,1,0,1,2,1,2,0,0,1]
def sort_all(arr):
  low = 0
  mid = 0
  high = len(arr) - 1
  while (high>=mid):
    if arr[low] == 0 and arr[mid] == 0:
      low += 1
      mid += 1
    elif arr[mid] == 0:
      arr[low], arr[mid] = arr[mid], arr[low]
      mid += 1
      low += 1
    elif arr[mid] == 2:
      arr[high], arr[mid] = arr[mid], arr[high]
      high -= 1
    else:
      mid += 1
  return arr

print(sort_all(arr))
