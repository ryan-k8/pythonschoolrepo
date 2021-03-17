
l = []
def push(x):
	l.append(x)

def pop():
	del_element = l[-1]
	print(f'{del_element} is the popped off element')
	l.pop()

while True:
	print("1.PUSH")
	print("2.POP")
	print("3.QUIT")
	c = int(input("enter choice : "))
	if c == 1:
		while True:
		    x = input("enter element to be pushed")
		    push(x)
		    a = input("more(y/n)?")
		    if a == 'n':
		    	break		
		print(l) # just for showing result
	if c == 2:
		pop()
	if c == 3:
		break
