import sys
from collections import deque

read = sys.stdin.readline

n = int(read())

graph = [list(map(str,read().strip())) for _ in range(n)]
queue = deque()

queue.append((0,0))

visited = [[-1]*n for _ in range(n)]
visited[0][0] = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]


while queue:
    print(visited)
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == -1:
                if graph[nx][ny] == '1':
                    queue.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]
                elif graph[nx][ny] == '0':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))


print(visited[n-1][n-1])