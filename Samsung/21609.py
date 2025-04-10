# 상어 중학교
# 아래를 블록 그룹 존재하는 동안 반복
    # 1. 가장 큰 블록 그룹 찾기
        # bfs()로 최대값 업데이트 하며 찾기
            # 일단 bfs에서 리턴한 tmp_group이
                # 현재 값보다 크면
                    # 현재 블록들 저장하고 있는 big_group을 초기화 하고 append
                # 현재 값과 같으면 big_group에 그냥 추가
            # 최종 완성된 big_group의 길이가 1이면 그대로 리턴,
            # 아니면
                # 포함된 무지개 블록의 수가 가장 많은 블록 그룹,
                # 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을,
                # 그것도 여러개이면 열이 가장 큰 것을 찾는다.
                # (기준 블록: 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록)
    # 2. 1에서 찾은 그룹의 모든 블록 제거후 점수 획득
        # big_group에 해당하는 모든 좌표 제거
            # 제거된 좌표는 -10이라고 하자
        # 점수 획득 후 합산
            # 그룹에 포함된 블록의 수를 B라 할 때,
            # result += B ** 2
    # 3. 격자에 중력 작용 gravity()
        # 검은색 블록(-1)을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
        # (이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속됨)
            # 모든 게임판 좌표에 대하여 (행은 밑에서 부터 거꾸로 간다/ N-2부터 0번 까지)
                # 0이상의 블록 일 때, 아래 칸의 좌표가 -10이면,
                    # 아래 칸으로 이동 후, 원래 칸을 -10으로 바꾸고 아래 칸에 본인을 넣음
                        # 아래 칸이 -10이 아닐 때 까지 계속 진행
        #중력 작용한 배열 리턴

    # 4. 격자가 90도 반시계 방향으로 회전 rotate_90()
        # new 행 = old 열 - (N-1)
        # new 열 = old 행
    # 5. 다시 격자에 중력이 작용 gravity()

    # 종료 조건 - 블록 존재하는지 검사 condition()
# 6. result 출력

import copy
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))

def bfs(x, y, visited) :
    group = []
    cnt = 1
    que = deque()

    color = board[x][y]
    que.append((x, y))
    while que :
        x, y = que.popleft()
        group.append((x, y))
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if board[nx][ny] == color or board[nx][ny] == 0 :
                    que.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt, group

def find_big() :
    max_v = -1
    big_group = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                tmp, tmp_group = bfs(i, j, visited)

                if max_v < tmp:
                    max_v = tmp
                    big_group.clear()
                    big_group.append(tmp_group)
                elif max_v == tmp : big_group.append(tmp_group)

            for a in range(N):
                for b in range(N):  # 0일 때는 방문 처리 다시 없애줘야 함
                    if board[a][b] == 0: visited[a][b] = 0

    if len(big_group) == 1 :
        for bg in big_group : return bg

    l = len(big_group)
    # 현재 big_group에 있는 블록들에 대해 (무지개블록수, 기준블록 x좌, y좌) 저장
    blocks = [[0, 0, 0, i] for i in range(l)]

    for i in range(l) :
        cnt_rbw = 0
        blk = []
        for arr in big_group[i] :
            x, y = arr
            if board[x][y] == 0 : cnt_rbw += 1
            else : blk.append([x, y])

        blk.sort()
        blocks[i][0] = cnt_rbw
        blocks[i][1], blocks[i][2] = blk[0][0], blk[0][1]

    blocks.sort(reverse=True)
    idx = blocks[0][3]
    return big_group[idx]


def bfs2(x, y, visit) :
    cnt = 1
    que = deque()

    color = board[x][y]
    que.append((x, y))
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if board[nx][ny] == color or board[nx][ny] == 0 :
                    que.append((nx, ny))
                    visit[nx][ny] = 1
                    cnt += 1
    return cnt

def gravity(arr) :
    for i in range(N-1, -1, -1) :
        for j in range(N) :
            if arr[i][j] > -1 :
                for k in range(i, N-1) :
                    if arr[k+1][j] == -10 : # 아래 칸이 -10이면 아래로 다운
                        arr[k+1][j] = arr[k][j]
                        arr[k][j] = -10
                    else : break
    return arr

def rotate_90(old_arr) : # 반시계 90도 회전
    new_arr = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N) :
         for j in range(N) :
             new_arr[N - 1 - j][i] = old_arr[i][j]

    return new_arr

def condition() :
    visits = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if board[i][j] > 0 and not visits[i][j]:
                visits[i][j] = 1
                temp = bfs2(i, j, visits)
                if temp >= 2 : return False

    return True
######## Main ########
result = 0
while True :    ## 종료 조건
    if condition() : break

    big = find_big() # 1. 가장 큰 블록 찾기

    # 2. 1에서 찾은 그룹의 모든 블록 제거후 점수 획득
    for b in big :
        x, y = b
        board[x][y] = -10
    result += len(big) ** 2

    # 3. 격자에 중력 작용 gravity()
    board = gravity(copy.deepcopy(board))

    # 4. 반시계 방향 회전 (지금 이게 문제)
    board = rotate_90(board)

    # 5. 다시 격자에 중력이 작용
    board = gravity(copy.deepcopy(board))

print(result)