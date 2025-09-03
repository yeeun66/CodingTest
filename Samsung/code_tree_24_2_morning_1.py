# 타임머신이 탈출구까지 이동하는데 필요한 최소시간 출력
# 탈출 불가 시 -1 
# BFS (방문 처리)와 2차원, 3차원 따로 돌리는 BFS가 중요한 문제였다!

'''
메모리 초과 문제 해결
방문처리 제대로 + 3차원과 2차원을 따로 bfs하기!!
3차원 -> 2차원으로 가는 경로는 단 한 곳 밖에 없기 때문에, 그 연결 칸에 간 순간 부터는 큐를 다 초기화 후 2차원 탐색만 진행
'''

'''
로직
미지의 공간 평면도
시간의 벽 단면도 - 5면
0은 빈공간, 1은 장애물 (이동불가), 2는 타임머신 초기 위치
평면도에서는 시간의 벽 위치 3 / 탈출구 4
시간의 벽 -> 미지의 공간 이어지는 곳은 단 하나

0. 평면도, 단면도 관리 
    * 시간의 벽 단면도는 동서남북위 따로 5개의 배열이 들어있는 3차원 배열로 관리
    * 5개의 연결 정확히 해줘야 함 - (0~4 > 동서남북위)
    * 시간의 벽과 평면도의 연결은 단 한군데 이므로 그 칸은 가장 먼저 찾고 어떤 면과 연결되는지 구해놓기
    - 위쪽과 4개 면과의 연결 
        위쪽 첫번째 행 - 북쪽 0번 행과 연결 (이때 열은 거꾸로)
        위쪽 마지막 행 - 남쪽 첫번째 행과 연결
        위쪽 첫번째 열 - 서쪽 첫번째 행과 연결
        위쪽 마지막 열 - 동쪽 0번 행과 연결 (이때 열은 행의 반대)
    - 동쪽과의 연결
        동쪽 첫번째 열 - 남쪽 마지막 열과 연결
        동쪽 마지막 열 - 북쪽 첫번째 열과 연결
    - 서쪽과의 연결
        서쪽 첫번째 열 - 북쪽 마지막 열과 연결
        서쪽 마지막 열 - 남쪽 첫번째 열과 연결

1. 시간의 벽 위치 찾기 (0, 0) 부터 시작해서 3 발견하면 종료
    - 이점이 시간의 벽 좌상단 위치 
2. 평면도와 연결된 시간의 벽 출구 찾기
    - 값이 3인 좌표 찾아서 bfs 탐색 시작
    - 0을 발견하면 바로 그 좌표 저장해서 탐색 종료 - tmp_exit = (,)
    - 해당 0의 좌표에 대하여 동서남북 탐색 후 3 찾기
        - 3이 서쪽에 있으면 동쪽(0) / 3이 동쪽에 있으면 서쪽(1) / 3이 북쪽에 있으면 남쪽(2) / 3이 남쪽에 있으면 북쪽(3) 저장
    
    * 연결된 d 방향의 면은, 마지막 행일 때, 평면도와 닿는 처리 해줘야 함 


---
종료시까지 아래를 반복 

3. 시간 이상 현상 확산
    - 시간 이상 현상 배열에 F개 저장해두기 (현재 좌표, 확산방향, v)
        - 처음 시간 이상 현상은 보드에 5로 두기
    - 각 시간 이상 현상에 대해, 각 v의 배수턴일 때 방향 d로 한칸 씩 확산
    - 동시 진행이니까 현재 배열 깊은 복사해서 모두 진행 후 리턴 
    - 시간 이상 현상은 0인 칸으로만 확산됨 -> 확산 후 마지막 위치를 배열에 업데이트 
        - 확산할 곳에 타임 머신이 있을시 ..? 어케 해야 되지 
    - 업데이트 위치가 보드 밖이면 더이상 확산 X
    * 이때 출구면을 막아버리면 바로 강제종료 

4. 타임머신 이동 
    - 타임머신 초기 위치 저장 후 이동 시작 (초기 위치는 위쪽 면 탐색해서 구해 큐에 넣기)
        - 초기 위치: (좌표, 현재 면) >> 현재 면: 0~5면 벽면도 동서남북위 / 6은 평면도 
    - 빈공간(0)으로만 이동 가능 / 4이면 해당 턴 출력 후 종료
    - 큐에 가장 최근에 이동한 좌표 저장해두기
        - 큐에서 모두 꺼내면서 이동 가능하다면 이동 후 해당 좌표를 다시 큐에 넣어
    - 큐 엠티면 더이상 이동 불가로, -1출력 후 종료 
    
    (벽면도 -> 평면도 이동 처리)
    현재 위치가 동서남북 중 2에서 구한 출구면이고, M-1번째 행일 때, 
        - 동쪽면 이었다면, 행 = 좌상단좌표 + M - 1 - 원래 열 / 열 = 좌상단좌표 + M
        - 서쪽면 이었다면, 행 = 좌상단좌표 + 원래 열 / 열 = 좌상단좌표 - 1
        - 남쪽면 이었다면, 행 = 좌상단좌표 + M / 열 = 좌상단좌표 + 원래 열
        - 북쪽면 이었다면, 행 = 좌상단좌표 - 1 / 열 = 좌상단좌표 + M -1 - 원래열 
    새롭게 구한 좌표가 tmp_exit 이라면, 큐로 이동, 아니면 무시 

'''

