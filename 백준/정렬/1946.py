import sys
input=sys.stdin.readline
t=int(input().rstrip())
for _ in range(t):
    n=int(input().rstrip())
    res=n
    l=[]
    result=[]
    for _ in range(n):
        l.append(list(map(int,input().rstrip().split())))
    l.sort(key=lambda x:x[0])
    for x in l:
        result.append(x[1])
    last=float('inf')
    for x in result:
        if last>x:
            last=x
        else:
            res-=1
    print(res)
