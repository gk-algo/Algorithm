def mise():
    miselist=[]
    for x in range(r):
        for y in range(c):
            if m[x][y]!=0 and m[x][y]!=-1:
                miselist.append([x,y])
    tmp=[[0 for _ in range(c)] for _ in range(r)]
    for t in miselist:
        x=t[0]
        y=t[1]
        a=[-1,1,0,0]
        b=[0,0,-1,1]
        cnt=0
        for i in range(4):
            X=x+a[i]
            Y=y+b[i]
            if 0<=X<r and 0<=Y<c and m[X][Y]!=-1:
                tmp[X][Y]+=m[x][y]//5
                cnt+=1
        m[x][y]=m[x][y]-(m[x][y]//5)*cnt
    for x in range(r):
        for y in range(c):
            if m[x][y]!=-1:
                m[x][y]=m[x][y]+tmp[x][y]

def wind():
    windlist=[]
    for x in range(r):
        for y in range(c):
            if m[x][y]==-1:
                windlist.append([x,y])
    wx1,wy1=windlist[0][0],windlist[0][1]
    wx2,wy2=windlist[1][0],windlist[1][1]
    for t in range(1,wx1):
        m[wx1-t][0]=m[wx1-t-1][0]
    for t in range(0,c-1):
        m[0][t]=m[0][t+1]
    for t in range(0,wx1):
        m[t][-1]=m[t+1][-1]
    for t in range(c-2,0,-1):
        m[wx1][t+1]=m[wx1][t]
    m[wx1][1]=0
    for t in range(wx2+2,r):
        m[t-1][wy2]=m[t][wy2]
    for t in range(1,c):
        m[-1][t-1] = m[-1][t]
    for t in range(r-2,wx2-1,-1):
        m[t+1][-1]=m[t][-1]
    for t in range(c-2,0,-1):
        m[wx2][t+1] = m[wx2][t]
    m[wx2][1]=0
r,c,t=map(int,input().split())
m=[]
for _ in range(r):
    m.append(list(map(int,input().split())))

for x in range(t):
    mise()
    wind()
SUM=0
for x in range(r):
    SUM+=sum(m[x])
print(SUM+2)