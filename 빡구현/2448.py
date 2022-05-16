def shape(n,x,y):

    if n==3:
            result[x][y]="*"
            result[x+1][y-1]=result[x+1][y+1]="*"
            for t in range(-2,3):
                result[x+2][y+t]="*"
    else:
        shape(n//2,x,y)
        shape(n//2,x+n//2,y-n//2)
        shape(n//2,x+n//2,y+n//2)

n=int(input())
result = [[" "]*2*n for x in range(n)]
shape(n,0,n-1)
for x in result:
    print("".join(x))