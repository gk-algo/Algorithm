from collections import deque
n,m,k=map(int,input().split())
node={}
visited=[0 for _ in range(n+1)]
def bfs(start):
    q=deque([start])
    visited[start]=1
    while q:
        now=q.popleft()
        for x in node[now]:
            if visited[x]==0:
                q.append(x)
                visited[x]=visited[now]+1
        
for _ in range(m):
    u,v=map(int,input().split())
    if node.get(u):
        node[u].append(v)
    else:
        node[u]=[v]
    if node.get(v):
        node[v].append(u)
    else:
        node[v]=[u]
bfs(1)
if(visited[n]!=0 and visited[n]-1<=k):
    print("YES")
else:
    print("NO")