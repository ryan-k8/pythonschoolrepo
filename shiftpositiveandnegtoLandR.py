def ShiftPNLR(l):
	print(f'original input : {l}')
	positive = []
	negative = []
	n = len(l)
	for i in range(n):
		if float(l[i])>=0:
		   positive.append(l[i])              #positive.insert(0,x)
		else:
		   negative.append(l[i])
	l = positive+negative
	print(f'final output: {l}')


ShiftPNLR([-1,2,5,0,7,-6,-7,-3])
