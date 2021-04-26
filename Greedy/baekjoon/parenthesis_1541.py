data = input()

def main(data:str)->int:
    import re
    p = re.compile('[0-9]+')
    ret = 0
    right = ''
    left = ''
    for idx in range(len(data)):
        if data[idx] == '-':
            right = data[:idx]
            left = data[idx+1:]

            right = list(map(int,p.findall(right)))
            left = list(map(int,p.findall(left)))


            ret = sum(right) - sum(left)
            return ret

    data = list(map(int,p.findall(data)))
    ret = sum(data)

    return ret

print(main(data))
        
    