# 인구 이동

"""
더이상 인구 인동이 없을 때 까지 아래 과정을 반복

1. 모든 인접한 두 칸씩 국경선의 차이 계산 -> 차이가 L과 R 사이면, 국경선 열기 [open_border]
    - 국경선 여는 법: (새로운 탐색 배열 - test_board로 처리)
        - (0, 0)부터 차이가 있으면 bfs로 탐색해서 같은 숫자로 저장 (연합국 번호 1부터 시작-> 점점 증가)
            - bfs 탐색 시 방문처리 상태 유지하기
        - bfs 탐색 끝나면, 연합국 번호 1증가 시킴
        - 아직 방문하지 않은 나라부터 다시 bfs 시작 -> 연합국 번호로 국경선 배열 처리

1.5. 국경선 하나도 안열리면 반복 종료 -> 출력

2. 국경선 다 열었으면, 인구 이동 [move_people]
    - 연합을 이루는 각 칸의 인구 수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 됨 (소수점 버림)
3. 하루 추가 day += 1

"""

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, L, R = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))

def is_inrange(x, y) :
    return 0 <= x < N and 0 <= y < N

def bfs1(x, y, visited, number, tboard):
    que = deque()
    que.append((x, y))
    visited[x][y] = 1
    tboard[x][y] = number

    while que : 
        x, y = que.popleft()
        num1 = board[x][y]
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] :
                num2 = board[nx][ny] 
                if L <= abs(num1-num2) <= R : 
                    tboard[nx][ny] = number
                    que.append((nx, ny))
                    visited[nx][ny] = 1

    return visited, tboard

def open_border() :
    test_board = [b[:] for b in board]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    num = 0
    for i in range(N) :
        for j in range(N) :
            if not visited[i][j] :
                num += 1
                visited, test_board = bfs1(i, j, visited, num, test_board)

    if num == N*N : return False, test_board
    else: return True, test_board

def bfs2(x, y, visited, cnt_board) :
    que = deque()
    que.append((x, y))
    visited[x][y] = 1
    cnt = 1 # 칸의 갯수
    total = board[x][y] # 총 인구수
    num = cnt_board[x][y] # 연합국의 고유번호 
    pos = [] # 해당 연합국의 좌표 저장
    pos.append((x, y))
    
    while que : 
        x, y = que.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and cnt_board[nx][ny] == num:
                cnt += 1
                total += board[nx][ny]
                que.append((nx, ny))
                pos.append((nx, ny))
                visited[nx][ny] = 1
    
    calculated = total // cnt
    for (x, y) in pos : board[x][y] = calculated

    return visited, board

# bfs로 cnt_board의 같은 숫자 그룹 탐색해서 인구수 다시 계산해 보드에 넣기
# 각 인구수 = 총 인구수 / 칸의 개수
def move_people(cnt_board):
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N) :
        for j in range(N) :
            if not visited[i][j] : 
                visited, board = bfs2(i, j, visited, cnt_board)
    
    return board

day = 0
while True : 
    chk, cont_board = open_border() # 1
    if chk == False : # 1.5
        print(day)
        break
    board = move_people(cont_board) # 2  
    day += 1 # 3
