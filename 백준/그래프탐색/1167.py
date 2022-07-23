import heapq
INF=int(1e9)
def dik(start):
    heap=[]
    distance=[INF for _ in range(n+1)]
    distance[start]=0
    heapq.heappush(heap,(start,0))
    while heap:
        now,cost=heapq.heappop(heap)
        if distance[now]<cost:
            continue
        for x in g[now]:
            next=x[0]
            tmpcost=x[1]
            if cost+tmpcost<distance[next]:
                distance[next]=cost+tmpcost
                heapq.heappush(heap,(next,distance[next]))
    MAX=0
    where=0
    for x in range(len(distance))[1:]:
        if distance[x]>MAX:
            MAX=distance[x]
            where=x
    return where,MAX
n=int(input())
g=[[]for _ in range(n+1)]
for x in range(n):
    tmp=list(map(int,input().split()))
    for x in range(1,len(tmp),2):
        if tmp[x]!=-1:
            g[tmp[0]].append(tmp[x:x+2])
where,res=dik(1)
where,res=dik(where)
print(res)