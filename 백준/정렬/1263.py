n=int(input())
m=float('inf')
l=[]
for _ in range(n):
    t,s=map(int,input().split())
    l.append([t,s])
l.sort(key=lambda x:x[1])
for x in range(len(l)):
    S=l[x][0]
    for y in range(x):
        S+=l[y][0]
    if l[x][1]<S:
        print(-1)
        exit()
    else:
        m=min(m,l[x][1]-S)
print(m)