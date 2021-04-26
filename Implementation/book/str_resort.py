
data = input()

def my_main(data:str)->str:
    ret = ''
    sum_number = 0
    data = sorted(data,key=lambda x: ord(x))
 
    for idx in range(len(data)):
        if ord(data[idx]) < 65:
            sum_number += int(data[idx])
        else:
            ret += data[idx]
    
    ret += str(sum_number) 

    return ret

print(my_main(data))
