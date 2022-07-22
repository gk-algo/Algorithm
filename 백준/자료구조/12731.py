import heapq
from collections import deque
from tracemalloc import start
def function_a(a,acount,asave,bsave):
    now_a=heapq.heappop(a)
    start_hour,start_minutes=now_a[0].split(":")
    start_hour=int(start_hour)
    start_minutes=int(start_minutes)
    if asave:
        if start_hour<asave[0][0]:
            acount+=1
        elif start_hour==asave[0][0]:
            if start_minutes<asave[0][1]:
                acount+=1
            else:
                heapq.heappop(asave)
        else:
            heapq.heappop(asave)
    else:
        acount+=1
    hour, minutes=now_a[1].split(':')
    if int(minutes)+t<60:
        minutes=int(minutes)+t
    else:
        hour=int(hour)+1
        minutes=int(minutes)-60
    heapq.heappush(bsave,[int(hour),int(minutes)])
    return a,acount,asave,bsave
def function_b(b,bcount,bsave,asave):
    now_b=heapq.heappop(b)
    start_hour,start_minutes=now_b[0].split(':')
    start_hour=int(start_hour)
    start_minutes=int(start_minutes)
    if bsave:
        if start_hour<bsave[0][0]:
            bcount+=1
        elif start_hour==bsave[0][0]:
            if start_minutes<bsave[0][1]:
                bcount+=1
            else:
                heapq.heappop(bsave)
        else:
            heapq.heappop(bsave)
    else:
        bcount+=1
    hour, minutes=now_b[1].split(':')
    if int(minutes)+t<60:
        minutes=int(minutes)+t
    else:
        hour=int(hour)+1
        minutes=int(minutes)-60
    heapq.heappush(asave,[int(hour),int(minutes)])
    return b,bcount,bsave,asave
n=int(input())
for v in range(n):
    a=[]
    b=[]
    asave=[]
    bsave=[]
    acount=0
    bcount=0
    t=int(input())
    na,nb=map(int,input().split())
    for _ in range(na):
        x=list(map(str,input().split()))
        heapq.heappush(a,x)
    for _ in range(nb):
        x=list(map(str,input().split()))
        heapq.heappush(b,x)
    while a or b:
        if a and b:
            if int("".join(list(a[0][0].split(':'))))>int("".join(list(b[0][0].split(':')))):
                b,bcount,bsave,asave=function_b(b,bcount,bsave,asave)
                a,acount,asave,bsave=function_a(a,acount,asave,bsave)
            else:
                a,acount,asave,bsave=function_a(a,acount,asave,bsave)
                b,bcount,bsave,asave=function_b(b,bcount,bsave,asave)
        elif a:
            a,acount,asave,bsave=function_a(a,acount,asave,bsave)
        elif b:
            b,bcount,bsave,asave=function_b(b,bcount,bsave,asave)   
    print("Case #",end='')
    print(v+1,end='')
    print(": ",end='')
    print(acount,bcount)


