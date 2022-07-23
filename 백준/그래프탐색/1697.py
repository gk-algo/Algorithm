from collections import deque

def bfs(arr, n, k):
    q = deque()
    q.append(n)
    while q:
        i=q.popleft()
        if i==k:
            return arr[i]
        for j in (i+1, i-1, 2*i):
            if (0 <= j < 100001) and arr[j] == 0:
                arr[j] = arr[i] + 1
                q.append(j)

n,k= map(int, input().split())
li = [0] * 100001
print(bfs(li, n, k))