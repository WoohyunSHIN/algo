n = int(input())

computers = []

for _ in range(n):
    computers.append(list(map(int, input())))

def solution(n:int,computers:list)->int:
    answer = 0

    graph = [[]]

    for i in range(n):
        tmp = []
        for j in range(n):
            if computers[i][j] == 1:
                tmp.append(j)
        graph.append(tmp)

    print(graph)

    return answer

print(solution(n,computers))