# 시간 복잡도 = O(logN)

def binary_search(array:list,target:int,start:int,end:int)->int:
    if start > end:
        return None
    
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    elif array[mid] < target:
        return binary_search(array,target,mid+1,end)    

n, target = map(int,input().split())
array = list(map(int,input().split()))
array = sorted(array)
start = 0
end = n - 1

result = binary_search(array,target,start,end)
if result == None:
    print(-1)
else:
    print(result+1)


"""
10 7
1 3 5 7 9 11 13 15 17 19
4
"""