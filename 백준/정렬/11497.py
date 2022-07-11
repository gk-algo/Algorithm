t=int(input())
for _ in range(t):
    m=0
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    for x in range(n-2):
        m=max(m,abs(l[x]-l[x+2]))
    print(m)