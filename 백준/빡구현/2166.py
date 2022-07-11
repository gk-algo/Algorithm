n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
l.append(l[0])
plus=0
minus=0
for x in range(n):
    plus+=l[x][0]*l[x+1][1]
    minus+=l[x][1]*l[x+1][0]
S=abs(plus-minus)/2
print(round(S,2))