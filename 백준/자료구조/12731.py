import heapq
from collections import deque
from tracemalloc import start
def f(heap,count,save,op_save):
    now_a=heapq.heappop(heap)
    start_hour,start_minutes=now_a[0].split(":")
    start_hour=int(start_hour)
    start_minutes=int(start_minutes)
    if save:
        if start_hour<save[0][0]:
            count+=1
        elif start_hour==save[0][0]:
            if start_minutes<save[0][1]:
                count+=1
            else:
                heapq.heappop(save)
        else:
            heapq.heappop(save)
    else:
        count+=1
    hour, minutes=now_a[1].split(':')
    if int(minutes)+t<60:
        minutes=int(minutes)+t
    else:
        hour=int(hour)+1
        minutes=int(minutes)-60
    heapq.heappush(op_save,[int(hour),int(minutes)])
    return heap,count,save,op_save
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
                b,bcount,bsave,asave=f(b,bcount,bsave,asave)
                a,acount,asave,bsave=f(a,acount,asave,bsave)
            else:
                a,acount,asave,bsave=f(a,acount,asave,bsave)
                b,bcount,bsave,asave=f(b,bcount,bsave,asave)
        elif a:
            a,acount,asave,bsave=f(a,acount,asave,bsave)
        elif b:
            b,bcount,bsave,asave=f(b,bcount,bsave,asave)   
    print("Case #",end='')
    print(v+1,end='')
    print(": ",end='')
    print(acount,bcount)


