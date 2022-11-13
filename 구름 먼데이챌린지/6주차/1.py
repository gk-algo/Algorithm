answer=[]
for _ in range(5):
    k=int(input())
    string=str(k)
    a=0
    for x in range(len(string)):
        if(x%2==0):
            a=a+int(string[x])
    for x in range(len(string)):
        if x%2==1 and string[x]!='0':
            a=a*int(string[x])
    answer.append(a%10)
for x in answer:
    print(x)