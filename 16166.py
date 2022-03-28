def dfs(start, dest,cnt):
    havetogo=[]
    for x in route[start]:
        if x==dest:
            return cnt
        if len(h[x])==1 and not vis.get(x): #환승 못하는 것들
            vis[x]=1
        else:
            if not vis.get(x):
                vis[x]=1
                havetogo.append(x)
    for x in havetogo:
        return dfs(x, dest,cnt+1)
n=int(input())
vis={}
vis[0]=1
h={}
route={}
ck={}
for x in range(1,n+1):
    l=list(map(int,input().split()))
    for y in l[1:]:
        if h.get(y):
            h[y].extend([x])
        else:
            h[y]=list()
            h[y].extend([x])
        if route.get(y):
            route[y].extend(l[1:])
        else:
            route[y]=l[1:]
dest=int(input())
c=dfs(0,dest,0)
if c is None:
    print(-1)
else:
    print(c)
