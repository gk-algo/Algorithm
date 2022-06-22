n=list(input())
stack=[]
for x in n:
    if x==')':
        if stack:
            if stack.pop()!='(':
                print("유효하지 않음")
                exit()
        else:
            print("유효하지 않음")
            exit()
    else:
        stack.append(x)
if stack:
    print("유효하지 않음")
    exit()
else:
    print("유효함")

