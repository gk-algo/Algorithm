import heapq
n,m=map(int, input().split())
카드=list(map(int,input().split()))
heapq.heapify(카드)
for _ in range(m):
    카드1=heapq.heappop(카드)
    결과=카드1
    if 카드:
        카드2=heapq.heappop(카드)
        결과+=카드2
        heapq.heappush(카드, 결과)
    heapq.heappush(카드,결과)
print(sum(카드))