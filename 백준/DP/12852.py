n=int(input())
dp=[99999999 for x in range(n+4)]
m=[[] for x in range(n+4)]
dp[0],dp[1]=0,0
dp[2],dp[3]=1,1
m[0]=[0]
m[1]=[1]
m[2]=[1]
m[3]=[1]
if n>3:
    for x in range(4,n+1):
        if x%3==0:
            dp[x]=min(dp[x],dp[x//3]+1)
            if dp[x]==dp[x//3]+1:
                k=x//3
        if x%2==0:
            dp[x]=min(dp[x],dp[x//2]+1)
            if dp[x]==dp[x//2]+1:
                k=x//2
        dp[x]=min(dp[x],dp[x-1]+1)
        if dp[x]==dp[x-1]+1:
            k=x-1
        m[x].extend(m[k])
        m[x].extend([k])
print(dp[n])
if n!=1:
    print(n, end=' ')
for x in reversed(m[n]):
    print(x, end=' ')