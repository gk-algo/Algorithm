from itertools import combinations
s=list(input())
stack=[]
bracket=[]
res=[]
for x in range(len(s)):
    if s[x]=='(':
        stack.append(x)
    elif s[x]==')':
        start=stack.pop()
        bracket.append((start,x))
for x in range(1,len(bracket)+1):
    for i in list(combinations(bracket,x)):
        ans=s[:]
        for j in i:
            ans[j[0]]=''
            ans[j[1]]=''
        res.append(''.join(s for s in ans))
res=list(set(res))
res.sort()
for x in res:
    print(x)
    