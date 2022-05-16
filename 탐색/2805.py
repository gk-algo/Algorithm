n,m=map(int, input().split())
namu=list(map(int, input().split()))
low=1
top=max(namu)
while low<=top:
    d=0
    mid=(top+low)//2
    for x in namu:
        if (x-mid)>=0:
            d=d+(x-mid)
        if d>=m:
            break
    if d<m:
        top=mid-1
    elif d>=m:
        low=mid+1
print(top)