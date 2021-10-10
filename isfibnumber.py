def solve(n:int) -> bool:
    a = 0
    b = 1
    is_fib_num = False
    while a <= n:
        if (a==n):
            is_fib_num = True
        c = a+b
        a = b
        b = c 
    print(is_fib_num)


solve(int(input()))
