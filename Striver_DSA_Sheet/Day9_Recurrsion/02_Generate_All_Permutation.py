# generate all permutation of [1,2,3]

def solve(arr):
    curr = [-1] * len(arr)
    ans = []
    def generate(index):
        if index == len(curr):
            ans.append(curr)
        for i in range(len(arr)):
            flag = 0
            for j in range(index):
                if curr[j] == arr[i]:
                    flag = 1
                    break
            if flag == 0:
                curr[index] = arr[i]
                generate(index+1)
    generate(0)
    return ans
