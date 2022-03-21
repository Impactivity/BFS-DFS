def solution(n, computers):
    answer = 0
    visit = [0] * n

    for cur_com in range(n):
        if visit[cur_com] == 0:
            dfs(n, computers, cur_com, visit)
            answer += 1

    return answer


def dfs(n, computers, cur_com, visit):
    visit[cur_com] = 1
    for i in range(n):
        if computers[cur_com][i] == 1:
            if i != cur_com and visit[i] == 0:
                dfs(n, computers, i, visit)


