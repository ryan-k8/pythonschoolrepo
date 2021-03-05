def bubbles(l):
	print(f"before sorting: {l}")
	n = len(l)
	for i in range(n):
		for j in range(0,n-i-1):
			if l[j]>l[j+1]:
				l[j],l[j+1] = l[j+1],l[j]
	print(f"after sorting: {l}")


bubbles([2,0,7,9,5,50,1])