t=int(input())
for _ in range(t):
    n=int(input())
    compare=[1 for x in range(n)]
    w=[]
    c=[]
    for _ in range(n):
        a,b=map(float, input().split())
        w.append(a)
        c.append(b)
    for x in range(n):
        for y in range(x):
            if w[x]>w[y] and c[x]<c[y]:
                compare[x]=max(compare[x],compare[y]+1)
    print(max(compare))