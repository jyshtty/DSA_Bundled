# Generate all permutation of [1,2,2] with repetation.
# # # Example: arr = [1,2,2]
# # # Output: [[1,2,2], [2,1,2], [2,2,1]]   

from collections import Counter

def solve(arr):
    curr = [-1] * len(arr)
    frequency_map = Counter(arr)
    ans = []

    def generate(index):
        if index == len(curr):
            ans.append(curr[:])   # store a copy
            return                # ✅ important to stop recursion
        for k, v in frequency_map.items():
            if v > 0:
                curr[index] = k
                frequency_map[k] -= 1
                generate(index + 1)
                frequency_map[k] += 1

    generate(0)
    return ans

if __name__ == "__main__":
    print(solve([1, 2, 2]))


