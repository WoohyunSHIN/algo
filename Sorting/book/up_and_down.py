n = int(input())
array = []

for _ in range(n):
    data = int(input())
    array.append(data)

def main(array:list)->str:
    ret = ' '
    array = sorted(array,reverse=True)
    array = list(map(str,array))
    ret = ret.join(array)
    return ret

print(main(array))