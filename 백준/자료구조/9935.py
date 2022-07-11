s=input()
bomb=input()
com=len(bomb)
stack=[]
for x in s:
    stack.append(x)
    if x==bomb[-1] and ''.join(stack[-com:])==bomb:
        del stack[-com:]
ans=''.join(stack)
if ans=='':
    print("FRULA")
else:
    print(ans)