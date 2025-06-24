# 코드트리 - 포탑 부수기
# 3시간 30분 걸림 (코드 구현 1시간 + 디버긴 2시간 반)
# 처음에 틀린 이유)
# 1. 공격자는 포탑에서 공격 당하면 안되는 로직을 경계 넘어가서 공격자에게 왔을 때는 고려 안함. 즉 로직 위치를 잘못씀
# 2. 유사 백트래킹 할때도 경계 넘어가서 공격자 찾으면 멈춰야 하는지 순서 잘못써서 안멈춰서 반복 계속 돌아감. 로직 위치 바꿔서 바로 해결

# 마지막으로 틀린 이유)
# 디버깅 하려고 while True에서 10제한 걸어논거 안지워서 뒤에서 계속 틀림;;

"""
로직

0. 사용할 배열
    - board 게임판
    - 현재 무너지지 않은 포탑 관리 is_live
    - 최근 공격한 포탑 저장 recent

아래 1~6번을 K번 반복
부서지지 않은 포탑이 1개가 되면 즉시 종료

1. 공격자 선정
    - 가장 약한 포탑 우선 순위 (우선순위 배열에 모두 담고 솔팅)
        1) 공격력 가장 낮음
        2) 가장 최근에 공격한 포탑
        3) 행과 열의 합 가장큰
        4) 열이 가장 큰
    - 공격자로 선정되면 핸티캡: 공격력 += (N+M)
- 공격자로 선정되면 recent를 k로 업데이트

2. 공격 대상 선정
    - 가장 강한 포탑 우선 순위
        1) 공격력 가장 큼
        2) 공격한지 가장 오래됨
        3) 행과 열의 합 가장 작음
        4) 열이 가장 작음

## 공격) 레이저 공격 시도 => 안되면 포탄 공격
3. 레이저 공격 (bfs)
    - 규칙
        - 우하좌상으로 이동 (우선순위)
        - 부서진 포탑으로는 이동X
        - 가장 자리에서 막힌 방향 -> 반대 방향으로 나옴
    - 공격대상까지 최단 경로로 공격, 그러한 경로 없으면 4. 포탄 공격

    - 최단 경로 있다면 공격
        - 공격대상 -= (공격자의 공격력)
        - 나머지 경로에 애들 -= (공격자의 공격력)/2

4. 포탄 공격
    - 공격대상 -= (공격자의 공격력)
    - 공격 대상 주위 8방향에 있는 포탑 -= (공격자의 공격력)/2
        - 이때 공격자는 피해X, 가장 자리 밖으로 나가면 반대로 옮겨서 피해 받음

5. 공격 이후 공격력이 0이하가 된 포탑은 부서짐
    - 부서짐 처리, 보드에서도 공격력 0으로 변경
6. 포탑 정비
    - 부서지지 않은 포탑중 공격자도 아니고, 피해자도 아니었던 포탑은 공격력 += 1

7. 출력: 남아있는 가장 강한 포탑의 공격력 출력 - 이때도 아마 우선순위 적용하면 될듯

"""
from collections import deque

dx = [0, 0, 1, 0, -1] # 우하좌상
dy = [0, 1, 0, -1, 0]
ex = [-1, -1, -1, 0, 0, 1, 1, 1] # 8방향
ey = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))

is_live = [[1 for _ in range(M)] for _ in range(N)]
recent = [[0 for _ in range(M)] for _ in range(N)]
# 시작 전에 죽은거 관리
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            is_live[i][j] = 0

def select_attack_object():
    prior = []
    for i in range(N) :
        for j in range(M) :
            if is_live[i][j]:
                prior.append((board[i][j], -recent[i][j], -(i+j), -j, i, j))

    prior.sort()
    ax, ay = prior[0][4], prior[0][5]
    board[ax][ay] += (N+M)
    sx, sy = prior[-1][4], prior[-1][5]

    return board, ax, ay, sx, sy

