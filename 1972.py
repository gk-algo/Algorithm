#https://www.acmicpc.net/problem/1972

while (1):
    l=input()
    if l=='*':
        break
    check=1
    for x  in range(1,len(l)):
        result=[]
        for y in range(len(l)):
            if y+x<len(l):
                result.append(l[y]+l[x+y])
        for t in range(len(result)):
            if result[t] in result[t+1:]:
                check=0
    if check:
        print(l+" is surprising.")
    else:
        print(l+" is NOT surprising.")