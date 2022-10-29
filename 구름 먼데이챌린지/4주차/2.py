park=[]
def check(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]
        if 0<=X<n and 0<=Y<n:
            if park[X][Y]==0:
                minus[x][y]-=1
n=int(input())
minus=[[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    tmp=list(map(int,input().split()))
    park.append(tmp)
cnt=0
SUM=0
for x in park:
    SUM+=sum(x)
while SUM!=0:
    minus=[[0 for _ in range(n)] for _ in range(n)]
    cnt+=1
    for x in range(n):
        for y in range(n):
            if park[x][y]!=0:
                check(x,y)
    for x in range(n):
        for y in range(n):
            park[x][y]+=minus[x][y]
            if (park[x][y]<0):
                park[x][y]=0
    SUM=0
    for x in park:
        SUM+=sum(x)
print(cnt)