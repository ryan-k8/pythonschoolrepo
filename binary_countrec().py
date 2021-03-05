import pickle

with open('sample.dat','wb') as f:
    rec = [[1,'r',76],[2,'s',70],[3,'t',80]]
    pickle.dump(rec,f)

def countrec():
    with open('sample.dat','rb') as f:
        c = 0
        while True:
            try:
                s = pickle.load(f)
                for i in s:
                    if i[2] > 75:
                        print(i)
                        c +=1
            except EOFError:
                break
        print(f'no of students with percentage greater than 75 : {c}')

countrec()
