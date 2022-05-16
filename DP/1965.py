import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
dp=[1 for x in range(n)]
for x in range(n):
    for y in range(x):
        if l[x]>l[y]: 
            dp[x]=max(dp[x],dp[y]+1)
print(max(dp))