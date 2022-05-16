dp=[0 for x in range(251)]
dp[0]=1
dp[1]=1
for x in range(2,251):
    dp[x]=dp[x-1]+2*dp[x-2]
while (1):
    try:
        n=int(input())
        print(dp[n])
    except:
        break