# Generate Permutation of binary string of size N

def solve(N):
    curr = [-1] * N
    ans = []
    def generate(index):
        if index == N:
            ans.append(curr.copy())
            return
        curr[index] = 0
        generate(index+1)
        curr[index] = 1
        generate(index+1)
    generate(0)
    return ans

print(solve(3))


