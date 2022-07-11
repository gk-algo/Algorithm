import sys
input=sys.stdin.readline
n=int(input())
numcase=[[0 for _ in range(10)] for _ in range(n)]
numcase[0]=[0,1,1,1,1,1,1,1,1,1]
for x in range(1,n):
        numcase[x][0]=numcase[x-1][1]
        numcase[x][9]=numcase[x-1][8]
        for y in range(1,9):
            numcase[x][y]=numcase[x-1][y+1]+numcase[x-1][y-1]
print(sum(numcase[-1])%1000000000)