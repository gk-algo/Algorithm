n=int(input())
h=[0]
h.extend(map(int,input().split()))
dp=[0 for _ in range(n+1)]
dp[1]=h[1]
for x in range(1,n+1):
    if h[x]>h[x-1]:
        dp[x]=dp[x-1]+1
    elif h[x]==h[x-1]:
        dp[x]=dp[x-1]
    else:
        if dp[x-1]<h[x]:
            dp[x]=dp[x-1]+1
        elif dp[x-1]==h[x]:
            dp[x]=dp[x-1]
        else:
            dp[x]=h[x]
print(max(dp))