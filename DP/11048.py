import sys
input=sys.stdin.readline
n,m=map(int,input().split())
ma=[]
for x in range(n):
    ma.append(list(map(int,input().split())))
dp=[[0 for x in range(m)] for x in range(n)]
dp[0][0]=ma[0][0]
for x in range(n):
    for y in range(m):
        if x>0 and y>0:
            dp[x][y]=max(dp[x-1][y-1],dp[x][y-1],dp[x-1][y])+ma[x][y]
        elif x>0:
            dp[x][y]=dp[x-1][y]+ma[x][y]
        elif y>0:
            dp[x][y]=dp[x][y-1]+ma[x][y]
print(dp[-1][-1])