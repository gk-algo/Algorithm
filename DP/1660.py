n=int(input())
tri=[1,3]
d=[1,4]
idx=1
while n>d[-1]:
    idx+=1
    tri.append(tri[idx-1]+(tri[idx-1]-tri[idx-2])+1)
    d.append(d[idx-1]+tri[idx])
dp=[9999999 for x in range(n+1)]
dp[0]=0
dp[1]=1
for x in range(2,len(dp)):
    for std in d:
        if x-std>=0:
            dp[x]=min(dp[x],dp[x-std]+1)
print(dp[-1])