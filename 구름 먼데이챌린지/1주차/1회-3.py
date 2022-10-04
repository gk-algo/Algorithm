# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
numbers=list(map(int,input().split()))
numbers.sort()
distance=numbers[3]-numbers[0]+numbers[2]-numbers[1]
print(distance)