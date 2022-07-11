
s=input()
l=[]
ret=[]
start=0
for x in range(len(s)):
    if s[x]==':':
        l.append(s[start:x])
        start=x+1
l.append(s[start:])
for x in l:
    if len(x)==4:
        ret.append(x)
    elif len(x)==3:
        ret.append('0'+x)
    elif len(x)==2:
        ret.append('00'+x)
    elif len(x)==1:
        ret.append('000'+x)
    else:
        ret.append('')
tmp=[]
for x in range(len(ret)-1):
    if ret[x]=='':
        t=9
        if ret[x+1]=="":
            t=10
        for i in range(t-len(ret)):
            tmp.append('0000')
        break
if ret[x]=='':
    if ret[x+1]=='':
        ret=ret[:x]+tmp+ret[x+2:]
    else:
        ret=ret[:x]+tmp+ret[x+1:]
for x in range(len(ret)):
    if x!=7:
        print(ret[x],end=":")
    else:
        print(ret[x])