from collections import deque


def solution(n, computers):
    answer = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        if visited[i][i] == 0:
            queue = deque()
            queue.append(i)
            visited[i][i] = 1

            while queue:
                node = queue.popleft()
                for next_inx in range(len(computers[node])):
                    if computers[node][next_inx] == 1:
                        if visited[node][next_inx] == 0:
                            queue.append(next_inx)
                            visited[node][next_inx] = 1

            answer += 1

    return answer