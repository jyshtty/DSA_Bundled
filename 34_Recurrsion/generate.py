curr = [-1] * 3
arr = [1, 2, 3]

def generate(index):
    if len(arr) == index:
        print(curr)
    else:
        for i in range(len(arr)):
            flag = 0
            for j in range(index):
                if curr[j] == arr[i]:
                    flag = 1
            if flag == 0:
                curr[index] = arr[i]
                generate(index + 1)

generate(0)