s=input()
i=0
cnt=0
length=len(s)
for x in range(length):
    j=length-1
    ck=0
    if s[x]==s[j]:
        i=x
        while s[i]==s[j] and i<j:
            i+=1
            j-=1
        if i>=j:
            print(x+length)
            exit()