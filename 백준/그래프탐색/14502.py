import sys
import copy
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
ans=0
space=[]
for _ in range(n):
    a=list(map(int,input().split()))
    space.append(a)
    
def wall(cnt):
    if cnt==3:
        virus()
        return 
    for x in range(n):
        for y in range(m):
            if space[x][y]==0:
                space[x][y]=1
                wall(cnt+1)
                space[x][y]=0
    
def virus():
    global ans
    newspace=copy.deepcopy(space)
    q=deque()
    cnt=0
    for x in range(n):
        for y in range(m):
            if newspace[x][y]==2:
                q.append([x,y])
    while q:
        x,y=q.popleft()
        a=[1,-1,0,0]
        b=[0,0,1,-1]
        for i in range(4):
            X=x+a[i]
            Y=y+b[i]
            if 0<=X<n and 0<=Y<m:
                if newspace[X][Y]==0:
                    newspace[X][Y]=2
                    q.append([X,Y])
    for x in range(n):
        for y in range(m):
            if newspace[X][Y]==0:
                cnt+=1
    cnt=0
    for i in newspace:
        cnt+=i.count(0)
    ans=max(ans,cnt)
    return 


            
wall(0)
print(ans)