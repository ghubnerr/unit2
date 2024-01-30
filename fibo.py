def fib(n):
	result = []
	for idx in range(0, n):
		if idx == 0:
			result.append(0)
		elif idx == 1:
			result.append(1)
		else:
			result.append(result[idx - 1] + result[idx - 2])
	return result
