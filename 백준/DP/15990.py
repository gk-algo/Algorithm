import sys
input=sys.stdin.readline
r=1000000009
dp=[[0,0,0],[1,0,0],[0,1,0],[1,1,1]]
ans=[0 for x in range(100001)]
for k in range(3,100001):
        dp.append([(dp[k][1]+dp[k][2])%r,(dp[k-1][0]+dp[k-1][2])%r,(dp[k-2][0]+dp[k-2][1])%r])
for k in range(100001):
    ans[k]=(dp[k][0]+dp[k][1]+dp[k][2])%r
t=int(input())
for _ in range(t):
    x=int(input())
    print(ans[x])