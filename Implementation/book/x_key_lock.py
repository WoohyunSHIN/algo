
m, n = map(int,input().split())
# 3 3
keys = []
for _ in range(m):
    keys.append(list(map(int, input().split())))

locks = []
for _ in range(n):
    locks.append(list(map(int, input().split())))

def _resize(m:int, n:int, keys:list)->list:
    ret = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if i > m-1 or j > m-1:
                tmp.append(0)
            else:
                tmp.append(keys[i][j])
        ret.append(tmp)

    return ret

def _rotation_90(keys:list)->list:
    ret = []

    for row_idx in range(len(keys)):
        tmp = []
        for col_idx in range(len(keys)):
            tmp.append(keys[len(keys)-col_idx-1][row_idx])
        ret.append(tmp)

    return ret

def _checker(keys:list,locks:list)->bool:
    ret = True

    for i in range(len(keys)):
        for j in range(len(keys)):
            locks[i][j] += keys[i][j]
            if locks[i][j] != 1:
                return False

    return ret

def _move(keys:list,times:int)->list:
    ret = []



    return ret


def my_main(m:int, n:int, keys:list, locks:list)->bool:
    ret = False

    if m < n:
        keys = _resize(m,n,keys)

    print(f"keys {keys}")
    print("----")

    for times in range(n*n):
        _move(keys,times)

        for _ in range(4):
            keys = _rotation_90(keys)
            if _checker(keys,locks):
                ret = True
                return ret

    return ret


print(my_main(m, n, keys, locks))
