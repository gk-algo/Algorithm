import heapq
from collections import deque
n=int(input())
line=deque()
heap=[]
stack=[] #대기줄
for _ in range(n):
    l=list(map(str,input().split()))
    for x in l:
        a,b=x.split('-')
        b=int(b)
        heapq.heappush(heap,[a,b])
        line.append([a,b])
while heap:
    target=heapq.heappop(heap)
    while line:
        x=line.popleft()
        if x!=target:
            if stack:
                y=stack.pop()
                if y!=target:
                    stack.append(y)
                    stack.append(x)
                else:
                    if heap:
                        target=heapq.heappop(heap)
                        line.appendleft(x)
            else:
                stack.append(x)
        else:
            if heap:
                target=heapq.heappop(heap)
    while stack:
        x=stack.pop()
        if x==target:
            if heap:
                target=heapq.heappop(heap)
            else:
                print("GOOD")
                exit()
        else:
            print("BAD")
            exit()
print("GOOD")
