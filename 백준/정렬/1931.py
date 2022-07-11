n=int(input())
li=[]
for _ in range(n):
    a,b=map(int, input().split())
    li.append([a,b])
cnt=1
li.sort(key=lambda x:x[0])
li.sort(key=lambda x:x[1])
time=li[0][1]
for i in range(1,n):
    if li[i][0]>=time:
        cnt+=1
        time=li[i][1]
print(cnt)