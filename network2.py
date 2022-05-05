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
                for next_node in range(len(computers[node])):
                    if computers[node][next_node] == 1:
                        if visited[node][next_node] == 0:
                            queue.append(next_node)
                            visited[node][next_node] = 1

            answer += 1

    return answer


def solution2(n, computers):
    length = len(computers)
    answer = 0
    graph = [[] * n for _ in range(n)]
    visited = [0] * n

    for i in range(length):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    for num in range(n):
        if graph[num] and visited[num] == 0:
            queue = deque()
            visited[num] = 1
            queue.append(num)

            while queue:
                cur_com = queue.popleft()

                for next_com in graph[cur_com]:
                    if visited[next_com] == 0:
                        visited[next_com] = 1
                        queue.append(next_com)

            answer += 1

        elif visited[num] == 0:
            answer += 1

    return answer



solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])