# 뱀
# 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 
# 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# 방법: 
# 매 시점마다 snake 배열에 뱀이 존재하는 위치를 항상 2차원 리스트에 기록
# 앞으로 전진한 값 nx, ny를 계속 담고
    # nx, ny의 값이 사과가 아니면 snake의 맨 왼쪽 값을 pop한다
    # 사과면 냅둬

from collections import deque

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]
for _ in range(K) :
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1 # 사과 심기

L = int(input())
info = deque()
for _ in range(L) :
    x, c = map(str, input().split())
    info.append((x, c)) # 뱀의 방향 전환 정보

dir = 1 # 원래 방향 (오른쪽)
time = 0 # 현재 지난 시각
arr[0][0] = 9 
x, y = 0, 0 # 초기 뱀 위치
snake = deque()
snake.append((0, 0))
while True :
    # 뱀의 방향 회전
    if info : X, C = info[0]
    if int(X)  == time :
        info.popleft()
        if C == 'L' : dir = (dir+3) % 4 # 왼쪽 90도 회전
        else : dir = (dir+1) % 4 # 오른쪽 90도 회전

    time += 1
    nx = x + dx[dir] 
    ny = y + dy[dir]
    if nx < 0 or nx >= N or ny < 0 or ny >= N : break
    if arr[nx][ny] == 9 : break # 본인 몸통 만나면 종료
    if arr[nx][ny] != 1: # 사과가 아니면
        if snake : # 꼬리 한칸 자르기
            a, b = snake.popleft()
            arr[a][b] = 0

    arr[nx][ny] = 9 # 뱀으로 바꾸고
    if (nx, ny) not in snake : snake.append((nx, ny)) # 뱀의 몸통 추가
    x, y = nx, ny
    
print(time)