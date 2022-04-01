#https://www.acmicpc.net/problem/23349
n=int(input())
place=[]
time=dict()
maxplace=[]
name=[]
for _ in range(n):
    l=list(map(str, input().split()))
    if l[0] not in name:
        name.append(l[0])
        if time.get(l[1]) is None:
            time[l[1]]=[0 for _ in range(50001)]
        for x in range(int(l[2]),int(l[3])):
            time[l[1]][x]+=1
        if not maxplace:
            maxplace.append([l[1],1])
        else:
            placename, cnt=maxplace.pop()
            if cnt<max(time[l[1]]):
                cnt=max(time[l[1]])
                placename=l[1]
                while maxplace:
                    maxplace.pop()
            elif cnt==max(time[l[1]]):
                maxplace.append([l[1],max(time[l[1]])])
            maxplace.append([placename,cnt])
        if l[1] not in place:
            place.append(l[1])
if len(maxplace)==1:
    p,maxx=maxplace.pop()
else:
    maxplace.sort(key= lambda x:x[0])
    p,maxx=maxplace[0][0],maxplace[0][1]
print(p, end=' ')
for x in range(50001):
    if time[p][x]==maxx:
        start=x
        break
for x in range(start, 50001):
    if time[p][x]!=maxx:
        end=x
        break
print(start,end)