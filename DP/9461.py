def dp(n):
    dp=[0]*101
    dp[1],dp[2],dp[3],dp[4],dp[5]=1,1,1,2,2
    for x in range(6,n+1):
        dp[x]=dp[x-1]+dp[x-5]
    return dp[n]
T=int(input())
for _ in range(T):
    n=int(input())
    print(dp(n))