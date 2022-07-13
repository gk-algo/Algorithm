s=input()
cur=0
stack=[]
for x in range(len(s)):
    if s[x]=="(":
        if x!=0:
            mul=int(s[x-1])
        stack.append((cur-1,mul))
        cur=0
    elif s[x]==")":
        c,m=stack.pop()
        cur=(m*cur)+c
    else:
        cur+=1
print(cur)
