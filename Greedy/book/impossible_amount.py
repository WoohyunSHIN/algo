n = int(input())
data = list(map(int,input().split()))

def my_main(n:int, data:list)->int:
    ret = 0
    amount = sum(data)
    coin_types = sorted(data, reverse=True)

    for target in range(amount):
        tmp = target
        for coin in coin_types:
            if target <= 0:
                break
            if target >= coin:
                target = target - coin 

        if target != 0:
            ret = tmp 
            break

    return ret

def main(n:int, data:list)->int:
    ret = 0
    target = 1
    data = sorted(data)
    for x in data:
        print(f"x : {x} target : {target}")
        if target < x:
            break
        target += x
    ret = target
    return ret

#print(my_main(n,data))
print(main(n,data))