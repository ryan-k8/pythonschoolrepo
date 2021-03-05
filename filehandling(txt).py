 # file handling (txt)

with open('text.txt','r') as f:
	x = f.read()
	print(type(x))
	word = x.split()
	print(word)
	c1 = 0
	for i in word:
		if(i=='this'):
			c1+=1
	print(f'no of times this has appeared in the txt file - {c1}\n no of word {len(word)}')
	lines = x.splitlines()
	print(f'no of lines in the txt : {len(lines)} ')

with open('text.txt','r') as f:
	x = f.read()
	y = x.splitlines()
	print(f'y=x.splitlines : \n {y}')
	c2 = 0 
	for i in y:
	    z = i.split()
	    if z[0] =='this':
	    	c2+=1
	print(f'no of lines starting with "this" : {c2}')