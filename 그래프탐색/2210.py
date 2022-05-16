def dfs(x,y,number):
    if len(number)==6:
        if number not in result:
            result.append(number)
        return
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]
        if 0<=X<5 and 0<=Y<5:
            dfs(X,Y,number + m[X][Y])
m=[]
l=[]
result=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for x in range(5):
    l=list(map(str, input().split()))
    m.append(l)
for x in range(5):
    for y in range(5):
        dfs(x,y,m[x][y])
print(len(result))