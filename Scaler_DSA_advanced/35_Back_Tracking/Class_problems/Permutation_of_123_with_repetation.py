arr = [1,2,2]
curr = [-1 for i in range(len(arr))]

from collections import Counter
frequency_map = Counter(arr)

def generate(index):
	if index == len(arr):
		print(curr)
		return
	for k,v in frequency_map.items():
		if v > 0:
			curr[index] = k
			frequency_map[k] -=1
			generate(index + 1)
			frequency_map[k] +=1

generate(0)