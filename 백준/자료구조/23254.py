import heapq
n,m=map(int,input().split())
# 24*n시간 후 시작
time=24*n
# m과목
a=list(map(int,input().split()))
b=list(map(int,input().split()))
단위별점수=dict()
결과=0
힙=[]
for x in range(m):
    heapq.heappush(힙, [-b[x],a[x]])
while 힙:
    힙에서뽑은거=heapq.heappop(힙)
    단위,점수=-힙에서뽑은거[0],힙에서뽑은거[1]
    while 단위+점수<100:
        if time>0:
            점수+=단위
            time-=1
        else:
            break
    if 단위별점수.get(단위):
        heapq.heappush(단위별점수[단위],점수)
    else:
        단위별점수[단위]=[]
        heapq.heappush(단위별점수[단위],점수)
    if 힙:
        while 단위별점수[단위]:
            if (100-단위별점수[단위][0])>=-힙[0][0] and time>0:
                heapq.heappop(단위별점수[단위])
                결과+=100
                time-=1
            else:
                break
print(단위별점수)
for 키 in 단위별점수.keys():
    for 점수 in 단위별점수[키]:
        결과+=점수
print(결과)