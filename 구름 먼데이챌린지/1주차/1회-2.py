# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n,s=input().split()
n=int(n)
count=0
for _ in range(n):
	name=input()
	if s in name:
		count+=1
print(count)