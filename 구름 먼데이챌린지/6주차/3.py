def encryption(plain,key):
    newKey=getKey(plain,key)
    ret=""
    for x in range(len(plain)):
        ret+=change(plain[x],newKey[x])
    return ret

def decryption(encrp, key):
    newKey=getKey(encrp,key)
    ret=""
    for x in range(len(encrp)):
        ret+=undo(encrp[x],newKey[x])
    return ret

def getKey(msgString, key):
    index=0
    ret=key
    while (len(msgString)>len(ret)):
        ret=ret+key[index]
        index=(index+1)%len(key)
    return ret

def change(msg, token):
    ascii=ord(msg)
    ascii_token=ord(token)
    if(65<=ascii<=90):
        ascii=ascii-65
        ascii=(ascii+ascii_token)%26+65
    elif (97<=ascii<=122):
        ascii=ascii-97
        ascii=(ascii+ascii_token)%26+97
    return chr(ascii)

def undo(msg, token):
    ascii=ord(msg)
    ascii_token=ord(token)
    if(65<=ascii<=90):
        ascii=ascii-65
        ascii=(ascii-ascii_token)
        if ascii<=0:
            ascii+=26
        ascii=ascii%26+65
    elif (97<=ascii<=122):
        ascii=ascii-97
        ascii=(ascii-ascii_token)
        if ascii<=0:
            ascii+=26
        ascii=ascii%26+97
    return chr(ascii)

T=int(input())
for _ in range(T):
    S=input()
    method,Key=map(str,input().split())
    if(method=="E"):
        print(encryption(S, Key))
    else:
        print(decryption(S,Key))
