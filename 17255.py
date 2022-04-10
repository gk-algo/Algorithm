#https://www.acmicpc.net/problem/17255
from collections import deque
def dfs(start,end,res):
    vis=deque(res[-1])
    if len(vis)==len(l):
        s.append(tuple(res))
        return 
    if start-1>=0:
        vis.appendleft(l[start-1])
        res.append(tuple(vis))
        dfs(start-1,end,res)
        vis.popleft()
        res.pop()
    if end+1<len(l):
        vis.append(l[end+1])
        res.append(tuple(vis))
        dfs(start,end+1,res)
        vis.pop()
        res.pop()
n=int(input())
l=list(str(n))
res=[]
s=[]
for x in range(len(l)):
    dfs(x,x,[(l[x])])
s=set(s)
print(len(s))
