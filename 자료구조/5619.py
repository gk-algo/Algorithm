#https://www.acmicpc.net/problem/5619

n=int(input())
l=[]
result=[]
for _ in range(n):
    l.append(int(input()))
l.sort()
cnt=0
miin=0
result=[]
for x in l[:4]:
    for y in l[:4]:
        if x!=y:
            tmp1=int(str(x)+(str(y)))
            result.append(tmp1)
result.sort()
print(result[2])