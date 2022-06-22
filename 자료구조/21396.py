from collections import Counter
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    cnt=0
    n,target=map(int,input().split())
    l=Counter(list(map(int,input().split())))
    if target==0:
        for x in l.keys():
            cnt+=(l[x]-1)*l[x]
    else:
        for x in l.keys():
            cnt+=(l[x]*l[x^target])
    print(cnt//2)