# 최단 경로 구하기 - 방문 기록을 부모가 자신에게 온 방향으로 남김
# 나중에 대상자를 만났을 때, 그때부터는 거꾸로 공격자를 찾아감
# 그 과정에서 경로 공격력 감소하면 됨
def rasier_attack(ax, ay, sx, sy):
    move = False
    power = board[ax][ay]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append((ax, ay))
    visited[ax][ay] = 5
    while que :
        x, y = que.popleft()
        for i in range(1, 5) :
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 : nx = N-1
            elif nx >= N : nx = 0
            if ny < 0 : ny = M-1
            elif ny >= M : ny = 0
            if not is_live[nx][ny] : visited[nx][ny] = 1 # 죽은 애들은 어차피 방문할 필요 없으니까
            if not visited[nx][ny] and is_live[nx][ny] :
                if (nx, ny) == (sx, sy) :
                    visited[nx][ny] = i
                    move = True
                    break
                que.append((nx, ny))
                visited[nx][ny] = i

    if move : # 이동 가능하면,
        # for v in visited: print(v)
        board[sx][sy] -= power  # 공격력 감소
        x, y = sx, sy
        while True :
            dir = (visited[x][y] + 2) % 4 # 역순으로 추적
            if dir == 0 : dir = 4
            nx, ny = x + dx[dir], y + dy[dir]
            # print('prev: ',nx, ny)
            if nx < 0: nx = N - 1
            elif nx >= N: nx = 0
            if ny < 0: ny = M - 1
            elif ny >= M: ny = 0
            if (nx, ny) == (ax, ay): break # 이거 순서 잘못 되어서 무한 반복이었음
            # print('after: ', nx, ny)
            board[nx][ny] -= power//2
            x, y = nx, ny

        return board, True

    else : return board, False

def potan_attack(ax, ay, sx, sy) :
    power = board[ax][ay]
    board[sx][sy] -= power

    x, y = sx, sy
    for i in range(8) :
        nx, ny = x + ex[i], y + ey[i]
        if nx < 0: nx = N - 1
        elif nx >= N: nx = 0
        if ny < 0: ny = M - 1
        elif ny >= M: ny = 0
        if (nx, ny) == (ax, ay) : continue # 이것도 순서 잘못적어서 틀렸었음

        if is_live[nx][ny] :
            board[nx][ny] -= power//2

    return board

for k in range(K) :
    print("#"*10, "K: ", k+1)
    old_board = [b[:] for b in board] # 원래 정보 저장해둠
    print("공격 이전 -------")
    for b in board: print(b)

    board, ax, ay, sx, sy = select_attack_object() # 1. 공격자 선정 # 2. 대상자 선정
    recent[ax][ay] = k+1 # 공격자로 선정되면 recent를 k로 업데이트
    print('ax, ay: ', ax, ay)
    print('sx, sy: ', sx, sy)

    board, is_attack = rasier_attack(ax, ay, sx, sy) # 3. 레이저 공격 (bfs)
    if is_attack :
        print("레이저 공격-------")
        for b in board : print(b)

    if not is_attack :
        board = potan_attack(ax, ay, sx, sy) # 4. 포탄 공격

        print("포탄 공격-------")
        for b in board: print(b)

    # 5. 공격 이후 공격력이 0이하가 된 포탑은 부서짐
    for i in range(N) :
        for j in range(M) :
            if is_live[i][j]:
                if board[i][j] <= 0 :
                    board[i][j] = 0
                    is_live[i][j] = 0
    # 6. 포탑 정비
    # 부서지지 않은 포탑중 공격자도 아니고, 피해자도 아니었던 포탑은 공격력 += 1
    # 점수 그대로면 관련 없는애
    for i in range(N) :
        for j in range(M) :
            if is_live[i][j] :
                if (i, j) == (ax, ay) : continue
                if board[i][j] == old_board[i][j] :
                    board[i][j] += 1

    print("포탑 정비-------")
    for b in board: print(b)
    # 얼리 종료 조건 - 생존 포탑 1개 이하
    sums = 0
    for live in is_live : sums += sum(live)
    if sums <= 1 : break

# 7. 출력
max_val = 0
for bd in board :
    tmp = max(bd)
    max_val = max(max_val, tmp)
print(max_val)