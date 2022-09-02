n=int(input())
l=list(map(int,input().split()))
m=int(input())
dp=[[0 for _ in range(n)] for _ in range(n)]
# for x in range(n):
#     for y in range(x,n):
#         if l[x]==l[y] and dp[x+1][y-1]==1:
#             dp[x][y]=1
for idx in range(n):
    for start in range(n-idx):
        end=start+idx
        if start==end:
            dp[start][end]=1
        elif l[start]==l[end]:
            if start+1==end:
                dp[start][end]=1
            elif dp[start+1][end-1]==1:
                dp[start][end]=1
for _ in range(m):
    s,e=map(int,input().split())
    print(dp[s-1][e-1])
