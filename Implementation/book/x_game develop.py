n, m = map(int,input().split())
caracter = list(map(int, input().split()))
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

def _turn(caracter:list)->list:
    caracter[2] += 1
    if caracter[2] == 4:
        caracter[2] = 0
    return caracter

def _can_move(caracter:list, grid:list, n:int, m:int)->bool:
    ret = False
    # 북 -> 서 -> 남 -> 동
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]

    nx, ny = caracter[0]+dx[caracter[2]], caracter[1]+dy[caracter[2]]
    
    if nx > n or nx < 0 or ny > m or ny < 0 or grid[nx][ny] == 1 or grid[nx][ny] == 9:
        ret = False
        return ret
    else:
        ret = True
        return ret
    
    return ret

def _move(caracter:list, grid:list)->(list,list):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]

    caracter[0] = caracter[0] + dx[caracter[2]]
    caracter[1] = caracter[1] + dy[caracter[2]]

    grid[caracter[0]][caracter[1]] = 9
    return caracter, grid

def _end_game(caracter:list,grid:list)->bool:
    ret = False
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]

    nx, ny = caracter[0]-dx[caracter[2]], caracter[1]-dy[caracter[2]]
    print(grid)
    if (nx > n or nx < 0 or ny > m or ny < 0) or grid[nx][ny] == 1:
        ret = True
        return ret
    else:
        return ret

def _go_back(caracter:list,grid:list)->(list,list):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]

    caracter[0] = caracter[0] - dx[caracter[2]]
    caracter[1] = caracter[1] - dy[caracter[2]]

    grid[caracter[0]][caracter[1]] = 9
    return caracter, grid

def my_main(n:int, m:int, caracter:list, grid:list)->int:
    ret = 0 
    grid[caracter[0]][caracter[1]] = 9
    print(grid)

    while True:

        if _end_game(caracter,grid):
            caracter, grid = _go_back(caracter,grid)
            if _end_game(caracter,grid):
                return ret
            else:
                continue


        for _ in range(0,5):
            caracter = _turn(caracter)
            #print(_can_move(caracter, grid, n, m))
            if _can_move(caracter, grid, n, m):
                print(f"direct : {_}")
                caracter, grid = _move(caracter,grid)
                print(grid)
                break
        ret += 1

            # if _end_game(caracter,grid):
            #     return ret
            # else:
            #     caracter, grid = _go_back(caracter,grid)
            #     print(grid)
            #     break

    return ret



print(my_main(n, m, caracter, grid))