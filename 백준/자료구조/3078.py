import sys
input=sys.stdin.readline
from collections import deque
n,k=map(int,input().split())
count=[0 for x in range(21)]
name=[]
window=deque()
ans=0
for x in range(n):
    name.append([x+1,len(input().rstrip())])
for now in name:
    window.append(now[1])
    count[now[1]]+=1
    if len(window)==k+1:
        x=window.popleft()
        count[x]-=1
        ans+=count[x]
while window:
    x=window.popleft()
    count[x]-=1
    ans+=count[x]
print(ans)
