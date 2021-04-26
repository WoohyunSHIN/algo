n = int(input())
data = list(map(str, input().split()))

def my_main(n:int, data:list)->str:
    ret = ' '

    grid = []
    position = (1,1)

    for x in range(1,n+1):
        for y in range(1,n+1):
            grid.append((x,y))

    for direc in data:
        if direc == 'R':
            check = (position[0],position[1]+1)
            if check in grid:
                position = check
            else:
                pass
        if direc == 'L':
            check = (position[0],position[1]-1)
            if check in grid:
                position = check
            else:
                pass
        if direc == 'U':
            check = (position[0]-1,position[1])
            if check in grid:
                position = check
            else:
                pass
        if direc == 'R':
            check = (position[0]+1,position[1])
            if check in grid:
                position = check
            else:
                pass

    position = tuple(map(str,position))        
    ret = ret.join(position)
    return ret

def main(n:int ,data:list)->str:
    x, y = 1, 1
    plans = data


    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    move_types = ['L','R','U','D']


    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > x or ny > n:
            continue
        x, y = nx, ny

    ret = (x, y)
    return ret


print(my_main(n,data))
print(main(n,data))