def ok(x,y):
	x = x+y
	print(x,'#',y)
	return (x)
p= 10
q= 20

ok(p,q)
print(p,'$',q)
p = ok(p,q)
print(p,'$',q)