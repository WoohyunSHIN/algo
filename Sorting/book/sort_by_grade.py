n = int(input())
array = []

for _ in range(n):
    name, grade = map(str,input().split())
    array.append((name,int(grade)))

def main(array:list)->str:
    ret = ''
    array = sorted(array,key=lambda x:x[1])

    for data in array:
        name = data[0]
        # grade = data[1]
        ret += (name+' ')

    return ret

print(main(array))