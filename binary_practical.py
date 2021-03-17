import pickle

with open("example.dat","wb") as f:
        rec = []
        while True:
                rno = int(input("rno:"))
                name = input("name:")
                marks = int(input("marks:"))
                r = [rno,name,marks]
                rec.append(r)
                a = input("more(y/n)?")
                if a =='n':
                        break

        pickle.dump(rec,f)

print(rec)

def updatemarks(r,m):
        rec2 = []
        with open("example.dat","rb") as f:
            while True:
                try:
                    s = pickle.load(f)
                    for i in s:
                        rec2.append(i)
                except EOFError:
                        break
        for j in rec2:
                if j[0]== r:
                        j[2] = m
        with open("example.dat",'wb') as f:
            pickle.dump(rec2,f)
        #code below is only for viewing
        with open("example.dat","rb") as f:
            while True:
                try:
                    x = pickle.load(f)
                    for i in x:            
                        print(i)
                except EOFError:
                    break

updatemarks(1,99)
