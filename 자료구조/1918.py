def priority(x):
    if x=='+' or x=='-':
        return 1
    elif x=='*' or x=='/':
        return 2
    else:
        return 0

l=list(input())
stack=[]
pp=[]
p=0

for x in l:
    if not (x=='+' or x=='-' or x=='*' or x=='/' or x=='(' or x==')'):
        print(x, end='')
    else:
        if x==')':
            while stack and stack[-1]!='(':
                print(stack.pop(),end='')
            if stack:
                stack.pop()
            if pp:
                p=pp.pop()
            else:
                p=0
        elif x=='(':
            pp.append(p)
            p=0
            stack.append(x)
        elif priority(x)>p:
            stack.append(x)
            p=priority(x)
        else:
            while stack and priority(stack[-1])>=priority(x):
                q=stack.pop()
                print(q,end='') 
            stack.append(x)
            p=priority(x)
while stack:
    print(stack.pop(), end='')
            
        