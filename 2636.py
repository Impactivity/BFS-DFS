import sys
from collections import deque

read = sys.stdin.readline

m,n = map(int,read().split())

graph = [list(map(int,read().split())) for _ in range(m)]
answer = []


dx = [1,-1,0,0]
dy = [0,0,-1,1]


def bfs():
    queue = deque()
    visited[0][0] = 1
    queue.append((0,0))
    cnt = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n :
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                    elif graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        visited[nx][ny] = 1
                        cnt += 1

    answer.append(cnt)
    return cnt

time = 0
while 1 :
    time += 1

    visited = [[0] * n for _ in range(m)]
    cnt = bfs()
    if cnt == 0:
        break

print(time-1)
print(answer[-2])
