# https://www.acmicpc.net/problem/3055
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                X = x + dx[i]
                Y = y + dy[i]
                if 0 <= X < n and 0 <= Y < m:
                    if M[X][Y] == '.' and c[X][Y] == 0:
                        c[X][Y] = c[x][y] + 1
                        q.append([X, Y])
                    elif M[X][Y] == 'D':
                        print(c[x][y])
                        return
            qlen -= 1
        water()
    print("KAKTUS")
    return


def water():
    qlen = len(wq)
    while qlen:
        x, y = wq.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < n and 0 <= Y < m:
                if M[X][Y] == '.':
                    M[X][Y] = '*'
                    wq.append([X, Y])
        qlen -= 1


n, m = map(int, input().split())
M = [list(map(str, input())) for _ in range(n)]
c = [[0]*m for _ in range(n)]
q, wq = deque(), deque()

for x in range(n):
    for y in range(m):
        if M[x][y] == 'S':
            x1, y1 = x, y
            M[x][y] = '.'
        elif M[x][y] == '*':
            wq.append([x, y])

water()
bfs(x1, y1)
