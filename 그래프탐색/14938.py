from collections import deque
n, d, r = map(int, input().split())
region = [0]
region.extend(list(map(int, input().split())))
m = [[999999 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    m[a][b] = m[b][a] = c
for t in range(n+1):
    for x in range(n+1):
        for y in range(n+1):
            if x==y:
                m[x][y]=0
            elif m[x][y]>m[x][t]+m[t][y]:
                m[x][y]=m[x][t]+m[t][y]
ans=[]
for x in range(n+1):
    item=0
    for y in range(n+1):
        if m[x][y]<=d:
            item+=region[y]
    ans.append(item)
print(max(ans))