import pickle
# appending to binary file is included!
def write():
	f = open('b.dat','wb')
	records = [] 
	while True:
		sno = int(input('SNO : '))
		name = input('NAME : ')
		rec = [sno,name]
		records.append(rec)
		a = input('more?(y/n)')
		if a == 'n':
			print('RECORD ENTRY OVER')
			break
	pickle.dump(records,f)
	f.close()

def append():
	f = open('b.dat','ab')
	records = [] 
	while True:
		sno = int(input('SNO : '))
		name = input('NAME : ')
		rec = [sno,name]
		records.append(rec)
		a = input('more?(y/n)')
		if a == 'n':
			print('RECORD ENTRY OVER')
			break
	pickle.dump(records,f)
	f.close()		
def read():
	f = open('b.dat','rb')
	while True:
		try:
			s=pickle.load(f)
			for i in s:
				print(i)
		except EOFError:
			break
	f.close()
read()