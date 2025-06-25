# 미세먼지 안녕!
# 55분 
"""
T초 동안 1,2를 반복
1. 미세먼지 확산 - 모든 칸 동시 발생
    >> 모든 칸에 대해 상하좌우 탐색 후, 새로운 배열에 추가 후 리턴 
    - 인접한 네 방향으로 확산. 방향에 공기청정기가 있거나, 칸이 없으면 확산x
    - 확산되는 양은 A/5, 소수점 버림 
    - 원래 위치에 남는 미세먼지의 양은 A-int(A/5)*확산된 방향의 개수
2. 공기청정기 작동
    >> 위쪽, 아래 쪽 따로 작업 -> 해당 방향으로 순환 로직을 미리 짜두고 그 방향대로 미세먼지 이동 후 리턴
    - 위쪽 청정기 > 반시계 순환
    - 아래쪽 > 시계 순환 
    - 바람이 불면 미세먼지가 바람 방향으로 모두 한칸씩 이동
    - 일단 그림에서 화살표에 표시된 부분(가장자리)만 이동한다고 가정 

3. 반복 이후 남아있는 미세먼지의 양 출력
"""
dx = [0, -1, 0, 1] # 우상좌하 
dy = [1, 0, -1, 0]

dx2 = [0, 1, 0, -1] # 우하좌상 
dy2 = [1, 0, -1, 0]

R, C, T = map(int, input().split())
board = []
for _ in range(R) : board.append(list(map(int, input().split())))

# 공기청정기 미리 찾아두기
tx, ty = -1, -1
bx, by = -1, -1
for i in range(R) : 
    for j in range(C) : 
        if board[i][j] == -1 :
            if (tx, ty) == (-1, -1) : 
                tx, ty = i, j
            else :
                bx, by = i, j
                break

def is_inrange(x, y) :
    return 0<= x < R and 0 <= y < C 

def move_send() :
    new_board = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R) : 
        for j in range(C) : 
            if board[i][j] == -1 : 
                new_board[i][j] = -1
                continue
            A = board[i][j]
            move = A // 5
            cnt = 0
            for k in range(4) : 
                nx = i + dx[k]
                ny = j + dy[k]
                if is_inrange(nx, ny) and board[nx][ny] != -1:
                    cnt += 1
                    new_board[nx][ny] += move
            
            new_board[i][j] += A - cnt * move 
    
    return new_board

def clear_send_top(x, y) :
    new_board = [b[:] for b in board]
    # 처음 청정기 앞 칸을 우상좌하 우선순위로 한칸 선택 
    direct = -1 # 첫 시작 방향 
    px, py = -1, -1 # 첫 시작 칸 
    for i in range(4) : 
        nx, ny = x + dx[i], y + dy[i]
        if is_inrange(nx, ny) : 
            px, py = nx, ny
            direct = i
            break

    amount = board[px][py] # 이동할 모래 
    new_board[px][py] = 0
    while True :
        ax, ay = px + dx[direct], py + dy[direct] # 이동할 곳 
        if not is_inrange(ax, ay) : 
            direct += 1
            if direct > 3 : direct = 0 
            continue
        
        if (ax, ay) == (x, y) : break
        
        new_board[ax][ay] = amount
        amount = board[ax][ay]
        px, py = ax, ay
    
    return new_board
    
def clear_send_bottom(x, y) :
    new_board = [b[:] for b in board]
    # 처음 청정기 앞 칸을 우하좌상 우선순위로 한칸 선택 
    direct = -1 # 첫 시작 방향 
    px, py = -1, -1 # 첫 시작 칸 
    for i in range(4) : 
        nx, ny = x + dx2[i], y + dy2[i]
        if is_inrange(nx, ny) : 
            px, py = nx, ny
            direct = i
            break

    amount = board[px][py] # 이동할 모래 
    new_board[px][py] = 0
    while True :
        ax, ay = px + dx2[direct], py + dy2[direct] # 이동할 곳 
        if not is_inrange(ax, ay) : 
            direct += 1
            if direct > 3 : direct = 0 
            continue
        
        if (ax, ay) == (x, y) : break
        
        new_board[ax][ay] = amount
        amount = board[ax][ay]
        px, py = ax, ay
    
    return new_board

for _ in range(T) :
    board = move_send()
    board = clear_send_top(tx, ty)
    board = clear_send_bottom(bx, by)

    # for b in board : print(b)

sums = 2
for b in board : sums += sum(b)
print(sums)