n=int(input())
dp=[0,1,2]
for x in range(1,n):
    dp.append(dp[x]+dp[x+1])
print(dp[n]%10007)