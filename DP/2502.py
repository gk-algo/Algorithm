import sys
sys.setrecursionlimit(100000)
d,k=map(int,input().split())
d1,d2=0,0
def dp(n):
    global d1
    global d2
    if n==1:
        d1+=1
        return 
    if n==2:
        d2+=1
        return 
    else:
        dp(n-1)
        dp(n-2)
dp(d)
for x in range(k//d1):
    for y in range(x,k//d2):
        if x*d1+y*d2==k:
            print(x)
            print(y)
            exit()