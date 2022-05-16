import sys

input = sys.stdin.readline
n = int(input())
maxdp=[0,0,0]
mindp=[0,0,0]
tmp1=[0,0,0]
tmp2=[0,0,0]
for _ in range(n):
    a,b,c=map(int,input().split())
    for x in range(3):
        if x==0:
            tmp1[0]= a+ max(maxdp[x],maxdp[x+1])
            tmp2[0]= a+ min(mindp[x],mindp[x+1])
        elif x==1:
            tmp1[1]=b+max(maxdp[x-1],maxdp[x],maxdp[x+1])
            tmp2[1]=b+min(mindp[x-1], mindp[x],mindp[x+1])
        else:
            tmp1[2]=c+max(maxdp[x-1],maxdp[x])
            tmp2[2]=c+min(mindp[x-1],mindp[x])
    for x in range(3):
        maxdp[x]=tmp1[x]
        mindp[x]=tmp2[x]
print(max(maxdp),min(mindp))