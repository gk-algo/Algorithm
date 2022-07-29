import heapq
n=int(input())
결과=0
힙=[]
for _ in range(n):
    heapq.heappush(힙, int(input()))
while len(힙)!=1:
    임시=heapq.heappop(힙)
    if 힙:
        임시=임시+heapq.heappop(힙)
    결과+=임시
    heapq.heappush(힙,임시)
print(결과)