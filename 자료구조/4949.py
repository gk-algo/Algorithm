while 1:
    stack=[]
    inp=list(input())
    if inp[0]==".":
        break
    for x in inp:
        if x=="(" or x=="[" or x=="]" or x==")":
            if not stack:
                stack.append(x)
            else:
                pop=stack.pop()
                if pop=="(" and x!=")":
                    stack.append(pop)
                    stack.append(x)
                elif pop=="[" and x!="]" :
                    stack.append(pop)
                    stack.append(x)
                elif pop=="]":
                    stack.append(pop)
                    stack.append(x)
                elif pop==")":
                    stack.append(pop)
                    stack.append(x)
    if not stack:
        print("yes")
    else:
        print("no")