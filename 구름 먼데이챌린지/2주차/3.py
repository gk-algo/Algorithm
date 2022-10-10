n,k=map(int,input().split())
출석부=[]
for _ in range(n):
    name, height=map(str,input().split())
    height=float(height)
    출석부.append((name,height))
출석부.sort(key=lambda x:x[1])
출석부.sort(key=lambda x:x[0])
resultName=출석부[k-1][0]
resultHeight=round(출석부[k-1][1],2)
print(resultName,format(resultHeight,".2f"))