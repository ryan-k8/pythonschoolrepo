#CBSE SQP Q34
def Lshift(Arr,n):
    print(f'array before operation : {Arr}')
    for i in range(n):
        a = Arr[0]
        Arr.pop(0)
        Arr.append(a)
    print(f'array after operation : {Arr}')

#CBSE sample Input:
Arr = [10,20,30,40,12,11]
n = 2
Lshift(Arr,n)
