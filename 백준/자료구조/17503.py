import sys
import heapq
input=sys.stdin.readline
n,m,k=map(int,input().split())
heap=[]
answer=[]
for _ in range(k):
    prefer,alchol=list(map(int,input().split()))
    heapq.heappush(heap,[alchol,prefer])
s=0
maxalchol=0
second_alchol=0
# heap에는 알콜이 낮은 순으로 들어감
# answer에는 perfer가 낮은 순으로 들어감
while heap:
    alchol, prefer=heapq.heappop(heap)
    if maxalchol<alchol:
        secondalchol=maxalchol
        maxalchol=alchol
    s+=prefer
    heapq.heappush(answer,[prefer,alchol])
    if len(answer)==n:
        if s>=m:
            print(maxalchol)
            exit()
        else:
            x=heapq.heappop(answer)
            s-=x[0]
            if x[1]==maxalchol:
                maxalchol=second_alchol
print(-1)
