
arr = [1,2,3,4,5]
# 여기에서 두개를 뽑는 경우의 수

visit = [0,0,0,0,0]
# 1. dfs 를 이용하여 두개 뽑기, 조합
# 방법.
# for 문으로 하나씩 돌면서 값을 append 하는데, 2개가 들어갈 경우 리턴
# 재귀 호출을 통해 append한 값 말고 다른 값으로 append 하여 주어진 수 2개 넣어 줄 수 있다.
# 재귀호출 이후 백트래킹으로 현재 값 pop, visit 초기화해주면 방금 append 했던 값 빼고 다른 값 append 할 수 있음.
# 재귀호출할 때 넘기는 인덱스 값에 따라 순열과 조합으로 구현할 수 있다.
# 순열은 순서에 상관없이 뽑기 때문에 재귀호출할때 inx를 현재 depth와 같은 값으로 넘기면 순열이됨. 현재 값을 제외하고 처음부터 서칭이 가능하기 때문.
# 조합은 재귀호출할 때 inx를 현재 인덱스 다음 값인 Inx+1로 넘기면 됨.


tot = []

def dfs(cnt,depth, answer):
    if cnt == 2 :
        tot.append(answer[:])
        return

    for i in range(depth,len(arr)):
        if visit[i] == 0:
            visit[i] = 1
            answer.append(arr[i])
            dfs(cnt+1,i+1,answer)
            visit[i] = 0
            answer.pop()
    return

dfs(0,0,[])
print(tot)