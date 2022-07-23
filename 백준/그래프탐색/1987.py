import sys
input=sys.stdin.readline
def dfs(x,y,cnt):
    global M
    vis[ord(m[x][y])-65]=1
    M=max(M,cnt)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]
        if 0<=X<r and 0<=Y<c and vis[ord(m[X][Y])-65]==0:
                dfs(X,Y,cnt+1)
                
                vis[ord(m[X][Y])-65]=0
               
M=0
r,c=map(int,input().rstrip().split())
vis=[0 for x in range(26)]
m=[]
for _ in range(r):
    m.append(list(input()))
dfs(0,0,1)
print(M)