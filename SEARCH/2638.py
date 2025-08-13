# 치즈
'''
로직
0. 보드 상태
    - 0: 치즈 속 구멍 1: 치즈 2: 외부 공기 3: 곧 녹을 치즈 
아래를 치즈 없어질 때 까지 반복
1. 현재 치즈 존재하는지 검사 - is_exist
    - False면 sec 출력 후 종료
2. 현재 외부 공기 모두 2로 바꾸기
    - 첫 공기 좌표로 부터 bfs로 2 또는 0 인것을 모두 2로 바꾼다
3. 현재 모든 치즈 덩어리에 대해 두 변 이상 공기(2)와 접촉한 치즈 모두 3으로 바꿈
    - 방문 기록 참고해서 각 치즈 덩어리 마다 bfs로 탐색하며 체크
4. 3으로 바뀐 치즈 2로 바꾸기 (녹이기)
'''
from collections import deque
import sys; input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))

def is_inrange(x, y) :
    return 0 <= x < N and 0 <= y < M

def is_exist() : 
    for i in range(N) : 
        for j in range(M) : 
            if board[i][j] == 1 : 
                return True
    
    return False

def bfs(x, y) :
    que = deque()
    visit = [[0 for _ in range(M)] for _ in range(N)]
    que.append((x, y))
    visit[x][y] = 1

    while que :
        x, y = que.popleft()
        board[x][y] = 2
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visit[nx][ny] and (board[nx][ny] == 0 or board[nx][ny] == 2) :
                que.append((nx, ny))
                visit[nx][ny] = 1

sx, sy = -1, -1
for i in range(N) :
    if (sx, sy) != (-1, -1) :
        break
    for j in range(N) :
        if board[i][j] == 0 :
            cnt = 0
            for k in range(4) :
                ni, nj = i + dx[k], j + dy[k]
                if is_inrange(ni, nj) and board[ni][nj] == 1 :
                    cnt += 1
            if cnt <= 2 :
                sx, sy = i, j
                break

def find_cheese(x, y) : 
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    while que: 
        x, y = que.popleft()
        cnt = 0
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and board[nx][ny] == 2 : 
                cnt += 1
        if cnt >= 2 : 
            board[x][y] = 3 
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == 1 : 
                que.append((nx, ny))
                visited[nx][ny] = 1

sec = 0
while True :
    if not is_exist() : # 1
        print(sec)
        exit()
    
    sec += 1

    bfs(sx, sy) # 2

    visited = [[0 for _ in range(M)] for _ in range(N)] # 3. 치즈 녹이기 
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 1 and not visited[i][j] :
                visited[i][j] = 1
                find_cheese(i, j)
    
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 3 : board[i][j] = 2
