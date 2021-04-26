
from collections import Counter
data = input().rstrip('\n')

def my_main(data:str)->int:
    ret = len(data)
    
    for size in range(1,len(data)+1):
        a = 0
        b = size
        new_list = []
        while True:
            if b >= len(data):
                new_list.append(data[a:])
                break
            new_list.append(data[a:b])
            a = b
            b += size
        print(new_list)
        cnt = 1
        for idx in range(len(cnt)):
            for compare_idx in range(idx+1, len(cnt)):
                if new_list[idx] != new_list[compare_idx]:
                    break
                cnt+=1




    return ret

print(my_main(data))
