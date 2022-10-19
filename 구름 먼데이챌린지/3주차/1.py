# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10**6)
def BinarySearch(start,end, target):
	if start>end:
		return False
	mid=(start+end)//2
	if people[mid]==target:
		return True
	elif people[mid]>target:
		return BinarySearch(start,mid-1,target)
	elif people[mid]<target:
		return BinarySearch(mid+1,end, target)

n=int(input())
people=list(map(int,input().split()))
people.sort()
result=0
for x in people:
    if not BinarySearch(0,len(people)-1,-x):
        result+=x
print(result)