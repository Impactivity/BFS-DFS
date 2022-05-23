import sys
from collections import deque

read = sys.stdin.readline

n,m = map(int, read().split())

graph = [ list(map(int,read().split())) for _ in range(n)]
melted = [ [0]*m for _ in range(n)]
Time = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(queue):

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 0:
                    melted[x][y] += 1
    return

# 빙하 녹음 처리
def melt():
    for i in range(n):
        for j in range(m):
            if melted[i][j] != 0:
                graph[i][j] -= melted[i][j]
                if graph[i][j] < 0:
                    graph[i][j] = 0

    return


# 탐색하면서 주위의 빙하갯수를 melted에 저장
while True:
    visited = [[0] * m for _ in range(n)]
    melted = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == 0:
                queue = deque()
                queue.append((i,j))
                visited[i][j] = 1
                bfs(queue)
                cnt += 1

    if cnt >=  2:
        print(Time)
        break

    if cnt == 0:
        print(0)
        break

    Time += 1
    melt()

