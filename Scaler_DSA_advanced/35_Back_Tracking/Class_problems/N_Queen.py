n = 4
curr = [0] * n
col = [0] * n
diag1 = [0] * 2 * n
diag2 = [0] * 2 * n

def generate(index):
    if index == n:
        return 1
    for i in range(n):
        if col[i] == 1:
            continue
        if diag1[index + i] == 1:
            continue
        if diag2[n + i - index] == 1:
            continue
        curr[index] = i
        col[i] = 1
        diag1[index + i] = 1
        diag2[n + i - index] = 1
        res = generate(index + 1)
        if res == 1:
            return 1
        curr[index] = 0
        col[i] = 0
        diag1[index + i] = 0
        diag2[n + i - index] = 0

print(generate(0))
for i in range(len(curr)):
    print(i,curr[i])

