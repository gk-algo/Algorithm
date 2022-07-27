import heapq
n,m=map(int,input().split())
# 24*n시간 후 시작
time=24*n
# m과목
a=list(map(int,input().split()))
b=list(map(int,input().split()))
결과=0
힙=[]
for x in range(m):
    heapq.heappush(힙, [-b[x],a[x]])
while 힙:
    힙에서뽑은거=heapq.heappop(힙)
    단위,점수=-힙에서뽑은거[0],힙에서뽑은거[1]
    while 단위+점수<=100:
        if time>0:
            점수+=단위
            time-=1
        else:
            break
    if 점수==100:
        결과+=100
    else:
        heapq.heappush(힙,[-(100-점수),점수])
    if time==0:
        break
while 힙:
    필요없는거, 점수=heapq.heappop(힙)
    결과+=점수
print(결과)