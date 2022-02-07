import sys
from collections import deque

read = sys.stdin.readline
n,m = map(int, read().split()) #세로, 가로

graph = [list(map(str, read().strip())) for _ in range(n)]

visit = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move(i,j, dx,dy):
    c = 0
    while graph[i+dx][j+dy] != '#' and graph[i][j] != "O":
        i += dx
        j += dy
        c += 1
    return i,j,c

def bfs():

    while queue:
        rx,ry,bx,by,d = queue.popleft()
        if d > 10:
            break
        for i in range(4):
            #red 구슬의 위치
            nrx,nry,rc = move(rx,ry,dx[i],dy[i])
            nbx,nby,bc = move(bx,by,dx[i],dy[i])
            if graph[nbx][nby] != "O": # 파란 구슬이 구멍에 빠지지 않을 경우
                if graph[nrx][nry] == "O":
                    print(d)
                    return
                if nrx == nbx and nry == nby: #두 개 구슬 위치가 같을 때
                    if rc > bc: #이동한 거리를 계산해서 먼거리를 이동한 대상을 이전 위치로 옮김
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby] = True
                    queue.append([nrx,nry,nbx,nby,d+1])
    print(-1)

for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            rx = i
            ry = j
        elif graph[i][j] == "B":
            bx = i
            by = j
queue = deque()
queue.append([rx,ry,bx,by,1])
visit[rx][ry][bx][by] = True
bfs()

