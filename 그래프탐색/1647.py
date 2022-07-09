import heapq
import sys
input=sys.stdin.readline


n,m=map(int,input().split())
route=[[] for _ in range(n+1)]
vis=[0 for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    route[a].append((c,b))
    route[b].append((c,a))
cost=0
maxcost=0
heap=[(0,1)]
cnt=0
while heap:
    if cnt==n:
        break
    nowcost,now=heapq.heappop(heap)
    if vis[now]==0:
        for x,y in route[now]:
            if vis[y]==0:
                heapq.heappush(heap,(x,y))
        vis[now]=1
        cost+=nowcost
        maxcost=max(maxcost,nowcost)
        cnt+=1
print(cost-maxcost)