'''
메모리 초과 문제 해결
방문처리 제대로 + 3차원과 2차원을 따로 bfs하기!!
3차원 -> 2차원으로 가는 경로는 단 한 곳 밖에 없기 때문에, 그 연결 칸에 간 순간 부터는 큐를 다 초기화 후 2차원 탐색만 진행
'''

from collections import deque
dx = [0, 0, 1, -1] # 동서남북
dy = [1, -1, 0, 0] 

N, M, F = map(int, input().split())
board = [] # 평면도
for _ in range(N) : board.append(list(map(int, input().split())))
cube = [ [] for _ in range(5)] # 시간의 벽
for s in range(5) : 
    for _ in range(M) : 
        cube[s].append(list(map(int, input().split())))

anomaly = [] # 이상 현상 (r, c, d, v)
for _ in range(F) : anomaly.append(list(map(int, input().split())))

top_left = (-1, -1) # 시간의 벽 좌상단 위치
for i in range(N) : 
    if top_left != (-1, -1) : break
    for j in range(N) : 
        if board[i][j] == 3 : 
            top_left = (i, j)
            break

def is_inrange(x, y) : 
    return 0<=x<N and 0<=y<N 

def is_inrange_mini(x, y) : 
    return 0<=x<M and 0<=y<M

'''
 평면도와 연결된 시간의 벽 출구 찾기
'''
que = deque()
sx, sy = top_left
que.append((sx, sy))
visited = [[0 for _ in range(N)] for _ in range(N)]
visited[sx][sy] = 1

tmp_exit = (-1, -1)
while que : 
    x, y = que.popleft()
    for i in range(4) : 
        nx, ny = x + dx[i], y + dy[i]
        if is_inrange(nx, ny) and not visited[nx][ny] : 
            if board[nx][ny] == 3 : 
                que.append((nx, ny)) 
                visited[nx][ny] = 1
            elif board[nx][ny] == 0 : 
                tmp_exit = (nx, ny)
                break
    if tmp_exit != (-1, -1) : break

x, y = tmp_exit
exit_side = -1 # 출구가 있는 면 
for i in range(4) : 
    nx, ny = x + dx[i], y + dy[i]
    if is_inrange(nx, ny) and board[nx][ny] == 3 : 
        if i == 0 : exit_side = 1
        elif i == 1 : exit_side = 0
        elif i == 2 : exit_side = 3
        elif i == 3 : exit_side = 2

'''
시간 이상 현상 확산
'''
def spread_time(time) : 
    new_board = [b[:] for b in board]

    for i in range(F) : 
        r, c, d, v = anomaly[i]
        if time % v != 0 : continue
        if not is_inrange(r, c) : continue
        r, c = r + dx[d], c + dy[d] # 한칸 이동
        anomaly[i] = [r, c, d, v]
        if is_inrange(r, c) and board[r][c] == 0 : 
            new_board[r][c] = 5 
        if (r, c) == tmp_exit : 
            print(-1)
            exit()
    
    return new_board


machine_pos = (-1, -1)
for i in range(M) :  
    if machine_pos != (-1, -1) : break
    for j in range(M) : 
        if cube[4][i][j] == 2 : 
            machine_pos = (i, j) # 초기 타임머신 위치 
            break

