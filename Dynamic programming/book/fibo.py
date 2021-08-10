def fibo(x:int)->int:
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)