import heapq
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def dfs(start):
    global cnt
    visited[start]=cnt
    cnt+=1
    for where in nodeEdgeList[start]:
        if visited[where]==0:
            dfs(where)

N,M,R=map(int,input().split())
nodeEdgeList=[[] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
cnt=1
for _ in range(M):
    start,destination=map(int,input().split())
    nodeEdgeList[start].extend([destination])
    nodeEdgeList[destination].extend([start])
for x in range(N):
    nodeEdgeList[x].sort()
dfs(R)
for x in visited[1:]:
    print(x)