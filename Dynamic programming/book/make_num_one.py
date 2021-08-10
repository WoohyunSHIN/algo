from sys import stdin
X = int(stdin.readline())

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

print(main(X))