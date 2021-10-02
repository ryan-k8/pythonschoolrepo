"""
Problem Statement: Given an Integer, Print all the Prime Numbers between 0 and that
Integer.
"""
n = int(input("enter Integer "))

#--------------------------------
for i in range(2,n+1):
	isPrime = True
	for j in range(2,i):
		if (i%j ==0):
			isPrime = False

	if isPrime:
		print(i)

#------------------------------------
n = int(input('enter Integer again '))
i  = 2 
while i <= n :
	j = 2
	isPrime = True 
	while j < i:
		if (i%j ==0):
			isPrime = False
		j+=1
	if isPrime:
		print(i)
	i+=1


#-------------------------------------