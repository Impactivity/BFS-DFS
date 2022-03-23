from collections import deque
# 두개의 단어가 서로 다른 알파벳 갯수 체크
def check(src, dst):
    tmp_cnt = 0
    for i in range(len(src)):
        if src[i] == dst[i]:
            tmp_cnt += 1

    if tmp_cnt == len(src) - 1:
        return True
    else:
        return False


def solution(begin, target, words):
    size = len(words)
    queue = deque()
    queue.append((begin, 0))
    visited = [0] * size

    while queue:
        node, cnt = queue.popleft()
        if node == target:
            return cnt
        # 한개 알파벳만 다른 단어 탐색
        for i in range(size):
            if visited[i] == 0:
                if check(node, words[i]):
                    visited[i] = 1
                    queue.append((words[i], cnt + 1))

    return 0




