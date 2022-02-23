# -*- coding: utf-8 -*-
from collections import deque

#토마토의 위치를 x,y 좌표로 생각하여 graph로 구성.
#bfs를 이용하여 값이 1인 위치부터 탐색을 한다.
#탐색할떄마다 + 1 씩 해주면서 이동 한다.

m, n = map( int, input().split())

graph =[list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

queue = deque()


def bfs():

    while queue:
        x,y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 :
                continue

            #안익은 토마토의 위치값은 0이기 때문에 i,j 위치부터 0을 찾아감.
            if graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

    return

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 :
            queue.append((i,j))

bfs()
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
    answer = max(answer,max(graph[i]))

print(answer-1)
