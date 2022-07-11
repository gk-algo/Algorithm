d, p = map(int, input().split())
dp = [0 for _ in range(d+ 1)]
for _ in range(p):
    l, c = map(int, input().split())
    for x in reversed(range(d+1)):
        if x>=l:
            dp[x] = max(dp[x], min(c, dp[x-l]))
    if c > dp[l]:
        dp[l] = c
print(dp[-1])