import sys
input=sys.stdin.readline
n=int(input())
m=[]
for x in range(n):
    m.append(list(map(int,input().split())))
x=0
y=0
cnt=0
dp=[[0 for x in range(n)] for x in range(n)] 
dp[0][0]=1
for x in range(n):
    for y in range(n):
        if (x==n-1 and y==n-1):
            print(dp[-1][-1])
        else:
            jump=m[x][y]
            if x+jump<n:
                dp[x+jump][y]+=dp[x][y]
            if y+jump<n:
                dp[x][y+jump]+=dp[x][y]