n=int(input())
for _ in range(n):
    stack=[]
    inp=list(input())
    for x in inp:
        if not stack:
            stack.append(x)
        else:
            pop=stack.pop()
            if pop==x or (pop==")" and x=="("):
                stack.append(pop)
                stack.append(x)
    if not stack:
        print("YES")
    else:
        print("NO")