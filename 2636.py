import sys
from collections import deque

read = sys.stdin.readline

m,n = map(int,read().split())

graph = [list(map(int,read().split())) for _ in range(m)]
answer = []
visited = [[0] * n for _ in range(m)]
queue = deque()


dx = [1,-1,0,0]
dy = [0,0,-1,1]

def check_zero(a,b):

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] == 0:
                return True

    return False



def bfs(a,b):
    visited[a][b] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n :
                if graph[nx][ny] == 1 and visited[nx][ny] == 0 and check_zero(nx,ny):
                    visited[nx][ny] = 1
                    queue.append((nx,ny))

    print(visited)
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 1 and graph[i][j] == 1:
                graph[i][j] = 0

    tmp = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                tmp += 1
    answer.append(tmp)

    return



for i in range(m):
    for j in range(n):
        if check_zero(i,j) == True:
            queue.append((i,j))

cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
            cnt += 1

print(cnt)
print(answer[-2])


[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
 [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
 [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]