#---section(1)----

 #1 b) True  c)2ndName
 
 #2 [6,82,5]

 #3 comma seperated values
 
 #4 c)**
 
 #5 b) T[2]=-29 #tuples are immutable
 
 #6 d ={1:'Monday',2:'Tuesday',3:'Wednesday'}
 
 #7 30

 #8 abs() eg -9.7 --> 9.7 and +9.7 --> 9.7

 #9 smtp

 #10 Cyber Stalking

 #11 'ORDER BY' 

 #12 to check if the column has null value

 #13 SUM()

 #14 b.ALTER 

 #!5 microwave/radio wave

 #16 d.list

#17 puterS

#18 SHOW tables;

#19 Wireless Fidelity (Wi-Fi)

#20) c.PRIMARY KEY

#21 bps < kbps < mpbs < gbps < tbps

#--section(2)---
 
#22) a ) ItemNo b) deg - 4 cardinality -7 
#22) c ) INSERT INTO STORE VALUES(2010,'Note Book',25)
#22  d) b) DROP TABLE store; e) desc STORE;

#23 a) csv b ) a   c ) reader d) close()
#23 e)  Arjun 123@456
 #      Arunima aru@nima
 #      Frieda myname@FRD

#24 a) 13 b) False

#25 Viruses require an active host program or an already-infected and active os
#order for viruses to run, cause damage and infect other executable files or documents
#Worms are stand-alone malicious programs that can self-replicate.

#26 a)simple mail transfer protocol b) extensible markup language
# c) local area network d) intellectual property rights

#27 formal para - during definition ; actual para - function callback

 #28
value=30
for val in range(0,value):
    if val%4==0:
       print(val*4)
    elif val%5==0:
       print(val*5)
    else:
       print(val+10)
  

# 29 (ii)30#40#50#   lower-3 , upper -4

#30 A table may have more than one such attribute/group of attributes that identifies a
#   tuple uniquely, all such attribute(s) are known as Candidate Keys.

#31 fetchone() fetches one row from the query result while fetchall() gets all rows

'''32
 data definiton language ; data manipulation language
 dml - INSERT,SELECT,UPDATE
'''
#33
st = 'Fun@Python3.0' #
m = ""
for i in range(0,len(st)):
    if(st[i].isupper()):
        m +=st[i].lower()

    elif st[i].islower():
        m+=st[i].upper()

    else:
        if i%2==0: 
           m+=st[i-1]
        else:
           m+="#"
print(f'{m}')

#output : fUN#pYTHONn#.



 #--section(3)---

# 34
def Lshift(Arr,n):
    for i in range(0,n):
       a = Arr[0]
       Arr.pop(0)
       Arr.append(a)
    print(Arr)

    
#35 i)
#define it as function
with open('STORY.txt','rt') as f:
     c = 0
     x = f.read()
     words = x.split()
     for i in words:
        if i =="Me" or "My":
           c+=1
    print(f'no of "Me" or "my" words : {c}')


# 35 ii)
def AMCount():
   with open('STORY.txt','rt') as f:
        n = 0
        x = f.read()
        for j in x:
           if j.lower()=='a'or'm':
              n+=1
        print(f'occurences of A/a or m/m : {n}')
    


#36 sql done

#37
def PUSH(Arr):
   stk = []
   for i in Arr:
      if i%5==0:
      stk.append(i)
   if len(stk)>0:
      print(stk)
   else: 
      print('error : stack underflow ')

def POP(Arr):
   if len(stk)>0:
      return stk.pop()
   else:
      print("error: stack underflow")



#38 a) HR center(max computer) b) diagram from hr to all c) switch
  # d) when distance between 2 buildings more than 70m
   # e) WAN (1000km+)
 

"""39
i) SELECT * FROM Teacher WHERE Department='History';
ii) SELECT Name FROM Teacher WHERE Gender='F' AND Department='Mathematics';
iii) SELECT Name,Date_of_join FROM Teacher ORDER BY Date_of_join;
iv) SELECT Name,Salary,Age FROM Teacher WHERE Gender='M';
v) SELECT Name,0.1*Salary AS  Bonus  FROM Teacher;

"""

#40-1
 
import pickle
def CreateFile():
   with open('Book.dat','wb') as f:
       record = []
       while True:
           bno = int(input("book no :"))
           bname = input('book name : ')
           author = input('author : ')
           price = int(input('price : '))
           r = [bno,bname ,author,price]
           record.append(r)
           a = input('more enteries? (y/n) : ')
           if a == 'n':
              break
      pickle.dump(f,record)
def CountRec(Author):
    with open('Book.dat','rb') as f:
        n = 0
        while True:
             try:
                s = pickle.load(f)
                for i in s:
                  if i[2] == Author:
                     n+=1
            except EOFError:
                break
        return n
    

#40-2
def countrec():
   with open('STUDENT.dat','rb') as f:
       c = 0 
       while True: 
            try:
               s = pickle.load(f)
               for i in s:
                  if i[2] > 75:
                     c+=1
                     print(i)
            except EOFError:
               break
      print(f'no of students with above 75% : {c}')