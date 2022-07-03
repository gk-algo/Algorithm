k,n=map(int,input().split())
a=[]
res=[]
for _ in range(k):
    a.append(int(input()))
a.sort()
low=1
top=max(a)
while low<=top:
    mid=(low+top)//2
    cnt=0
    for x in a:
        cnt=cnt+x//mid
    if cnt>=n:
        low=mid+1
    else :
        top=mid-1
print(top)