n=int(input())
m=int(input())
road=[[99999999 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    if road[a][b]>c:
        road[a][b]=c
for t in range(n+1):
    for x in range(n+1):
        for y in range(n+1):
            if road[x][y]>road[x][t]+road[t][y]:
                road[x][y]=road[x][t]+road[t][y]
            if x==y:
                road[x][y]=0
for x in range(1,n+1):
    for t in road[x][1:]:
        if t==99999999:
            print(0, end=" ")
        else:
            print(t, end=" ")
    print()