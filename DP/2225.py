ans=0
n,k=map(int,input().split())
dp=[[0 for x in range(n+1)] for x in range(k+1)]
for t in range(k+1):
    dp[t][0]=1
for t in range(n+1):
    dp[1][t]=1
for x in range(2,k+1):
    for y in range(1,n+1):
        dp[x][y]=(dp[x-1][y]+dp[x][y-1])%1000000000
print(dp[-1][-1]%1000000000)