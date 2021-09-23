import math
m, n = map(int,input().split())

def method_1(m:int,n:int)->None:
    ret = []
    for i in range(m,n+1):
        is_prime_number = True

        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                #print(f"i = {i}, j = {j}, i%j = {i%j}")
                is_prime_number = False
                break
        
        if is_prime_number:
            ret.append(i)
    
    for i in ret:
        print(i)
method_1(m,n)

def method_2(m:int,n:int)->None:
    table = [True for _ in range(n+1)]
    table[0] = False
    table[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if table[i]:
            k = 2
            while i * k <= n:
                table[i * k] = False
                k += 1

    for idx in range(m,n+1):
        if table[idx]:
            print(idx)

method_2(m,n)
