"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
def main(n:int, triangle:list)->int:
    ret = 0 
    # i = n
    # j = list lengh
    
    for i in range(1,n):
        for j in range(len(triangle[i])):
            if j == 0:
                left = 0
                right = triangle[i-1][j]
            elif j == len(triangle[i])-1:
                right = 0
                left = triangle[i-1][j-1]
            else:
                left = triangle[i-1][j-1]
                right = triangle[i-1][j]

            triangle[i][j] = triangle[i][j] + max(left, right)

    ret = max(triangle[n-1])

    return ret

n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int,input().split())))

print(main(n,triangle))
