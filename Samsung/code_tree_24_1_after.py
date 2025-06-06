"""
2시간 20분 소요 - 다 맞음

로직
0. 입력 받기 및 사용할 배열
    - 입력: R, C, K
        K번 반복하며 c(골렘 출발 열), d(초기 출구 방향) 입력
         이때 d는 0~3 (북동남서)
    - 현재 이동중인 골렘의 좌표: r=1, c=ci 를 중심좌표로 시작해서, 이동 검사 시에는 이 중심 좌표에 대해서 상하좌우 탐색
    - 출구의 방향 d: 0~3의 형태로 저장 후
        '1. 골렘 이동' 에서는 반시계, 시계 방향으로만 바꿈
    - forest : 현재 숲의 상태 --> R +3 행 C 열 이고 (등장 때문에) , 숲은 3<=행<=R-1 이다.
    - result : 누적 최대 행

아래를 K번 반복
1. 골렘 이동
    # 더이상 움직이지 못할 때 까지 2-1 ~ 2-3 을 반복
    1-1. 남쪽으로 이동 가능하면, 남쪽으로 한칸 이동
    1-2. 위 이동 불가능 할 때, 서 -> 남 으로 이동 가능하면, 서남쪽으로 한칸 이동
        - 이동하면, 출구가 반시계 방향으로 이동
    1-3. 위 이동 다 불가할 때, 동 -> 남 으로 이동 가능하면, 동남쪽으로 한칸 이동
        - 이동하면, 출구가 시계 방향으로 이동
    1-4. 더이상 움직이지 못하면 골렘 중심 좌표와, 출구 방향(업데이트된 d) 리턴

2. 숲 채우기
    2-1. 2번을 통해 가장 남쪽으로 내려왔는데, 골렘의 몸 일부가 숲 벗어난 상태면 배열 forest 초기화 -> 다음 골렘으로 continue
    2-2. 2번에서 리턴된 골렘 중심 좌표와, 출구 방향(업데이트된 d)로 5칸의 골렘을 숲에 위치 시키기
        중심은 3으로, 출구 위치는 2로, 나머지는 1로

3. 정령 이동 (가장 남쪽 칸으로) - bfs()
    # 이때, 현재 골렘에서의 출구 방향을 먼저 저장 (중심에서 상하좌우 탐색 중 값이 2인 것)
    3-1. 골렘 내에서 이동 (우선 가장 큰 행번호 저장)
    3-2. 출구를 타고 다른 골램으로 이동 (거기서 가장 남쪽 행과 현재 가장 큰 행번호 비교)
        계속 출구 타고 이동 (이동 불가일 때 까지 반복)
    3-3. 최종 가장 남쪽 칸인 가장 큰 행번호를 누적 (result += 행번호)
"""
from collections import deque
dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]

R, C, K = map(int, input().split())
info = [] # 정령 위치 정보
for _ in range(K) : info.append(list(map(int, input().split())))

result = 0
forest = [[0 for _ in range(C)] for _ in range(R+3)]

def move_south(g_info) :
    r = 1 # 골렘 출발 중심 행 위치
    c, d = g_info # 골렘 출발 중심 열 위치, 초기 출구 방향
    c -= 1 # 0번 부터 시작하려고

    move = True
    while move :
        move = False

        if 0<= r+2 <R+3 and 0<= c-1 < C and 0<= c+1 < C : # 숲 경계 체크
            if forest[r+1][c-1] == 0 and forest[r+1][c+1] == 0 and forest[r+2][c] == 0 : # 빈칸인지 체크
                r += 1 # 남쪽으로 이동
                move = True
                continue

        if 0<= r+2 <R+3 and 0<= c-2 < C : # 숲 경계 체크
            if forest[r-1][c-1] == 0 and forest[r][c-2] == 0 and forest[r+1][c-1] == 0 and forest[r+1][c-2] == 0 and forest[r+2][c-1] == 0: # 빈칸인지 체크
                r += 1 # 서남쪽으로 이동
                c -=1
                d = (d+3) % 4 # 반시계 이동
                move = True
                continue

        if 0<= r+2 <R+3 and 0<= c+2 < C : # 숲 경계 체크
            if forest[r-1][c+1] == 0 and forest[r][c+2] == 0 and forest[r+1][c+1] == 0 and forest[r+1][c+2] == 0 and forest[r+2][c+1] == 0: # 빈칸인지 체크
                r += 1 # 동남쪽으로 이동
                c +=1
                d = (d+1) % 4 # 시계 이동
                move = True
                continue

    return r, c, d # 중심좌표와 방향

def fill_forest(r, c, d) :

    x, y = r, c
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 3 or ny < 0 or ny >= C : return True

    forest[x][y] = 3 # 중심
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if d == i: forest[nx][ny] = 2 # 출구
        else : forest[nx][ny] = 1  # 나머지

    return False

def move_bfs(r, c) :
    visited = [[0 for _ in range(C)] for _ in range(R + 3)]

    que = deque()
    que.append((r, c))
    visited[r][c] = 1
    max_row = 0
    ex, ey = 0, 0  # 현재 출구 좌표
    while que :
        x, y = que.popleft() # 현재 중심
        if forest[x][y] !=3 : # 중심이 아닌게 들어있으면 중심으로 바꿔주기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if forest[nx][ny] == 3 :
                    x, y = nx, ny
                    visited[x][y] = 1

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < R+3 and 0 <= ny < C : # 숲 경계
                if nx > max_row : max_row = nx
                if forest[nx][ny] == 2 : ex, ey = nx, ny # 출구 좌표 저장

        for i in range(4) :
            nx = ex + dx[i]
            ny = ey + dy[i]
            if 0<= nx < R+3 and 0 <= ny < C and not visited[nx][ny] :
                if forest[nx][ny] == 1 or forest[nx][ny] == 2 :
                    que.append((nx, ny))
                    visited[nx][ny] = 1

    return max_row-2


##### Main #####
for k in range(K) :
    r, c, d = move_south(info[k]) # 1. 골렘 이동

    init = fill_forest(r, c, d) # 2. 숲 채우기

    if init : # 숲 벗어난 상태면 초기화 하고, 다음 골렘 차례로
        forest = [[0 for _ in range(C)] for _ in range(R + 3)]
        continue

    tmp = move_bfs(r, c) # 3. 정령 이동 (가장 남쪽 칸으로)
    result += tmp

print(result)