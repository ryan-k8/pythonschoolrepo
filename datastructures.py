# stack (lifo)
l = [2,4,6,8]

def push(x):
	l.append(x)

def pop():
	del_element = l[-1]
	print(f'{del_element} is the popped off element')
	l.pop()
	
push(7)
print(f'after push - {l}')

pop()
print(f'after pop - {l}')


# queue (fifo)

q = ['b','c']

def enqueue(x):
	q.insert(0,x)

def dequeue():
	dequeued_element = q[-1]
	q.pop(-1)
	print(f'dequeued element is {dequeued_element}')

enqueue('a')
print(f'after enqueue - {q}')

dequeue()
print(f'after dequeue - {q}')
