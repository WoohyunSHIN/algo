N = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 3

def main(N:int)->int:
    if N == 2:
        return 3

    if d[N] != 0:
        return d[N]

    d[N] = main(N-2)*2 + main(N-1)
    return d[N]

print(main(N))
