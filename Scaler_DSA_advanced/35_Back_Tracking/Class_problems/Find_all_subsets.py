a = [1,2,3]
arr = [-1,-1,-1]

def find_subsets(index = 0):
    if index == len(a):
        ls = []
        for i in range(len(arr)):
            if arr[i] == 1:
                ls.append(a[i])
        print(ls)
        return
    arr[index] = 0
    find_subsets(index+1)
    arr[index] = 1
    find_subsets(index+1)

if __name__ == "__main__":
    find_subsets()

