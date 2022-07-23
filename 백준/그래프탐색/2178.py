def miro(space,vis):
    q=[(0,0)]
    vis[0][0]=1
    while q:
        x,y=q.pop(0)
        if x==n-1 and y==m-1:
            return vis[x][y]
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
        for i in range(4):
            ax=x+dx[i]
            ay=y+dy[i]
            if 0<=ax<n and 0<=ay<m and vis[ax][ay]==0 and space[ax][ay]==1:
                q.append((ax,ay))
                vis[ax][ay]=vis[x][y]+1
n,m=map(int,input().split())
space=[]
vis=[[0]*m for x in range(n)]
vis2=[[0]*m for x in range(n)]
res=[]
res2=[]
for x in range(n):
    inp=list(str(input()))
    inp=list(map(int,inp))
    space.append(inp)
print(miro(space,vis))