from collections import deque

def solution(brown, yellow):
    # 전체 격자의 수
    tot = brown + yellow
    answer = []
    # 세로 예상 길이 구하기
    arr = deque()
    for i in range(3, tot):
        if tot % i == 0:
            col = tot // i
            row = i
            if row > col:
                continue

            arr.append((col, row))

    if len(arr) == 1:
        return arr[0]

    # 우하좌상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 우하좌상 방향으로 돌면서 cnt하여 brown 수와 같으면 가로,세로 리턴
    while arr:
        tmp_col, tmp_row = arr.popleft()
        visited = [[0] * tmp_col for _ in range(tmp_row)]
        queue = deque()
        queue.append((0, 0))
        visited[0][0] = 1

        direction = 0
        cnt = 1
        while queue:
            x, y = queue.popleft()

            nx = x + dx[direction]
            ny = y + dy[direction]

            #사각형 범위를 벗어났을 경우, 방향 전환
            if nx < 0 or nx >= tmp_row or ny < 0 or ny >= tmp_col:
                direction = (direction + 1) % 4
                queue.append((x, y))
                continue

            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1

        if brown == cnt:
            answer.append([tmp_col, tmp_row])
            return answer[0]









