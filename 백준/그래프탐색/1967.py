from collections import deque
INF=int(1e9)
n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))
def bfs(s):
    res,resgo=0,0
    q=deque()
    q.append((s,0))
    vis=[0 for x in range(n+1)]
    vis[s]=1
    while q:
        where, dis=q.popleft()
        for x in tree[where]:
            next=x[0]
            cost=x[1]
            if vis[next]==0:
                vis[next]=1
                q.append((next,dis+cost))
                if dis+cost>res:
                    res=dis+cost
                    resgo=next
    return resgo,res
resgo,res=bfs(1)
go, result=bfs(resgo)
print(result)


