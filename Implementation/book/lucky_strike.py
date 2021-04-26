


n = input()

def my_main(n:str)->str:
    ret = ''
    right = []
    left = []
    mid = len(n)//2
    right_sum = 0
    left_sum = 0

    if len(n)%2 == 0:
        right = n[:mid]
        left = n[mid:]
    else:
        right = n[:mid]
        left = n[mid+1:]
    
    for idx in range(len(right)):
        right_sum += int(right[idx])
        left_sum += int(left[idx])
    
    if right_sum == left_sum:
        ret = 'LUCKY'
    else:
        ret = 'READY'

    return ret

print(my_main(n))

