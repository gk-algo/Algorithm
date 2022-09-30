import sys
sys.setrecursionlimit(10**6)
global cnt
N, M, R = map(int, input().split())

visit = [0 for _ in range(N+1)]
arr = [[]for _ in range(N+1)]
ans = [0 for _ in range(N)]
cnt=1

def DFS(start,cnt):
    if visit[start] != 1:
        ans[start-1] = cnt
        visit[start] = 1
    for i in arr[start]:
        if visit[i] != 1:
            cnt+=1
            DFS(i,cnt)

for i in range(M):
    a, b = map(int, input().split())

    arr[a].extend([b])
    arr[a].sort()
    arr[b].extend([a])
    arr[b].sort()

DFS(R,cnt)

for i in ans:
    print(i)