#https://www.acmicpc.net/problem/2467
n=int(input())
l=list(map(int,input().split()))
start=0
end=n-1
m=10000000000000
ret=[]
while start<end:
    if m>abs(l[start]+l[end]):
        m=abs(l[start]+l[end])
        ret=[l[start],l[end]]
    if l[start]+l[end]>0:
        end=end-1
    elif l[start]+l[end]==0:
        break
    else:
        start=start+1
print(ret[0],ret[1])
