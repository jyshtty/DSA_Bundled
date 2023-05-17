# Question = Number of times it is right shifted.


# find index of minimum element ---------- find pivot - which is lowest number in list

# next = (mid+1) % N    to avoid index going byond length of array
# prev = (N + mid-1) % N       to avoid index going less than araay 0.

# if arr[mid] < arr[next]  and arr[mid] < arr[prev] return mid  ----- property of smallest number is both the number on it left and right side are larger than itself

# if arr[mid] > arr[0], low = mid + 1          coz always take the unsorted and discard the sorted part
# else: hogh = mid - 1