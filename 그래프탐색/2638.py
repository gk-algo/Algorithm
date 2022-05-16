from collections import deque
import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

#(0,0)에서 부터 bfs실행, 기존l과 합을 구해서 0인 부분을 내부공기(2)로 갱신
def insidebfs():
    oxy=[]
    q=deque()
    q.append((0,0))
    vis=[[0 for x in range(m)] for y in range(n)]
    while q:
        x,y=q.popleft()
        a=[-1,1,0,0]
        b=[0,0,-1,1]
        for t in range(4):
            X=x+a[t]
            Y=y+b[t]
            if 0<=X<n and 0<=Y<m and l[X][Y]==0 and vis[X][Y]==0:
                q.append((X,Y))
                vis[X][Y]=1
    insideoxy=[]
    for x in range(n):
        for y in range(m):
            tmp=l[x][y]+vis[x][y]
            if tmp==0:
                insideoxy.append([x,y])
    for t in insideoxy:
        l[t[0]][t[1]]=2



#내,외부 공기를 구분한 뒤에 2개 이상 닿은 치즈를 제거한 후에, 내부공기를 다시 확인
def cheese():
    cheese=[]
    insidebfs()
    for x in range(n):
        for y in range(m):
            if l[x][y]==1:
                cheese.append([x,y])
    a=[-1,1,0,0]
    b=[0,0,-1,1]
    release=[]
    for t in cheese:
        x=t[0]
        y=t[1]
        cnt = 0
        for i in range(4):
            X=x+a[i]
            Y=y+b[i]
            if 0<=X<n and 0<=Y<m and l[X][Y]==0:
                cnt+=1
        if cnt>1:
            release.append([x,y])
    for x in release:
        l[x[0]][x[1]]=0

    for x in range(n):
        for y in range(m):
            if l[x][y]==2:
                l[x][y]=0

#반복및출력
def check(t):
    SUM=0
    for x in range(n):
        SUM+=sum(l[x])
    if SUM==0:
        print(t)
        return
    else:
        cheese()
        check(t+1)

n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
check(0)