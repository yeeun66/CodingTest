# 주사위 굴리기

# 주사위(dice) 2차원 deque로 상태 관리
    # [deque([-1, 0, -1]), deque([0, 0, 0]), deque([-1, 0, -1]), deque([-1, 0, -1])]
    # 맨 위는 dice[1][1] # 맨 아래는 dice[3][1]
# 1. 주사위 굴리기
    # 명령(동, 서, 북, 남) 대로 주사위 굴렸을 때
        # 지도 범위를 넘어가면 명령 수행X -> continue
        # 범위 이내면, 명령에 맞춰 주사위 굴린다
            # 동쪽 -> 
            #   dice[1].appendleft(dice[3][1])
            #   dice[3][1] = dice[1].pop()
            # 서쪽 -> 
            #   dice[1].append(dice[3][1])
            #   dice[3][1] = dice[1].popleft()
            # 북쪽 -> 
            #   tmp = dice[0][1]
            #   for i in range(1, 4) :
            #       dice[i-1][1] = dice[i][1]
            #   dice[3][1] = tmp 
            # 남쪽 -> 
            #   tmp = dice[3][1]
            #   for i in range(3) :
            #       dice[i+1][1] = dice[i][1]
            #   dice[0][1] = tmp 
# 2. 밑면 값 바꾸기
    # 주사위 굴려진 지도의 위치 값이 0이면, 
        # map[r][c] = dice[3][1] # 지도에 주사위 값 넣기
    # 지도값이 0이 아니면,
        # dice[3][1] = map[r][c] # 주사위 밑면에 지도 값 넣기
        # map[r][c] = 0 # 지도 값은 0이 됨
# 3. 맨 위 값 dice[1][1] 출력

from collections import deque
dice = [deque([-1, 0, -1]), deque([0, 0, 0]), deque([-1, 0, -1]), deque([-1, 0, -1])]

N, M, x, y, K = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]
cmd_list = [int(x) for x in input().split()]

# 동 서 북 남
dx = [0, 0, -1, 1] # 행
dy = [1, -1, 0, 0] # 열

for i in range(K) :
    cmd = cmd_list[i]
    
    nx = x + dx[cmd-1]
    ny = y + dy[cmd-1]
    if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
    # 주사위 굴리기 (전개도)
    if cmd == 1: 
        dice[1].appendleft(dice[3][1])
        dice[3][1] = dice[1].pop()
        
    elif cmd == 2 : 
        dice[1].append(dice[3][1])
        dice[3][1] = dice[1].popleft()
        
    elif cmd == 3 : 
        tmp = dice[0][1]
        for k in range(1, 4) : dice[k-1][1] = dice[k][1]
        dice[3][1] = tmp 
        
    else : 
        tmp = dice[3][1]
        for k in range(2, -1, -1) : dice[k+1][1] = dice[k][1]
        dice[0][1] = tmp 
    
    # 밑면 값, 지도 값 바꾸기
    if map[nx][ny] == 0 : map[nx][ny] = dice[3][1]
    else : 
        dice[3][1] = map[nx][ny] 
        map[nx][ny] = 0
    
    print(dice[1][1])
    x, y = nx, ny # 현재 값 업데이트