from collections import deque
import heapq
def change(d, c):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d
def start():
    direction = 1  
    time = 1  
    y, x = 0, 0  
    visited = deque([[y, x]])  
    matrix[y][x] = 2
    if times:
        ftime=heapq.heappop(times)
    else:
        ftime=[]
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < n and 0 <= x < n and matrix[y][x] != 2:
            if not matrix[y][x] == 1:  
                temp_y, temp_x = visited.popleft()
                matrix[temp_y][temp_x] = 0
            matrix[y][x] = 2
            visited.append([y, x])
            if ftime:
                if time==ftime[0]:
                    direction=change(direction,ftime[1])
                    if times:
                        ftime=heapq.heappop(times)
            time += 1
        else: 
            return time
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
n = int(input())
k= int(input())
matrix = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1 
l = int(input())
times=[]
for i in range(l):
    x,c = input().split()
    heapq.heappush(times,[int(x),c])
print(start())
