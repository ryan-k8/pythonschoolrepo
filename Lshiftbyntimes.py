def Lshift(Arr,n):
	print(f"sample input : {Arr}")
	m = []
	n = n - 1 
	while n>=0:
		a = Arr[n]
		m.append(a)
		Arr.pop(n)
		n-=1
	l = len(m)
	for i in range(-1,-l-1,-1):
		Arr.append(m[i])
	print(f"sample output: {Arr}")
	
Lshift([10,20,30,40,60],3)
