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
                    if graph[nx][ny] == 0: #공기 접촉부분을 탐색하여 치즈의 가장자리를 알게한다.
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                    elif graph[nx][ny] == 1: #공기와 접촉한 가장자리부분을 만나게 될경우 append하지 않고
                        #append할 경우 치즈 안쪽 공기부분도 녹기 때문이다.
                        #녹은 상태로 처리해준다. 이때 cnt변수에 담아 치즈가 녹은 부분을 카운팅 한다.
                        graph[nx][ny] = 0
                        visited[nx][ny] = 1
                        cnt += 1

    answer.append(cnt)
    print(cnt)
    return cnt

time = 0

# 치즈가 모두 녹을 때까지 while문을 이용하여 처리해주고
# bfs가 돌때마다 한시간씩 증가하는 것으로 구현
while 1 :
    time += 1

    visited = [[0] * n for _ in range(m)]
    cnt = bfs()
    if cnt == 0:
        break

print(time-1)
print(answer[-2]) # 치즈가 모두 녹기 한 시간 전 일때 치즈갯수