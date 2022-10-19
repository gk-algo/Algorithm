def changeNumber(number, repeat):
    if number==1:
        if repeat%5==1:
            return '1'
        elif repeat%5==2:
            return '.'
        elif repeat%5==3:
            return ','
        elif repeat%5==4:
            return '?'
        else:
            return '!'
    elif number==2:
        if repeat%4==1:
            return '1'
        elif repeat%4==2:
            return 'A'
        elif repeat%4==3 :
            return 'B'
        else:
            return 'C'
    elif number==3:
        if repeat%4==1:
            return '3'
        if repeat%4==2:
            return 'D'
        elif repeat%4==3:
            return 'E'
        else:
            return 'F'
    elif number==4:
        if repeat%4==1:
            return '4'
        elif repeat%4==2:
            return 'G'
        elif repeat%4==3:
            return 'H'
        else:
            return 'I'
    elif number==5:
        if repeat%4==1:
            return '5'
        elif repeat%4==2:
            return 'J'
        elif repeat%4==3:
            return 'K'
        else: 
            return 'L'
    elif number==6:
        if repeat%4==1:
            return '6'
        elif repeat%4==2:
            return 'M'
        elif repeat%4==3:
            return 'N'
        else:
            return 'O'
    elif number==7:
        if repeat%5==1:
            return '7'
        elif repeat%5==2:
            return 'P'
        elif repeat%5==3:
            return 'Q'
        elif repeat%5==4:
            return 'R'
        else:
            return 'S'
    elif number==8:
        if repeat%4==1:
            return '8'
        elif repeat%4==2:
            return 'T'
        elif repeat%4==3:
            return 'U'
        else:
            return 'V'
    elif number==9:
        if repeat%5==1:
            return '9'
        elif repeat%5==2:
            return 'W'
        elif repeat%5==3:
            return 'X'
        elif repeat%5==4:
            return 'Y'
        else:
            return 'Z'
n=int(input())
numbers=input()
answer=""
index=0
current_number=numbers[index]
repeat=0
while index<n:
    if current_number==numbers[index]:
        index+=1
        repeat+=1
    else:
        answer=answer+changeNumber(int(current_number),repeat)
        if index<n:
            current_number=numbers[index]
            repeat=0
answer=answer+changeNumber(int(current_number),repeat)
print(answer)