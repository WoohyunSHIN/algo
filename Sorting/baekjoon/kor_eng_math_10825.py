import sys

n = int(sys.stdin.readline())

grades = []

for _ in range(n):
    name, kor, eng, math = map(str,sys.stdin.readline().split())
    grades.append((name,int(kor),int(eng),int(math)))

def main(n:int,grades:list)->None:
    # cond 4.
    grades = sorted(grades, key=lambda data:data[0])
    # cond 3.
    grades = sorted(grades, key=lambda data:data[3],reverse=True)
    # cond 2.
    grades = sorted(grades, key=lambda data:data[2])
    # cond 1.
    grades = sorted(grades, key=lambda data:data[1],reverse=True)
    
    for data in grades:
        print(data[0])

main(n,grades)