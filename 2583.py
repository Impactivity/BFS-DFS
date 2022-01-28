import sys
from collections import deque

read = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n,k = map(int, read().split())
rect = [list(map(int,read().split())) for _ in range(k)]
graph = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]

for rec in rect:
    for j in range(rec[0], rec[2]):
        for k in range(rec[1],rec[3]):
            graph[k][j] = 1


def bfs(x,y):

    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    area = 1

    while queue:
        a,b = queue.popleft()

        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    area += 1

    answer.append(area)
    return

cnt = 0
answer = []

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 0:
            bfs(i,j)
            cnt += 1

print(cnt)
answer.sort()
print(*answer)