#https://www.acmicpc.net/problem/2665
from collections import deque
def bfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            X=x+dx[i]
            Y=y+dy[i]
            if 0<=X<n and 0<=Y<n:
                if vis[X][Y]==-1:
                    if m[X][Y]==0:
                        vis[X][Y]=vis[x][y]+1
                        q.append((X,Y))
                    else:
                        vis[X][Y]=vis[x][y]
                        q.appendleft((X,Y))
n=int(input())
m=[]
ch=0
for x in range(n):
    x=list(input())
    x=list(map(int,x))
    m.append(x)
vis=[[-1 for _ in range(n)] for _ in range(n)]
vis[0][0]=0
bfs(0,0)
print(vis[-1][-1])