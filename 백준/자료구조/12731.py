import heapq
n=int(input())
for v in range(n):
    a=[]
    b=[]
    t=int(input())
    na,nb=map(int,input().split())
    for _ in range(na):
        x=list(map(str,input().split()))
        heapq.heappush(a,x)
    for _ in range(nb):
        x=list(map(str,input().split()))
        heapq.heappush(b,x)
    while a or b:
        if a:
            now_a=heapq.heappop(a)
            if len(now_a)==2:
                na-=1
                acount+=1
            else:
                while a and len(a[0])==1:
                    now_a=heapq.heappop(a)
            hour, minutes=now_a[1].split(':')
            if int(minutes)+t<60:
                minutes=int(minutes)+t
            else:
                hour=str(int(hour)+1)
                minutes=int(minutes)-60
            if minutes<10:
                minutes=str('0'+str(minutes))
            minutes=str(minutes)
            heapq.heappush(b,[hour+":"+minutes])
        if b:
            now_b=heapq.heappop(b)
            if len(now_b)==2:
                nb-=1
                bcount+=1
            else:
                while b and len(b[0])==1:
                    now_b=heapq.heappop(b)
            hour, minutes=now_b[1].split(':')
            if int(minutes)+t<60:
                minutes=int(minutes)+t
            else:
                hour=str(int(hour)+1)
                minutes=int(minutes)-60
            if minutes<10:
                minutes=str('0'+str(minutes))
            minutes=str(minutes)
            heapq.heappush(a,[hour+":"+minutes])
    print("Case #",end='')
    print(v+1,end='')
    print(": ",end='')
    print(acount,bcount)
        
    
    