n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# my_list = [a,b,c,d,e,f,g] <- len(my_list) = m
# [7,7,3,2,1,0] -> x = 7, y = 7 7,7,7,7,7,7,7
# k = 3 -> x,x,x,y,x,x,x,y  
# n = len(data)

def my_main(m:int, k:int, data:list)->int:
    ret = 0
    data = sorted(data, reverse=True)
    tmp = k
    while m > 0:

        while k > 0:
            ret += data[0] # fist bigest number
            k -= 1
            m -= 1
        k = tmp
        ret += data[1] # second 
        m -= 1
        
    return ret 

def main(n:int, m:int, k:int, data:list)->int:
    data.sort()
    
    first = data[n-1]
    second = data[n-2]

    result = 0

    while True:
        for i in range(k):
            if m==0:
                break
            result += first
            m -= 1
        if m==0:
            break
        result += second
        m -= 1
    return result

def main2(n:int, m:int, k:int, data:list)->int:
    first = data[n-1]
    second = data[n-2]
    my_sum = first*k + second

    a = m//(k+1) # 몫
    b = m%(k+1)# 나머지

    return my_sum*a + first*b

print(my_main(m,k,data))
print(main(n,m,k,data))
print(main2(n,m,k,data))
