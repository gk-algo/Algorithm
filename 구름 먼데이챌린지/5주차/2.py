n,m=map(int,input().split())
sandMap=[]
def countOne(arr):
    count=0
    for x in range(n):
        for x in range(m):
            if arr[x][y]==1:
                count+=1
    return count
def getVisited(x,y):
    visited[x][y]=1
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[0,1,-1,1,-1,0,1,-1]
    for i in range(8):
        X=x+dx[i]
        Y=y+dy[i]
        if 0<=X<n and 0<=Y<m and visited[X][Y]==0 and sandMap[X][Y]==1:
            getVisited(X,Y)

def Water():
    좌표=[]
    for x in range(n):
        for y in range(m):
            if sandMap[x][y]==0:
                dx=[-1,1,0,0]
                dy=[0,0,-1,1]
                for i in range(4):
                    X=x+dx[i]
                    Y=y+dy[i]
                    if 0<=X<n and 0<=Y<m:
                        if sandMap[X][Y]==1:
                            좌표.append([x,y])
    print(좌표)
    for x,y in 좌표:
        print(x,y,sandMap[x][y])
        sandMap[x][y]=0

for _ in range(n):
    sandMap.append(list(map(int,input().split())))
time=0
while 1:
    visited=[[0 for _ in range(m)]for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if sandMap[x][y]==1:
                ckX,ckY=x,y
    SUM=0
    for x in sandMap:
        print(x)
        SUM+=sum(x)
    print()
    Water()
