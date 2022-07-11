import sys
input=sys.stdin.readline
t=int(input())
dp=[0,1,2,4]
for _ in range(t):
    x= int(input())
    for k in range(len(dp),x+1):
        if k>len(dp)-1:
            dp.append((dp[k-3]+dp[k-2]+dp[k-1])%1000000009)
    print(dp[x])