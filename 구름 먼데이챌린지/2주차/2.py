n=int(input())
s=list(input())
count=0
start=0
while start<n:
    prog=start+1
    while prog<n:
        if s[prog]==s[start]:
            prog+=1
        else:
            start=prog
            count+=1
            break
    if prog==n:
        count+=1
        break
print(count)