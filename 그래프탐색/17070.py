import sys
input=sys.stdin.readline
def dfs(status,x,y):
    if x==n-1 and y==n-1:
        global c
        c+=1
        return
    if status==0:
        if y+1<n and m[x][y+1]==0:
            dfs(0,x,y+1)
        if x+1<n and y+1<n and m[x+1][y]==0 and m[x+1][y+1]==0 and m[x][y+1]==0:
            dfs(2,x+1,y+1)
    elif status==1:
        if x+1<n and m[x+1][y]==0:
            dfs(1,x+1,y)
        if x+1<n and y+1<n and m[x+1][y]==0 and m[x][y+1]==0 and m[x+1][y+1]==0:
            dfs(2,x+1,y+1)
    elif status==2:
        if y+1<n and m[x][y+1]==0:
            dfs(0,x,y+1)
        if x+1<n and m[x+1][y]==0:
            dfs(1,x+1,y)
        if x+1<n and y+1<n and m[x+1][y]==0 and m[x+1][y+1]==0 and m[x][y+1]==0:
            dfs(2,x+1,y+1)

n=int(input())
m=[]
for _ in range(n):
    m.append(list(map(int,input().split())))
c=0
dfs(0,0,1)
print(c)