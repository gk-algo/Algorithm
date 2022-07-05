m=int(input())
d=dict()
for _ in range(m):
    a,b,=map(int,input().split())
    if d.get(a):
        d[a].extend([b])
    else:
        d[a]=[b]
    if d.get(b):
        d[b].extend([a])
    else:
        d[b]=[a]
for x in d.keys():
    d[x].sort()
for x in d.keys():
    print(x,d[x])