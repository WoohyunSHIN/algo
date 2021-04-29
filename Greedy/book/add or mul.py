data = input()

def my_main(data:str)->int:
    ret = 0

    new_data = []
    for idx in range(len(data)):
        new_data.append(int(data[idx]))

    ret = int(new_data[0])

    for idx in range(1,len(new_data)):
        num = int(new_data[idx])

        if num <= 1 or ret <= 1:
            ret += num
        else:
            ret *= num

    return ret

print(my_main(data))
