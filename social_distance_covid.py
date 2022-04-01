from collections import deque


def solution(places):
    answer = []

    T = len(places)
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    for i in range(T):
        graph = places[i]
        pos = []

        # 사람들의 좌표를 저장하고
        # bfs로 모든 경로 탐색하면서 이동거리 만큼 증가하여 P를 발견하면 현재 위치에서 거리를 구함.
        # 3이하이면 바로 return 0
        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    pos.append((i, j))

        # P가 있는 위치에서 부터 탐색시작.
        is_keep = True
        for x, y in pos:
            visited = [[0] * 5 for _ in range(5)]
            queue = deque()
            queue.append((x, y))
            visited[x][y] = 1

            while queue:
                a, b = queue.popleft()

                for i in range(4):
                    nx = a + dx[i]
                    ny = b + dy[i]

                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if graph[nx][ny] == 'O':
                            if visited[nx][ny] == 0:
                                visited[nx][ny] = visited[a][b] + 1
                                queue.append((nx, ny))

                        elif graph[nx][ny] == 'P':
                            if visited[nx][ny] == 0:
                                if visited[a][b] + 1 <= 3:
                                    is_keep = False
                                    answer.append(0)
                                    break

                if is_keep == False:
                    break

            if is_keep == False:
                break

        if is_keep == False:
            continue

        answer.append(1)

    return answer