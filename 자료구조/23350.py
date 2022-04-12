#우선 순위 숫자가 높은게 먼저 적재, 낮은 건 나중에 적재
#우선순위가 같으면 무게 무거운 것 먼저 적재. 
import heapq
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
def cal(stack,l,std):
    global cost
    next=[]
    for x in l:
        if x[0]==std:
            priority[std]-=1
            if stack:
                cnt=0
                y=len(stack)-1
                while(stack[y][1]<x[1] and y>=0 and stack[y][0]==std):
                    tmp.append(stack[y])
                    cost+=stack[y][1]
                    cnt+=1
                    y-=1
                for _ in range(cnt):
                    stack.pop()
                stack.append([x[0],x[1]])
                cost+=x[1]
                while tmp:
                    q=tmp.pop()
                    cost+=q[1]
                    stack.append(q)
            else:
                stack.append([x[0],x[1]])
                cost+=x[1]
            if priority[std]==0 and priorityarr:
                std=-heapq.heappop(priorityarr)
        else:
            cost+=x[1]
            next.append(x)
    if next:
        cal(stack,next,std)
l=[]
priority=[0 for _ in range(101)] #가치를 가진 물건 개수
priorityarr=[] #가치 높은 순으로 담은 최대 힙
n,m=map(int, input().split())
for _ in range(n):
    a,b=map(int,input().split())
    priority[a]+=1
    l.append([a,b])
    if -a not in priorityarr: #힙에 없다면 힙에 추가함
        heapq.heappush(priorityarr,-a)
cost=0
std=-heapq.heappop(priorityarr) #제일 큰 가치
tmp=[]
stack=[]
cal(stack,l,std)
print(cost)