# file handling (binary) using pickle module(simple)
import pickle 

with open('b.dat','wb') as f:
	rec = ['x','y','z']
	pickle.dump(rec,f)

with open('b.dat','rb') as f:
	x = pickle.load(f)
    print(x)