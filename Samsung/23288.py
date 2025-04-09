# 주사위 굴리기 2
# 1시간 만에 다 품

# 방향: 동, 서, 남, 북 (1, 2, 3, 4)
# 주사위 데큐 dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
# board 에서 점수 관리
# 1. 주사위 굴리기
    # 지정된 방향으로 한칸 굴린다
    # 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴린다
    # 이 때 dice 전개도 업데이트, board에서 주사위 위치도 업데이트 (nx, ny)

# 2. 주사위가 도착한 칸에 대한 점수 획득
    # 도착한 칸(x, y)에 연결된 칸들 중, 값이(B) 같은 칸들의 갯수를 구한다 bfs()
    # 방금 구한 갯수를 C라고 할 때, 점수는 B*C가 됨
    # result에 점수 합산

# 3. 주사위 이동 방향 결정
    # A가 현재 주사위 아랫면일 때, 즉 A = dice[3][1]
        # A > B인 경우 이동 방향을 90도 시계 방향으로 회전
        # A < B인 경우 이동 방향을 90도 반시계 방향으로 회전
        # A = B인 경우 이동 방향에 변화 없음
# 4. 점수의 합 출력

from collections import deque
dice = deque()
dice.append(deque([0, 2, 0]))
dice.append(deque([4, 1, 3]))
dice.append(deque([0, 5, 0]))
dice.append(deque([0, 6, 0]))

dx = [0, 0, 1, -1] # 동 서 남 북
dy = [1, -1, 0, 0]
N, M, K = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))

def bfs(x, y, cnt) :
    visited = [[0 for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == B and not visited[nx][ny]:
                cnt += 1
                que.append((nx, ny))
                visited[nx][ny] = 1

    return cnt

direct = 1
x, y = 0, 0
result = 0
for _ in range(K) :
    nx = x + dx[direct-1]
    ny = y + dy[direct-1]

    if nx < 0 or nx >= N or ny <0 or ny >=M : # 경계 넘으면 반대 방향으로
        if direct % 2 == 0 : direct -= 1
        else : direct += 1
        nx = x + dx[direct - 1]
        ny = y + dy[direct - 1]

    x, y = nx, ny # 주사위 위치 업데이트

    # 전개도 업데이트
    if direct == 1 : # 동
        dice[1].appendleft(dice[3][1])
        dice[3][1] = dice[1].pop()
    elif direct == 2 : # 서
        dice[1].append(dice[3][1])
        dice[3][1] = dice[1].popleft()
    elif direct == 3 : # 남
        tmp = dice[3][1]
        for i in range(2, -1, -1) :
            dice[i+1][1] = dice[i][1]
        dice[0][1] = tmp
    else : # 북
        tmp = dice[0][1]
        for i in range(1, 4):
            dice[i-1][1] = dice[i][1]
        dice[3][1] = tmp

    # 2. 점수 획득
    B = board[x][y]
    C = 1
    C = bfs(x, y, C)
    result += B*C

    # 3. 주사위 이동 방향 결정
    A = dice[3][1]
    if A > B :
        if direct <= 2 : direct += 2
        elif direct == 3: direct -= 1
        else: direct -=3
    elif A < B :
        if direct >= 3: direct -= 2
        elif direct == 2 : direct += 1
        else : direct += 3

print(result)