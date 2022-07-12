l=input()
stack=[]
res=0
tmp=1
for x in range(len(l)):
    if l[x]=="(":
        tmp*=2
        stack.append(l[x])
    elif l[x]=="[":
        tmp*=3
        stack.append(l[x])
    elif l[x]==")":
        if stack and stack.pop()=='(':
            if l[x-1]=='(':
                res+=tmp
            tmp=tmp//2
        else:
            print("0")
            exit()
    elif l[x]=="]":
        if stack and stack.pop()=='[':
            if l[x-1]=='[':
                res+=tmp
            tmp=tmp//3
        else:
            print("0")
            exit()
if stack:
    print("0")
else:
    print(res)
            
