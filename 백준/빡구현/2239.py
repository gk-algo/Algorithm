def 세로체크(col):
    ck=[0 for _ in range(9)]
    for x in range(9):
        ck[s[x][col]]=1
def 가로체크(row):
    ck=[0 for _ in range(9)]
    for x in range(9):
        ck[s[row][x]]=1


s=[]
for _ in range(9):
    l=list(input())
    s.append(l)
print(s)