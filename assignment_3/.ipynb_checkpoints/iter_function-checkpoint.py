def iter_z(c,max_iter=100):
	z = 0
	for i in range(max_iter):
		z = z**2 + c
		if abs(z) > 2:
			return i
	return max_iter
