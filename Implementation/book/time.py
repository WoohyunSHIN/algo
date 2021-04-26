n = int(input())

def my_main(n:int)->int:
    ret = 0 
    target = '3'
    hours = list(range(0,24))

    mins = list(map(str,range(0,60)))
    seconds = list(map(str,range(0,60)))
    hours = list(map(str,hours[:n+1]))

    for hour in hours:
        for minu in mins:
            for second in seconds:
                if target in hour or target in minu or target in second:
                    ret += 1

    return ret

def main(n:int)->int:
    ret = 0

    for h in range(n+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h)+str(m)+str(s):
                    ret += 1
    
    return ret

print(my_main(n))
print(main(n))