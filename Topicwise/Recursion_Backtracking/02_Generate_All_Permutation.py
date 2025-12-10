# generate all permutation of [1,2,3]
# # Example: arr = [1,2,3]
# # Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]


def solve(arr):
    curr = [-1] * len(arr)
    ans = []
    def generate(index):
        if index == len(curr):
            ans.append(curr.copy())
        for i in range(len(arr)):
            flag = 0
            for j in range(index): # check if arr[i] is already used
                if curr[j] == arr[i]: # already used
                    flag = 1 
                    break
            if flag == 0: # not used
                curr[index] = arr[i] # place arr[i] at index
                generate(index+1) # recurse for next index
                # no need to unmark, as we are overwriting in next iteration
    generate(0)
    return ans
