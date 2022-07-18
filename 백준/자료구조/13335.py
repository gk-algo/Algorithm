from collections import deque
n,w,l=map(int,input().split())
truck=deque(list(map(int,input().split())))
bridge=deque([0]*w)
time=0
while truck:
    bridge.popleft()
    if len(bridge)<w:
        x=truck.popleft()
        if sum(bridge)+x<=l:
            bridge.append(x)
        else:
            truck.appendleft(x)
            bridge.append(0)
    time+=1
while sum(bridge)!=0:
    bridge.append(0)
    bridge.popleft()
    time+=1
print(time)



