from collections import deque

def solution(triangle):
    queue = deque()
    visited = [[0] * i for i in range(1, len(triangle) + 1)]
    queue.append((0, 0))
    visited[0][0] = triangle[0][0]
    dx = [1, 1]
    dy = [0, 1]
    while queue:
        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(triangle):
                if 0 <= ny < len(triangle[nx]):
                    if visited[nx][ny] == 0: #방문하지 않았던 경우 그냥 더해주기
                        visited[nx][ny] = visited[x][y] + triangle[nx][ny]
                        queue.append((nx, ny))
                    else: # 방문한적이 있던 경우 최댓값 구해서 업데이트
                        visited[nx][ny] = max(visited[x][y] + triangle[nx][ny], visited[nx][ny])

    return max(visited[len(triangle) - 1])