def bin(x, start, end):
    mid=(start+end)//2
    if l[mid][0]>x:
        bin(x,start,mid)
    elif l[mid][0]<x:
        bin(x,mid,end)
    else:
        return mid

import heapq
n,m,k=map(int,input().split())
l=[]
maxnum=0
for _ in range(k):
    a,b=map(int,input().split())
    if b>maxsize:
        maxsize=b
    l.append([b,a])
l.sort()
for x in range(maxsize):
    start=bin(x,0,len(l))
    while l[start][0]!=x:
        start+=1