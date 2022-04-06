#https://www.acmicpc.net/problem/2812
import sys
N,K = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().strip()))
result = []
rest= K
for i in range(N):
    while rest>0 and result:
        if result[len(result)-1] < nums[i]:
            result.pop()
            rest-=1
        else:
            break
    result.append(nums[i])
for x in range(N-K):
    print(result[x], end="")