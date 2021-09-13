from sys import stdin
X = int(stdin.readline())

# SETTING main2
d = [0] * (X+1)
INF = X + 1


def main2(X:int)->int:
    #if X < INF - 1:
    #    print(f"X = {X}, d = {d}")
    if X == INF:
        return INF

    # 종료조건
    if X == 1:
        return 0

    # 이미 계산한 문제라면 그대로 반환
    if d[X] != 0:
        return d[X]

    # 아직 계산하지 않은 문제라면 점화식에 따라서 결과 반환
    divid_5 = INF
    if X % 5 == 0:
        divid_5 = int(X/5)
    divid_3 = INF
    if X % 3 == 0:
        divid_3 = int(X/3)
    divid_2 = INF
    if X % 2 == 0:
        divid_2 = int(X/2)
    minus_1 = X - 1 

    d[X] = min(main2(divid_5), main2(divid_3), main2(divid_2), main2(minus_1)) + 1
    return d[X]

def main(X:int)->int:
    dp = [0] * 30001
    ret = 0
    nums = []
    nums.append(X)

    while True:
        if dp[1] == 1:
            break

        tmp = []
        for num in nums:
            if dp[num] == 0:
                if num % 5 == 0:
                    tmp.append(num // 5)
                if num % 3 == 0:
                    tmp.append(num // 3)
                if num % 2 == 0:
                    tmp.append(num // 2)
                tmp.append(num - 1)
            dp[num] = 1
        nums.clear()
        nums = tmp
        ret += 1


    return ret - 1

# print(main(X))
print(main2(X))