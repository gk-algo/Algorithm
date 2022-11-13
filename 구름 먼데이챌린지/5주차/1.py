n,m=map(int,input().split())
def findMeal(x,y,m):
    antMap[x][y]=0
    for reach in range(1,m+1):
        dx=[-reach,reach,0,0]
        dy=[0,0,reach,-reach]
        for i in range(4):
            X=x+dx[i]
            Y=y+dy[i]
            if 0<=X<n and 0<=Y<n:
                if antMap[X][Y]==2:
                    antMap[x][y]=1
antMap=[]
for _ in range(n):
    antMap.append(list(map(int,input().split())))
for x in range(n):
    for y in range(n):
        if antMap[x][y]==1:
            findMeal(x,y,m)
count=0
for x in range(n):
    for y in range(n):
        if antMap[x][y]==1:
            count+=1
print(count)