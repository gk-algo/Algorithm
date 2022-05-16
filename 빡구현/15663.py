from itertools import permutations
n,m=map(int,input().split())
num=list(map(int,input().split()))
num=(list(set(permutations(num,m))))
num.sort()
for x in num:
    for t in x:
        print(t,end=" ")
    print()