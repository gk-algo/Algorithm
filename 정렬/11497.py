l=[2,4,5,7,9]
arr=[]
stack=[]
m=0
for x in range(len(l)):
    if x%2==0:
        arr.append(l[x])
for x in range(len(l)):
    if x%2==1:
        stack.append(l[x])
while stack:
    arr.append(stack.pop())
for x in range(len(arr)-1):
    m=max(m,abs(arr[x]-arr[x+1]))
print(m)