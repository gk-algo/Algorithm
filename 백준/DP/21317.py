n=int(input())
d=[[0,0]]
for _ in range(n-1):
    d.append(list(map(int,input().split())))
dp=[0 for x in range(n+1)]
if n==1:
    print(0)
    exit()
elif n==2:
    print(d[1][0])
    exit()
dp[2]=d[1][0]
dp[3]=min(d[1][0]+d[2][0],d[1][1])
for x in range(4,n+1):
    dp[x]=min(dp[x-1]+d[x-1][0],dp[x-2]+d[x-2][1])
k=int(input())
MIN=9999999
for x in range(1,n-2):
    dpcopy=dp[:]
    if dp[x]+k<dp[x+3]:
        dpcopy[x+3]=dpcopy[x]+k
        for t in range(x+4,n+1):
            dpcopy[t]=min(dpcopy[t],dpcopy[t-1]+d[t-1][0],dpcopy[t-2]+d[t-2][1])
        if MIN>dpcopy[-1]:
            MIN=dpcopy[-1]
if MIN==9999999:
    print(dp[-1])
else:
    print(MIN)