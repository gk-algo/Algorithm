n,t=map(int,input().split())
orgin=[]
for _ in range(n):
    orgin.append(list(map(int,input().split())))

def multiple(m1,m2):
    res=[[0 for _ in range(n)] for _ in range(n)]
    for t in range(n):
        for x in range(n):
            for y in range(n):
                res[t][x]+=m1[t][y]*m2[y][x]
            res[t][x]=res[t][x]%1000
    return res

def bin(t,orgin):
    if t==1:
        return orgin
    elif t==2:
        return multiple(orgin,orgin)
    else:
        tmp=bin(t//2,orgin)
        if t%2==0:
            return multiple(tmp,tmp)
        else:
            return multiple(multiple(tmp,tmp),orgin)

res=bin(t,orgin)
for x in res:
    for y in x:
        print(y%1000, end=' ')
    print()