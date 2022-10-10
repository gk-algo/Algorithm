def boom(x,y):
    metrix[x][y]+=1
    addX=[-1,1,0,0]
    addY=[0,0,-1,1]
    for i in range(4):
        afterX=x+addX[i]
        afterY=y+addY[i]
        if  0<afterX<=n and 0<afterY<=n:
            metrix[afterX][afterY]+=1
n,k=map(int,input().split())
metrix=[[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    x,y=map(int,input().split())
    boom(x,y)
result=0
for x in metrix:
	for y in x:
		result+=y
print(result)