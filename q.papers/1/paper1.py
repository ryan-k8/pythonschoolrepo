#p1-19
a = ['Cat','Dog','cat','Dog'] #dictionaries don't allow dupes 
def manip(f1):
    animal = {}
    for index in f1:
        if index in animal:
            animal[index] +=1
        else:
            animal[index]=1
    return (animal)
rec = manip(a)
print(rec)
print(len(rec))

#p1-34
l = [3,21,5,6,14,8,14,3]
def swapd7(l):
    print(f'before : {l}')
    n = len(l)
    i = 0
    while i<n:
        if l[i]%7==0:
            l[i],l[i+1]=l[i+1],l[i]
            i +=2
        else:
            i+=1
    print(f'after: {l}')
#swapd7(l)

#p1-35-1
def countlineste():
    c = 0
    with open('DATA.txt','rt') as f:
         x = f.read()
         lines = x.splitlines()
         print(lines)
         for j in lines:
             k = j.split()
             print(k)
             wb = k[0]
             we = k[-1]
             if wb[0] == 'T' and we[-1] == 'e':
                 c+=1
    print(f'no of lines which start and end with T or e resp. : {c}')

#countlineste()

#p1-35-2
def wordmaxvo():
    d = {}
    with open('DATA2.txt','r') as f:
        x = f.read()
        words = x.split()
        for word in words:
            n = 0
            for i in word:
                if i in ('a','i','e','o','u'):
                    n+=1
            d2 = {word:n}
            d.update(d2)
    maxvowc = max(list(d.values()))
    for i in d.keys():
        if d.get(i) == maxvowc:
            print(f'word with max vowel characters: {i}')
#wordmaxvo()

#p1-37-1
def POP_STACK(Arr):
    if len(Arr) == 0:
        print("error : stack underflow")
    return Arr.pop()

#p1-37-2
def PUSH_STACK(Arr,item):
    if len(Arr)>0:
        print(f'stack : {Arr}')
    else:
        print('error : stack underflow')
    if item%2==0:
        Arr.append(item)

#p1-40-1(i)
import pickle
def Add_Mobile(): #bfile structure : [Model,Company,Price]
    with open('Mobile.dat','wb') as f:
        rec = []
        while True:
            model = input('model :')
            company = input('company:')
            price = int(input('price'))
            rlst = [model,company,price]
            rec.append(rlst)
            a = input('more entries? (y/n) :')
            if a == 'n':
                break
        pickle.dump(rec,f)
#p1-40-1(ii)
 #import pickle
def count_company(company):
    count = 0 
    with open('Mobile.dat','rb') as f:
            while True:
                try:
                    s = pickle.load(f)
                    for i in s:
                        if i[1] == company:
                            count+=1
                except EOFError:
                    break
    print(f'no of mobiles by {company} : {count}')

#p1-40-2
def count_short_attendance():
    count = 0
    with open('ATTENDANCE.dat','rb') as f:
        while True:
            try:
                s = pickle.load(f)
                for i in s:
                    if i[2] < 75:
                        print(i)
                        count+=1
            except EOFError:
                break
    print(f'no of students with attedance below 75% : {count}')

