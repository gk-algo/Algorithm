from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
M=[]
for _ in range(n):
    M.append(list(str(input())))
vismap=[[[-1]*2 for x in range(m)] for y in range(n)]
def bfs():
    vismap[0][0][0]=1
    q=deque()
    q.append([0,0,0])
    while q:
        x,y,z=q.popleft()
        a=[-1,1,0,0]
        b=[0,0,-1,1]
        for t in range(4):
            X=x+a[t]
            Y=y+b[t]
            if 0<=X<n and 0<=Y<m:
                if M[X][Y]=='0' and vismap[X][Y][z]==-1:
                    vismap[X][Y][z]=vismap[x][y][z]+1
                    q.append([X,Y,z])
                elif M[X][Y]=='1'and vismap[X][Y][z]==-1 and z==0:
                    vismap[X][Y][1]=vismap[x][y][z]+1
                    q.append([X,Y,1])
bfs()
wallx=vismap[-1][-1][0]
wall=vismap[-1][-1][1]
if wallx==-1 and wall!=-1:
    print(wall)
elif wallx!=-1 and wall==-1:
    print(wallx)
else:
    print(min(wall,wallx))