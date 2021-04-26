from collections import Counter

data = input()

def my_main(data:str)->int:
    ret = 0

    my_list = ['x']

    for idx in range(len(data)):
        if my_list[-1] != data[idx]:
            my_list.append(data[idx])

    my_list.remove('x')
    if len(my_list)==1:
        ret = 0
    else:
        ret = min(Counter(my_list).values())

    return ret

print(my_main(data))
