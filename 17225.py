import heapq
heap=[]
tmpl=[]
B=[]
R=[]
a,b,n=map(int,input().split())
for _ in range(n):
    t,c,m=map(str,input().split())
    t=int(t)
    m=int(m)
    time=t
    first=1
    for _ in range(m):
        if not first:
            if c=='B':
                time=time+a
            elif c=='R':
                time=time+b
        tmpl.append([time,c])
        first=0
for x in tmpl:
    if x[1]=='B':
        heapq.heappush(heap,x)
for x in tmpl:
    if x[1]=='R':
        heapq.heappush(heap,x)
index=1
while heap:
    tmp=heapq.heappop(heap)
    if tmp[1]=='B':
        B.append(index)
    else:
        R.append(index)
    index+=1
B=list(map(str,B))
R=list(map(str,R))
print(len(B))
print(' '.join(B))
print(len(R))
print(' '.join(R))