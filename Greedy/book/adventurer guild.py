n = map(int,input().split())
data = list(map(int, input().split()))

def my_main(n:int, data:list)->int:
    ret = 0 
    
    #x = 1
    # 공포도가 1이상인 모험가는 반드시 1명이상 구성된 그룹 -> 5게

    #x = 2
    # 공포도가 2이상 모험가는 반드시 2명이상 구성된 그룹 -> 2개

    #x = 3
    # 공포도가 3이상 모험가는 반드시 3명이상 구성된 그룹 -> 0개

    for x in range(1, max(data)+1):
        cnt = 0
        for some_data in data:
            if x <= some_data:
                cnt += 1
        #print(f"x : {x} count : {cnt}")
        if x <= (cnt//x):
            ret = cnt//x
    return ret

def main(n:int, data:list)->int:
    data.sort()

    result = 0
    count = 0

    for i in data:
        count += 1
        print(f"count : {count}")
        if count >= i:
            result += 1
            count = 0
        
    return result

#print(my_main(n,data))
print(main(n,data))