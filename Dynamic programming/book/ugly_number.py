n = int(input())

def main(n:int)->int:
    ret = 0
    arr = [1]
    num = 2

    while True:
        if len(arr) == n:
            break
        
        if num%2 == 0:
            arr.append(num)
            num += 1
            continue

        if num%3 == 0:
            arr.append(num)
            num += 1
            continue

        if num%5 == 0:
            arr.append(num)
            num += 1
            continue

        num += 1

    ret = arr[-1]
    return ret

print(main(n))