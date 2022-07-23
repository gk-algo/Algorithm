#https://www.acmicpc.net/problem/13265
import sys
from collections import deque
input=sys.stdin.readline
def bfs(start):
    global impossible
    q=deque()
    if vis[start]=="B":
        origin="B"
        op="W"
    else:
        origin="W"
        op="B"
    for x in connection[start]:
        if vis[x]==0:
            q.append(x)
            vis[x]=op
        elif vis[x]==origin:
            impossible=1
            return
    while q:
        bfs(q.popleft())

t=int(input())
for _ in range(t):
    connection=dict()
    impossible=0
    n,m=map(int,input().split())
    vis=[0 for _ in range(n+1)]
    for _ in range(m):
        x,y=map(int,input().split())
        if x!=y:
            if connection.get(x):
                connection[x].extend([y])
            else:
                connection[x]=[y]
            if connection.get(y):
                connection[y].extend([x])
            else:
                connection[y]=[x]
    if connection:
        for x in connection.keys():
            if vis[x]==0:
                vis[x]="B"
                bfs(x)
        if impossible==1:
            print("impossible")
        else:
            print("possible")
    else:
        print("possible")