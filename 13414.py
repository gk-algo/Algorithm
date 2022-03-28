import sys
input=sys.stdin.readline
d=[]
stack=[]
check={}
k,l=map(int, input().split())
now=0
for _ in range(l):
    n=input().rstrip()
    d.append(n)
while d:
    tmp=d.pop()
    if check.get(tmp)!=1:
         stack.append(tmp)
         check[tmp]=1
for _ in range(k):
    print(stack.pop())