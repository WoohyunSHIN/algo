from sys import stdin

n = int(stdin.readline())

array = list(map(int,stdin.readline().split()))

def main(n:int,array:list)->int:
    ret = 0
    array = sorted(array)

    if n%2 == 1:
        ret = array[int(n/2)-1]

    else:
        right = array[int(n/2)]
        left = array[int(n/2)-1]
        ret = left
    
    return ret

print(main(n,array))
