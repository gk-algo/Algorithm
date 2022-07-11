n=int(input())
dp=[0 for x in range(n+1)]
dp[0]=1
for x in range(2,n+1):
    if x%2==0:
        dp[x]=3*dp[x-2]+2*sum(dp[:x-2])
print(dp[n])