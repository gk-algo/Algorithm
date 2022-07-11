#https://www.acmicpc.net/problem/2493
n=int(input())
l=list(map(int,input().split()))
result=[0 for x in range(n)]
stack=[]
for x in range(n):
    while stack:
        if stack[-1][1]>l[x]:
            result[x]=stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append([x,l[x]])
result=map(str,result)
print(" ".join(result))