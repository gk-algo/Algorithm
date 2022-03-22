def do(l):
    l[0]=l[0]+l[1]
    l[1]=l[0]
    
n,m=map(int, input().split())
l=list(map(int, input().split()))
l.sort()
for x in range(m):
    do(l)
print(sum(l))