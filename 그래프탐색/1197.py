import heapq
def mst(start):
    cost=0
    vis[start]=1
    heap=vertex[start][:]
    heapq.heapify(heap)
    while heap:
        now=heapq.heappop(heap)
        if vis[now[1]]==0:
            cost+=now[0]
            if vertex.get(now[1]):
                for x in vertex[now[1]]:
                    heapq.heappush(heap,x)
            vis[now[1]]=1
    return cost

v,e=map(int,input().split())
vis=[0]*(v+1)
vertex=dict()
for _ in range(e):
    a,b,c=map(int,input().split())
    if vertex.get(a) is None:
        vertex[a]=[[c,b]]
    else:
        vertex[a].append([c,b])
    if vertex.get(b) is None:
        vertex[b]=[[c,a]]
    else:
        vertex[b].append([c,a])
print(mst(1))