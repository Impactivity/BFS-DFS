import sys

read = sys.stdin.readline
sys.setrecursionlimit(100001)
n = int(read())

# 문제 풀이
# 현재 노드의 부모노드가 누구인지 알려면
# dfs를 통해 자신을 호출한 이전 노드가 무엇인지 알면 된다. 그 노드가 부모노드이기 때문이다.

graph = [ [] for _ in range(n+1) ]
visited = [0] * (n+1)
for i in range(n-1):
    a,b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    for i in graph[n]:
        if visited[i] == 0 :
            visited[i] = n
            dfs(i)

dfs(1)
for i in range(2, n+1):
    print(visited[i])
