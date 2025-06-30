# 스타트 택시
# 2시간 20분 걸림

"""
로직 
0. 보드 초기화 
    - 보드에 벽(1)은 -1로 바꾸기
    - 승객 번호 보드에 저장

아래 1, 2번을 m번 반복 
1. 지금 태울 승객 고르기
    - 최단거리 > 행 작은 > 열 작은 
        - 최단 거리 구할 때 택시 승객 위치 같은거 먼저 체크 
    >> bfs 내에서 최단거리에 있는 모든 승객 모두 리스트에 저장한 후, 
        해당 리스트에서 행열 작은 것 리턴

2. 승객 -> 목적지 
    - 그 승객 인덱스-1로 접근 해서 출발지 ~ 목적지와의 거리 계산 >> bfs
    - 이후 보드에서 그 승객 위치는 0으로 바꾸기
    - 거리 > 현재 연료 : -1 출력 후 완전 종료
    - 거리 <= 현재 연료 :
        현재 연로 -= 거리 
        현재 연료 += 거리 * 2
    - 택시 위치 목적지로 이동 시키기 

3. 출력
아직 승객이 남아있으면 -1 출력
아니면 현재 남은 연료 출력

<<< 예외 상황 >>>
- 손님은 있지만 벽 때문에 태우러 못 갈 경우 - 종료 
- 손님을 태웠지만 벽 때문에 목적지까지 못 갈 경우 - 종료
- 손님 픽업 전, 택시 칸에 손님이 있는 경우 - 바로 태움
- 픽업한 손님의 출발지 == 목적지 일 경우 - 바로 내림

"""

from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N, M, Y = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))
for i in range(N) : 
    for j in range(N) :
        if board[i][j] == 1 :
            board[i][j] = -1

tx, ty = map(int, input().split()) # 택시 위치
tx, ty = tx-1, ty-1
p_arr = [] # 승객 출발-도착 정보
for m in range(M) : 
    sx, sy, ex, ey = map(int, input().split())
    sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1
    p_arr.append([sx, sy, ex, ey])
    board[sx][sy] = m+1

def is_inrange(x, y):
    return 0 <= x < N and 0 <= y < N

def bfs(x, y):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    que = deque()
    que.append((x, y))
    visited[x][y] = 1
    is_select = -1
    candidate = []
    while que : 
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] >= 0:
                num = board[nx][ny]
                if num > 0 :
                    if is_select == -1 : 
                        is_select = visited[x][y]
                        candidate.append((nx, ny, num))
                    elif is_select == visited[x][y] :
                        candidate.append((nx, ny, num)) 
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))

    if not candidate : return -1, -1
    candidate.sort()
    return candidate[0][2], is_select

# 시간 초과 난 로직 : 모든 승객과의 거리 bfs로 구해서 최소 구한 것
# 수정한 로직: 
    # 가장 짧은 거리에 있는 승객만 모두 구해서 리스트에 넣은 후, 그 리스트에서 행 열 작은 것 리턴 
def select(x, y) :
    if board[x][y] > 0 : # 택시 위치에 바로 승객 있는 경우 
        return board[x][y], 0

    n, dist = bfs(x, y)
    if n == -1 : # 도달할 수 있는 곳이 없는 경우 
        print(-1)
        exit()

    return n, dist

def bfs2(x, y, num):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    while que : 
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] >= 0:
                if board[nx][ny] == num :
                    return visited[x][y]
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))

    return -1

def move(x, y, num, fuel):
    sx, sy, ex, ey = p_arr[num-1]
    d = 0
    if (sx, sy) != (ex, ey) :
        d = bfs2(ex, ey, num)
    
    if d > fuel or d == -1:
        print(-1)
        exit()
    
    fuel -= d
    fuel += d*2

    board[sx][sy] = 0
    tx, ty = ex, ey
    p_arr[num-1] = [-1, -1, -1, -1]

    return board, fuel, tx, ty

###### Main ######
cnt = 0
for _ in range(M) :
    n, di = select(tx, ty) # 1. 승객 선택
    Y -= di # 승객 태우러 가는 만큼 연료 소모 
    board, Y, tx, ty = move(tx, ty, n, Y) # 2. 승객 이동 시키기 
    cnt += 1


if cnt == M: print(Y)
else : print(-1)