#https://www.acmicpc.net/problem/4386
import heapq
def prim(start):
    vis=[0 for _ in range(n+1)]
    heap=[]
    cost=0
    heapq.heappush(heap,[0,start])
    while heap:
        if sum(vis)==n:
            break
        now_cost,now_place=heapq.heappop(heap)
        if vis[now_place]==0:
            cost+=now_cost
            vis[now_place]=1
            for x in node[now_place]:
                heapq.heappush(heap,x)
    return cost
        
n=int(input())
node=[[]for _ in range(n+1)]
arr=[]
for x in range(n):
    a,b=map(float,input().split())
    arr.append([round(a,2),round(b,2)])
for x in range(len(arr)):
    for y in range(len(arr)):
        if x!=y:
            cost=round(((arr[x][0]-arr[y][0])**2+(arr[x][1]-arr[y][1])**2)**(1/2),2)
            node[x+1].append([cost,y+1])
print(prim(1))

