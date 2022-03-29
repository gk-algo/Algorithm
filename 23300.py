#https://www.acmicpc.net/problem/23300
def doforward(now):
    if forward:
        backward.append(now)
        now=forward.pop()
    return now

def dobackward(now):
    if backward:
        forward.append(now)
        now=backward.pop()
    return now

def connect(where,now):
    if now=='first':
        now=where
    else:
        backward.append(now)
        now=where
    return now

def zip():
    stack=[]
    while backward:
        if not stack:
            stack.append(backward.pop())
        else:
            tmp=backward.pop()
            if stack[-1]!=tmp:
                stack.append(tmp)
    while stack:
        backward.append(stack.pop())
    return backward

backward=[]
forward=[]
n,q=map(int,input().split())
now='first'
for _ in range(q):
    i=list(map(str,input().split()))
    if len(i)==1:
        if i[0]=='B':
            now=dobackward(now)
        elif i[0]=='F':
            now=doforward(now)
        elif i[0]=='C':
            zip()
    else:
        now=connect(i[1],now)
        forward=[]
print(now)
if backward:
    backward.reverse()
    print(' '.join(backward))
else:
    print(-1)
if forward:
    forward.reverse()
    print(' '.join(forward))
else:
    print(-1)
