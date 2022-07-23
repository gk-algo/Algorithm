def bfs(v,vis):
    q1=[v]
    q2=[]
    c=[0 for x in range(102)]
    cnt=1
    vis.append(v)
    while q1:
        q2=[]
        while q1:
            v=q1.pop(0)
            for x in range(102):
                if li[x][v]==1 and x not in vis:
                    vis.append(x)
                    q2.append(x)
                    c[x]=cnt
        q1=q2[:]

        cnt+=1
    return c

n,m=map(int,input().split())
num=[]
res=[]
li=[[0]*(102) for x in range(102)]
LIST=[]
for x in range(m):
    a,b=map(int,input().split())
    li[a][b]=1
    li[b][a]=1
    LIST.append(a)
    LIST.append(b)
LIST=list(set(LIST))
LIST.sort()
for x in LIST:
    vis=[]
    num.append(sum(bfs(x,vis)))
MIN=99999
for x in range(len(num)):
    if MIN>num[x]:
        MIN=num[x]
        res=x
print(LIST[res])