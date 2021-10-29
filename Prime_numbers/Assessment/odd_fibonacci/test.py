def foo(A):
	flag = A[0]
	count = 1
	ls = []
	for i in range(1,len(A)):
		if flag == A[i]:
			count += 1
		else:
			ls.append(count)
			count = 1
			flag = A[i]
		if i == len(A) -1:
			ls.append(count)
	max_len = max(ls)
	sum = 0
	for i in ls:
		if i < max_len:
			sum = sum + (max_len - i)
	return sum, ls
A = 'bbbab'
print(foo(A))

