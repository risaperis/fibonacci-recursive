def recur_jibber(n):
	if n <= 1:
		return n
	else:
		return(recur_jibber(n-1) + recur_jibber(n-2))

nterms = 377

if nterms <= 0:
	print("no negative numbers or zero ")
else:
	print("Jibber Sequence:")
	for i in range(nterms):
		print(recur_jibber(i))
