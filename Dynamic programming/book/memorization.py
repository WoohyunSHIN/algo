# 다이나믹 프로그래밍을 활용할 수 있는 조건은 2가지 있다.
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

# 아래의 방식은 Top-Down 방식이라고 말한다. 큰 문제를 해결하기 위해 작은 문제를 호출하기 때문에.
d = [0] * 100

def fibo(x:int)->int:
    print(f'f({x})', end=' ')
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# 아래의 방식은 Bottom-Up 방식이라고 말한다. 작은 문제 부터 차근차근 답을 도출 하기 댸문에
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])