n=int(input())
a=[0 for t in range(n+3)]
dp=[0 for t in range(n+3)]
for t in range(1,n+1):
    a[t]=int(input())
dp[1]=a[1]
dp[2]=a[1]+a[2]
dp[3]=max(a[1]+a[3],a[2]+a[3])
for x in range(4,n+1):
    dp[x]=max(dp[x-2]+a[x], a[x-1]+dp[x-3]+a[x])
print(dp[n])