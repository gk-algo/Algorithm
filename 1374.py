#https://www.acmicpc.net/problem/1374
import sys
import heapq
from turtle import end_fill
input=sys.stdin.readline
n=int(input())
lecture=[]
q=[]
vis=[0 for _ in range(100001)]
for _ in range(n):
    l=list(map(int,input().split()))
    heapq.heappush(lecture,[l[1],l[2],l[0]])
start, end, no=heapq.heappop(lecture)
heapq.heappush(q,end)
while lecture:
    start, end, no=heapq.heappop(lecture)
    if q[0]<=start:
        heapq.heappop(q)
    heapq.heappush(q,end)
print(len(q))

        
    

    
