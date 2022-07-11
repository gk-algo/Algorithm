#https://www.acmicpc.net/problem/2866
r,c=map(int,input().split())
table=[]
for _ in range(r):
    l=list(input())
    table.append(l)
cnt=r-1
strlist=['' for _ in range(c)]
while table:
    li=table.pop()
    ch={}
    k=0
    for x in range(c):
        if ch.get(strlist[x]+li[x]) is None:
            strlist[x]=strlist[x]+li[x]
            ch[strlist[x]]=1
        else:
            strlist[x]=strlist[x]+li[x]
            k=1
    if k:
        cnt-=1
print(cnt)