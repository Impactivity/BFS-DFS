import math
import queue
# 카드 짝 맞추는 cost 비용의 최솟값을 구하는 문제이다.

# 문제의 key Point
# 1. 현재 위치에서 n번째 카드를 선택해서 짝맞추는 경우의 수를 모두 구해서 그 중 최솟값을 구한다.
# 그러나 n번째 카드를 선택할 때 같은 번호여도
# 1번이 -> 2번 , 2번 -> 1번 선택하는 경로 (순차, 역순) 중 최소를 선택해야한다.
# 짝을 맞추는 cost 는 다음과 같다.
# 현재위치에서 선택할 카드 번호중 첫번째로 선택할 카드로 이동하는 cost + 2번째 카트로 이동하는 cost + enter 두 번
Board = []  #전역변수 선언

Allcard = {} #모든카드를 딕셔너리로 삽입
Allremoved = 1 #0번째는 1로 세팅해서
MinCnt = math.inf # 최소 조작값

D = ((-1,0),(1,0),(0,-1),(0,1))

def bfs(removed, src, dst):
    visited = [[False for _ in range(4)] for _ in range(4)]
    q = queue.Queue()
    q.put(src)
    while q:
        curr = q.get()
        # 지금위치가 목적지와 같다면 row, col
        if curr[0] == dst[0] and curr[1] == dst[1]:
            return curr[2] #현재까지 조작수 리턴

        for i in range(4): # 방향키, ctrl키 움직였을 때 모든 경우 탐색
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            if nr < 0 or nr > 3 or nc < 0 or nc > 3 :
                continue
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.put((nr,nc,curr[2]+1)) # 현재 조작횟수에서 +1

            #컨트롤키 + 방향키 조작은 방향키 조작만 하는거랑 횟수가 같기에 방향키 for문안에 작성
            for j in range(2): # 끝에서 끝은 최대 거리 2
                if (removed & 1 << Board[nr][nc]) == 0: #현재 카드가 이미 제거된거면 break
                    break

                #컨트롤 조작도 맵 벗어나면 안되기에
                if nr + D[i][0] < 0 or nr + D[i][0] > 3 \
                or nc + D[i][1] < 0 or nc + D[i][1] > 3:
                    break

                nr += D[i][0]
                nc += D[i][1]

            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.put((nr, nc, curr[2] + 1))  # 현재 조작횟수에서 +1
    return math.inf




def permutate(cnt, removed, src) : #조작수, remove비트 , 카드 위치(행,열,조작수)
    global MinCnt

    if cnt >= MinCnt: # 최소값보다 큰값은 진행할 필요가 없기 때문에 return
        return

    if removed == Allremoved: #카드가 모두 제거되었으면 종료
        MinCnt = min(MinCnt, cnt)
        return

    for num, card in Allcard.items():
        if removed & 1 << num: # 해당 카드가 이미 삭제된거면 skip
            continue

        #현재 위치에서 0번(1번) 위치로 이동  + 1번(0번) 위치로 이동 + 엔터조작 2회
        one = bfs(removed, src, card[0]) + bfs(removed,card[0],card[1]) + 2 # 총필요한 순차 조작횟수
        two = bfs(removed, src, card[1]) + bfs(removed,card[1],card[0]) + 2 # 역순
        permutate(cnt+one, removed | 1 << num, card[1])
        permutate(cnt+two, removed | 1 << num, card[0])

def solution(board,r,c):
    global Board,Allcard, Allremoved
    Board = board
    for i in range(4):
        for j in range(4):
            num = Board[i][j]
            if num: # 값이 0이 아니면
                Allremoved |= 1 << num # 카드가 모두 제거되었는지 확인하는 비
                if num in Allcard:
                    Allcard[num].append((i,j,0))
                else: #dict 없는경우
                    Allcard[num] = [(i,j,0)] # 위차와 카드간 거리값

    permutate(0,1,(r,c,0))
    return MinCnt


board = [[1,0,0,3],
         [2,0,0,0],
         [0,0,0,2],
         [3,0,1,0]]

solution(board, 1,0)
