t=int(input())
for _ in range(t):
    stack=[]
    li=[]
    cnt=0
    x1=[1,-1,0,0]
    x2=[0,0,1,-1]
    m,n,k=map(int, input().split())
    space=[[0]*n for x in range(m)]
    check=[[0]*n for x in range(m)]
    for _ in range(k):
        a,b=map(int, input().split())
        space[a][b]=1
        li.append([a,b])
    for x in range(m):
        for y in range(n):
            if space[x][y]==1 and check[x][y]==0:
                cnt+=1
                check[x][y]=1
                stack.append([x,y])
                while stack:
                    a,b=stack.pop()
                    check[a][b]=1
                    for i in range(4):
                        A=a+x1[i]
                        B=b+x2[i]
                        if (0<=A<m) and (0<=B<n):
                            if space[A][B]==1 and check[A][B]==0:
                                stack.append([A,B])
    print(cnt)