n, k = map(int, input().split())

def my_main(n:int, k:int)->int:
    ret = 0

    while True:
        if n==1:
            break
        if n%k == 0:
            n = n//k
            ret += 1
        else:
            ret += 1
            n -= 1

    return ret 

def main(n:int, k:int)->int:
    ret = 0 
    
    while n >= k:
        while n%k != 0:
            n -= 1
            ret += 1
        n //= k
        ret += 1
    while n > 1:
        n -= 1
        ret += 1

    return ret

def main2(n:int, k:int)->int:
    ret = 0
    
    while True:
        # n 이 k로 나뉘어 지는 수는 target 이라고 한다
        target = (n//k) * k
        ret += (n - target)
        n = target

        if n<k:
            break

        ret +=1
        n //= k
    ret += (n-1)
    return ret
        
print(my_main(n,k))
print(main(n,k))
print(main2(n,k))