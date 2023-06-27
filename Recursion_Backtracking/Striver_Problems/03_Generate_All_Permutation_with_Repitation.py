# Generate all permutation of [1,2,2]

def solve(arr):
    curr = [-1] * len(arr)
    from collections import Counter
    frequency_map = Counter(arr)
    ans = []

    def generate(index):
        if index == len(curr):
            ans.append(curr)
        for k,v in frequency_map.items():
            if v > 0:
                curr[index] = k
                frequency_map[k] -= 1
                generate(index+1)
                frequency_map[k] += 1


