n,m=map(int,input().split())
p=list(map(int,input().split()))
party=[]
for x in range(m):
    v=list(map(int,input().split()))
    party.append(v[1:])
if p[0]==0:
    print(m)
else:
    del p[0]
    stack=[]
    stack.extend(p)
    vis=[0 for _ in range(n+1)]
    for x in p:
        vis[x]=1
    while stack:
        x=stack.pop()
        for t in party:
            if x in t:
                for r in t:
                    if vis[r]==0:
                        stack.append(r)
                        p.append(r)
                        vis[r]=1
    cnt=0
    for x in party:
        ck = 0
        for y in p:
            if y in x:
                ck=1
        if ck==0:
            cnt+=1
    print(cnt)