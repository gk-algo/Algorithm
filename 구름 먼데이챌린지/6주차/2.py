def change(alpha, number):
    squre=number**2
    ascii=ord(alpha)-97
    ascii=(ascii+squre)%26+97
    return chr(ascii)

n=int(input())
s=input()
answer=""
for x in range(len(s)):
    if x%2==0:
        answer+=change(s[x],int(s[x+1]))
print(answer)