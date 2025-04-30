arr = [1,2,3]

def generate(curr, index=0):
    if index == len(arr):
        print(curr)
        return
    for i in range(len(arr)):
        flag = 0
        for j in range(index):
            if curr[j] == arr[i]:
                flag = 1
        if flag == 0:
            curr[index] = arr[i]
            generate(curr, index + 1)

if __name__ == "__main__":
    curr = [-1 for i in range(len(arr))]
    generate([-1,-1,-1])
