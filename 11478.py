#https://www.acmicpc.net/problem/11478
import sys
sys.stdin.readline
s=input()
res=set()
for x in range(len(s)):
    for y in range(x, len(s)):
        tmp=s[x:y+1]
        res.add(tmp)
print(len(res))