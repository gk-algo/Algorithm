def bellman_ford(start):
    distance[start]=0

TC=int(input())
for _ in range(TC):
    n,m,w=map(int,input().split())
    edges=[[] for _ in range(n+1)]
    for _ in range(m):
        start, where, cost=map(int,input().split())
        edges[start].append([where,cost])
        edges[where].append([start,cost])
    for _ in range(w):
        start, where, minusCost=map(int,input().split())
        edges[start].append([where,cost])