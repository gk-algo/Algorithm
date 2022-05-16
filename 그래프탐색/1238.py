import heapq
n,m,x=map(int,input().split())
INF=int(1e9)
g=[[] for x in range(n+1)]
for _ in range(m):
    a,b,t=map(int,input().split())
    g[a].append((t,b))

def dik(start,end):
    distance=[INF for x in range(n+1)]
    distance[start]=0
    heap=[(0,start)]
    while heap:
        cost,now=heapq.heappop(heap)
        if distance[now]<cost:
            continue
        for x in g[now]:
            tmp=x[0]+cost
            if tmp<distance[x[1]]:
                distance[x[1]]=tmp
                heapq.heappush(heap,(tmp,x[1]))
    return distance[end]
res=[0 for x in range(n+1)]
for t in range(1,n+1):
    res[t]+=dik(t,x)+dik(x,t)
print(max(res[1:]))