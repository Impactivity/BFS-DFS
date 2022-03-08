import sys
from collections import deque


read = sys.stdin.readline

m,n = map(int,read().split()) #가로m , 세로 n

graph = [ list(map(str,read().strip())) for _ in range(n) ]
visited = [[-1] * m for _ in range(n)]

queue = deque()
queue.append((0,0))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited[0][0] = 0

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == -1:
                if graph[nx][ny] == '1':
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif graph[nx][ny] == '0':
                    queue.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]

print(visited[n-1][m-1])
