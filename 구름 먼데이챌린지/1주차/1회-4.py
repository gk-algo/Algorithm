# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math
def isPrime(number):
    x=2
    if number==1:
        return False
    while (x<=math.sqrt(number)):
        if (number%x)==0:
            return False
        x+=1
    return True
n=int(input())
numbers=list(map(int,input().split()))
SUM=0
for x in range(len(numbers)):
    if isPrime(x+1):
            SUM+=numbers[x]
print(SUM)