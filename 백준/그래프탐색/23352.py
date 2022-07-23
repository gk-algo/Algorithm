from collections import deque


def bfs(x, y):
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q.append((x, y))
    vis[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if 0 <= X < m and 0 <= Y < n and vis[X][Y] == 0:
                vis[X][Y] = vis[x][y]+1
                q.append((X, Y))
    MAX = 0
    for x in range(n):
        for y in range(m):
            if vis[x][y] > MAX:
                MAX = vis[x][y]
                rx = x
                ry = y
    return [MAX, rx, ry]


n, m = map(int, input().split())
M = []
maxcnt = 0
for _ in range(n):
    M.append(list(map(int, input().split())))
for x in range(n):
    for y in range(m):
        vis = [[0 for _ in range(m)] for _ in range(n)]
        if M[x][y] != 0:
            start = M[x][y]
            tmp = bfs(x, y)
            for x in vis:
                print(x)
            print()
            if tmp[0] > maxcnt:
                maxcnt = tmp[0]
                end = M[tmp[1]][tmp[2]]
print(start, end)
