s=input()
n=len(s)
acount=0
m=999999999999999999999999
for x in range(n):
    if s[x]=='a':
        acount+=1
for i in range(n):
    bcnt=0
    plus=1
    while plus<=acount:
        if s[(i+plus)%n]=='b':
            bcnt+=1
        plus+=1
    m=min(bcnt,m)
print(m)