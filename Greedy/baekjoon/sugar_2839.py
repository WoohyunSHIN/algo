# 18, 4, 6, 9, 11
# 4, -1, 2, 3, 3

n = int(input())

def box_count(n:int)->int:
    ret = 0

    while True:
        if n%5 == 0:
            ret += n//5
            break
        ret += 1
        n -= 3
        
        # Base Case
        if n < 0:
            ret = -1
            break

    return ret

print(box_count(n))
