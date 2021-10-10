def all_primes(n:int) -> None:
    i = 2
    while i <= n:
        if (i==2):
            print(2)
            i+=1
            continue
        j = 2 
        flag = True
        while j < i:
            if i%j == 0:
                flag = False 
                break
            j+=1
        if flag:
            print(i)
        i+=1



all_primes(21)
