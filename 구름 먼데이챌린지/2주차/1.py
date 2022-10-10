t=int(input())
for _ in range(t):
    n=int(input())
    v=list(map(int,input().split()))
    count=0
    average=sum(v)/n
    for x in v:
        if x>=average:
            count+=1
    print(count, end='')
    print('/',end='')
    print(n)