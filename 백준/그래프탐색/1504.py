import sys
import heapq
input=sys.stdin.readline
n,e=map(int,input().split())
INF=int(1e9)
l=[[INF for _ in range(n+1)] for _ in range(n+1)]
v=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    l[a][b]=c
    l[b][a]=c
    l[a][a]=0
    l[b][b]=0
v1,v2=map(int,input().split())

def dik(start,fin):
    distance=[INF]*(n+1)
    d = []
    heapq.heappush(d,(0,start))
    distance[start]=0
    while d:
        dist,t=heapq.heappop(d)
        if distance[t]<dist:
            continue
        for q in range(1,n+1):
            if dist+l[t][q]<distance[q]:
                distance[q]=dist+l[t][q]
                heapq.heappush(d,(distance[q],q))
    return distance[fin]
res=min(dik(1,v1)+dik(v1,v2)+dik(v2,n),dik(1,v2)+dik(v2,v1)+dik(v1,n))
if res<INF:
    print(res)
else:
    print(-1)