'''
타임머신 이동 
'''
# 방문기록
visit_cube = [[[0]*M for _ in range(M)] for _ in range(5)]
visit_board = [[0 for _ in range(N)] for _ in range(N)]

def move_machine(time) : 
    tx, ty = top_left
    new_machine_que = deque()

    while machine_que : 
        x, y, s = machine_que.popleft()
        ex, ey = tmp_exit
            
        if s == 0 : # 동
            for i in range(4) : 
                nx, ny = x + dx[i], y + dy[i]
                if is_inrange_mini(nx, ny) and cube[s][nx][ny] == 0 and not visit_cube[s][nx][ny]:
                    new_machine_que.append((nx, ny, s))
                    visit_cube[s][nx][ny] = 1

                if not is_inrange_mini(nx, ny) : 
                    if nx == -1 : nx, ny, ns = M-1 -y, M-1, 4 # 위쪽으로 이동 
                    elif nx == M : # 탈출면일 때 평면으로 이동 
                        if exit_side != s : continue
                        nx, ny, ns = tx + M-1-y, ty + M, 5
                    elif ny == -1 : nx, ny, ns = x, M-1, 2 # 남쪽으로 이동 
                    elif ny == M : nx, ny, ns = x, 0, 3 # 북쪽으로 이동 

                    if ns < 5 and cube[ns][nx][ny] == 0 and not visit_cube[ns][nx][ny]: new_machine_que.append((nx, ny, ns))
                    elif ns == 5 and board[nx][ny] == 0 and not visit_board[nx][ny]: 
                        visit_board[nx][ny] = 1
                        if (nx, ny) == (ex, ey) : # !!! 
                            new_machine_que = deque()
                            new_machine_que.append((nx, ny, ns))
                            return new_machine_que
                        else : new_machine_que.append((nx, ny, ns))

        elif s == 1 : # 서
            for i in range(4) : 
                nx, ny = x + dx[i], y + dy[i]
                if is_inrange_mini(nx, ny) and cube[s][nx][ny] == 0 and not visit_cube[s][nx][ny]:
                    new_machine_que.append((nx, ny, s))
                    visit_cube[s][nx][ny] = 1

                if not is_inrange_mini(nx, ny) : 
                    if nx == -1 : nx, ny, ns = y, 0, 4 # 위쪽으로 이동 
                    elif nx == M : # 탈출면일 때 평면으로 이동 
                        if exit_side != s : continue
                        nx, ny, ns = tx + y, ty -1, 5
                    elif ny == -1 : nx, ny, ns = x, M-1, 3 # 북쪽으로 이동 
                    elif ny == M : nx, ny, ns = x, 0, 2 # 남쪽으로 이동 

                    if ns < 5 and cube[ns][nx][ny] == 0 and not visit_cube[ns][nx][ny]: new_machine_que.append((nx, ny, ns))
                    elif ns == 5 and board[nx][ny] == 0 and not visit_board[nx][ny]: 
                        visit_board[nx][ny] = 1
                        if (nx, ny) == (ex, ey) : # !!! 
                            new_machine_que = deque()
                            new_machine_que.append((nx, ny, ns))
                            return new_machine_que
                        else : new_machine_que.append((nx, ny, ns))
            
        elif s == 2 : # 남
            for i in range(4) : 
                nx, ny = x + dx[i], y + dy[i]
                if is_inrange_mini(nx, ny) and cube[s][nx][ny] == 0 and not visit_cube[s][nx][ny]:
                    new_machine_que.append((nx, ny, s))
                    visit_cube[s][nx][ny] = 1

                if not is_inrange_mini(nx, ny) : 
                    if nx == -1 : nx, ny, ns = M-1, y, 4 # 위쪽으로 이동 
                    elif nx == M : # 탈출면일 때 평면으로 이동 
                        if exit_side != s : continue
                        # 행 = 좌상단좌표 + M / 열 = 좌상단좌표 + 원래 열
                        nx, ny, ns = tx + M, ty + y, 5
                    elif ny == -1 : nx, ny, ns = x, M-1, 1 # 서쪽으로 이동 
                    elif ny == M : nx, ny, ns = x, 0, 0 # 동쪽으로 이동 

                    if ns < 5 and cube[ns][nx][ny] == 0 and not visit_cube[ns][nx][ny]: new_machine_que.append((nx, ny, ns))
                    elif ns == 5 and board[nx][ny] == 0 and not visit_board[nx][ny]: 
                        visit_board[nx][ny] = 1
                        if (nx, ny) == (ex, ey) : # !!! 
                            new_machine_que = deque()
                            new_machine_que.append((nx, ny, ns))
                            return new_machine_que
                        else : new_machine_que.append((nx, ny, ns))

        elif s == 3 : # 북 
            for i in range(4) : 
                nx, ny = x + dx[i], y + dy[i]
                if is_inrange_mini(nx, ny) and cube[s][nx][ny] == 0 and not visit_cube[s][nx][ny]:
                    new_machine_que.append((nx, ny, s))
                    visit_cube[s][nx][ny] = 1

                if not is_inrange_mini(nx, ny) : 
                    if nx == -1 : nx, ny, ns = 0, M-1 - y, 4 # 위쪽으로 이동 
                    elif nx == M : # 탈출면일 때 평면으로 이동 
                        if exit_side != s : continue
                        nx, ny, ns = tx -1, ty + M-1 -y, 5
                    elif ny == -1 : nx, ny, ns = x, M-1, 0 # 동쪽으로 이동 
                    elif ny == M : nx, ny, ns = x, 0, 1 # 서쪽으로 이동 

                    if ns < 5 and cube[ns][nx][ny] == 0 and not visit_cube[ns][nx][ny]: new_machine_que.append((nx, ny, ns))
                    elif ns == 5 and board[nx][ny] == 0 and not visit_board[nx][ny]: 
                        visit_board[nx][ny] = 1
                        if (nx, ny) == (ex, ey) : # !!! 
                            new_machine_que = deque()
                            new_machine_que.append((nx, ny, ns))
                            return new_machine_que
                        else : new_machine_que.append((nx, ny, ns))

        elif s == 4 : # 위쪽면
            for i in range(4) : 
                nx, ny = x + dx[i], y + dy[i]
                if is_inrange_mini(nx, ny) and cube[s][nx][ny] == 0 and not visit_cube[s][nx][ny]:
                    new_machine_que.append((nx, ny, s))
                    visit_cube[s][nx][ny] = 1

                if not is_inrange_mini(nx, ny) : 
                    if nx == -1 : nx, ny, ns = 0, M-1 -y, 3 # 북쪽으로 이동 
                    elif nx == M : nx, ny, ns = 0, y, 2 # 남쪽으로 이동 
                    elif ny == -1 : nx, ny, ns = 0, x, 1 # 서쪽으로 이동 
                    elif ny == M : nx, ny, ns = 0, M-1-x, 0 # 동쪽으로 이동 
    
                    if ns < 5 and cube[ns][nx][ny] == 0 and not visit_cube[ns][nx][ny]: new_machine_que.append((nx, ny, ns))
                    elif ns == 5 and board[nx][ny] == 0 and not visit_board[nx][ny]: 
                        visit_board[nx][ny] = 1
                        if (nx, ny) == (ex, ey) : # !!! 
                            new_machine_que = deque()
                            new_machine_que.append((nx, ny, ns))
                            return new_machine_que
                        else : new_machine_que.append((nx, ny, ns))

        else : # 평면도 
            for i in range(4) : 
                    nx, ny = x + dx[i], y + dy[i]
                    if is_inrange(nx, ny) :
                        if board[nx][ny] == 0 and not visit_board[nx][ny] : 
                            new_machine_que.append((nx, ny, s))
                            visit_board[nx][ny] = 1
                        if board[nx][ny] == 4 : 
                            print(time)
                            exit()

    if not new_machine_que : 
        print(-1)
        exit()
    
    return new_machine_que
    

### Main ###
t = 1 
machine_que = deque() # 현재 타임머신 좌표들 저장 
tx, ty = machine_pos
machine_que.append((tx, ty, 4))
visit_cube[4][tx][ty] = 1

while True : 
    if t == 1 : 
        for r, c, d, v in anomaly : 
            board[r][c] = 5

    board = spread_time(t) # 3
    machine_que = move_machine(t) # 4
    
    t += 1