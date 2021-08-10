import sys
from collections import deque

N, M, K, X = map(int,sys.stdin.readline().split())

q = deque()
INF = 300001

for _ in range(M):
    A, B = map(int,sys.stdin.readline().split())
    q.append((A,B))
 
def main(N:int,K:int,X:int,q:deque)->list:


for i in main(N,K,X,q):
    print(i)