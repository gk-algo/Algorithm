import heapq
n,m=map(int, input().split())
l=list(map(int, input().split()))
heapq.heapify(l)
for _ in range(m):
    tmp=heapq.heappop(l)+heapq.heappop(l)
    heapq.heappush(l,tmp)
    heapq.heappush(l,tmp)
print(sum(l))