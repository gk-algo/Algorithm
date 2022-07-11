n,s=map(int,input().split())
l=list(map(int,input().split()))
start=0
end=0
ret=100001
sum=l[0]
while True:
    if sum<s:
        if end==n-1:
            break
        end+=1
        sum+=l[end]
    else:
        ret=min(ret,end-start+1)
        sum-=l[start]
        start+=1
if ret==100001:
    print(0)
else:
    print(ret)