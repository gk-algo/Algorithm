import sys
input=sys.stdin.readline
n,p=map(int,input().split())
stack=[[] for _ in range(p+1)]
cnt=0
for _ in range(n):
    a,b=map(int,input().split())
    if stack[a]:
        if stack[a][-1]>b:
            x=0
            while stack[a] and stack[a][-1]>=b:
                x=stack[a].pop()
                cnt+=1
            if x==b:
                cnt-=1
                stack[a].append(b)
            else:
                cnt+=1
                stack[a].append(b)
        elif stack[a][-1]==b:
            continue
        else:
            stack[a].append(b)
            cnt+=1
    else:
        stack[a].append(b)
        cnt+=1
print(cnt)