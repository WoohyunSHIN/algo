n = input()

def my_main(n:str)->int:
    ret = 0

    asci_dict= dict(zip(list(map(chr,range(97,105))),range(1,9)))
    position = (asci_dict[n[0]],int(n[1])) 

    grid = []
    for i in range(1,9):
        for j in range(1,9):
            grid.append((i,j))
    
    dx = [2,2,1,-1,-2,-2,1,-1]
    dy = [-1,1,2,2,1,-1,-2,-2] 

    for idx in range(len(dx)):
        nx = position[0] + dx[idx]
        ny = position[1] + dy[idx]
        if (nx, ny) in grid:
            ret += 1

    return ret

def main(n:str)->int:
    ret = 0
    row = int(n[1])
    col = int(ord(n[0]) - int(ord('a'))) + 1

    steps = [(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
    
    for step in steps:
        nr = row + step[0]
        nc = col + step[1]
        if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8:
            ret += 1

    return ret

#print(my_main(n))
print(main(n))