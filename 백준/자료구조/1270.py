#https://www.acmicpc.net/problem/1270
import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    d=dict()
    land=list(map(int, input().split()))
    check=0
    for x in land[1:]:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    M=max(d,key=d.get)
    if d[M]>(land[0]//2):
        check=1
    if check:
        print(M)
    else:
        print("SYJKGW")