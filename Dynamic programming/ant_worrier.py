n = input(int())
array = list(map(int,input().split()))

def main(n:int, array:list)->int:
    ret = 0 
    dp_table = [0] * 100

    dp_table[0] = array[0]
    dp_table[1] = array[1]
    
    for i in range(2,n):
        dp_table[i] = max(dp_table[i-1], dp_table[i-2]+array[i])

    return ret

main(n,array)


