'''

로직
아래를 k번 반복
1. 도망자 이동 - move_player()
    (1) 술래와의 거리가 3 이하일 때만 이동 (+ 아직 안잡힌 도망자만 이동)
    (2) - 현재 방향으로 1칸 이동(격자 내)
        움직이려는 칸에 술래가 없으면 이동
        - 현재 방향으로 1칸 이동 시 격자 밖 -> 방향 반대로 틀기
        움직이려는 칸에 술래가 없으면 이동
    (3) player 배열에 현재 좌표와 방향 업데이트 
    (4) 보드에는 player의 번호 1~m 업데이트 (움직이기 전은 당연히 0으로 바꿔줘야함)
2. 술래 이동 - move_tagger()
    (1) 위 방향부터 달팽이 모양으로 한칸씩 움직임 (끝에 도달하면 다시 거꾸로 해서 중심으로 이동)
    (2) 술래의 위치는 tagger 에만 업데이트 (보드에 굳이 X)
3. 도망자 잡기 - take_player()
    (1) 술래의 시야(현재 바라보고 있는 방향 기준, 현재칸 포함 3칸)에 있는 도망자 잡기
        - 이 때, 나무와 같이 있는 도망자는 못잡음 
        - 잡힌 도망자는 사라짐 -> player[i] = (-1, -1, -1) 처리 
    (2) 점수 획득
        - 현재 턴(t) * 현재 턴엥서 잡힌 도망자수 만큼 점수 얻음

'''

# !!! 한칸에 도망자 여러 명 있을 수 있는 거 고려 안함
# => 3차원 배열로 한칸에 여러명 들어갈 수 있도록 수정 

dx = [0, 1, 0, -1] # 우 하 좌 상 
dy = [1, 0, -1, 0]

n, m, h, k = map(int, input().split()) # 격자크기, 도망자수, 나무 수, 진행 턴 수
tagger = [(n//2, n//2, 3)] # 술래 초기 위치, 방향 
player = [(-1, -1, -1)] # 0번 player를 가정 (사용 X)
board = [[[0] for _ in range(n)] for _ in range(n)]

for num in range(1, m+1) : 
    x, y, d = map(int, input().split()) # 1은 우좌로 움직 / 2는 하상 으로 움직 
    player.append((x-1, y-1, d-1))
    board[x-1][y-1] = [num]

tree = set()
for _ in range(h) :
    x, y = map(int, input().split())
    tree.add((x-1, y-1))

def is_inrange(x, y) : 
    return 0<=x<n and 0<=y<n 

def move_player() :
    new_board = [[[0] for _ in range(n)] for _ in range(n)]
    
    for i in range(1, m+1) : 
        if player[i][0] == -1 : continue
        sx, sy, _ = tagger[0]
        cx, cy, cd = player[i]
        dist = abs(sx-cx) + abs(sy-cy)
        if dist > 3 : 
            if new_board[cx][cy] == [0] : new_board[cx][cy] = [i]
            else : new_board[cx][cy].append(i)
            continue

        nx, ny = cx + dx[cd], cy + dy[cd] 
        if not is_inrange(nx, ny) : 
            cd = (cd + 2) % 4
            nx, ny = cx + dx[cd], cy + dy[cd] 
        
        if (nx, ny) == (sx, sy) : # 못움직임
            player[i] = (cx, cy, cd)
            if new_board[cx][cy] == [0] : new_board[cx][cy] = [i]
            else : new_board[cx][cy].append(i)

        else : # 이동 가능
            player[i] = (nx, ny, cd)

            if new_board[nx][ny] == [0] : new_board[nx][ny] = [i]
            else : new_board[nx][ny].append(i)
        
    return new_board

cur_direct = 0 # 0은 나가는 방향 / 1은 들어오는 방향 

limit = 1 # 해당 방향으로 가는 칸 수 
tmp_limit = limit

def move_tagger_out() : 
    # 우 -> 하 일 때, 좌 -> 상 일때 마다 방향 변경 
    global cur_direct, limit, tmp_limit
    sx, sy, sd = tagger[0]

    nx, ny = sx + dx[sd], sy + dy[sd]
    if (nx, ny) == (0, 0) : 
        cur_direct = 1
        limit = n-1 # 해당 방향으로 가는 칸 수 
        tmp_limit = limit
        tagger[0] = (0, 0, 1) 
        return 

    tmp_limit -= 1
    if tmp_limit == 0 and sd == 3 : # 상
        sd = 0 
        tmp_limit = limit
    elif tmp_limit == 0 and sd == 0 : # 우
        limit += 1
        tmp_limit = limit
        sd = 1
    elif tmp_limit == 0 and sd == 1 : # 하
        sd = 2 
        tmp_limit = limit
    elif tmp_limit == 0 and sd == 2 : # 좌 
        limit += 1
        tmp_limit = limit
        sd = 3
    
    tagger[0] = (nx, ny, sd) 
    
def move_tagger_in() :
    global cur_direct, limit, tmp_limit
    sx, sy, sd = tagger[0]

    nx, ny = sx + dx[sd], sy + dy[sd]
    if (nx, ny) == (n//2, n//2) : 
        cur_direct = 0
        limit = 1 # 해당 방향으로 가는 칸 수 
        tmp_limit = limit
        tagger[0] = (nx, ny, 3) 
        return 

    tmp_limit -= 1
    if tmp_limit == 0 and sd == 1 and nx == n-1: # 하 인데 첫번째 하 
        sd = 0 
        tmp_limit = limit
    elif tmp_limit == 0 and sd == 1 : # 하 인데 첫번째 아닌 하 
        sd = 0 
        limit -= 1
        tmp_limit = limit
    elif tmp_limit == 0 and sd == 0 : # 우
        tmp_limit = limit
        sd = 3
    elif tmp_limit == 0 and sd == 3 : # 상
        sd = 2 
        limit -= 1
        tmp_limit = limit
    elif tmp_limit == 0 and sd == 2 : # 좌 
        sd = 1
        tmp_limit = limit
    
    tagger[0] = (nx, ny, sd) 

def take_player(turn) : 
    global score 
    nx, ny, sd = tagger[0]
    cnt = 0
    for i in range(3) : 
        if i != 0 : nx, ny = nx + dx[sd], ny + dy[sd]
        if not is_inrange(nx, ny) : break
        if (nx, ny) in tree : continue
        if board[nx][ny] != [0] : 
            cnt += len(board[nx][ny])
            for num in board[nx][ny] : 
                player[num] = (-1, -1, -1)
            board[nx][ny] = [0]
    
    score += cnt * turn

score = 0
for t in range(1, k+1) : 
    board = move_player()
    if cur_direct == 0 : move_tagger_out()
    else : move_tagger_in()
        
    take_player(t)

print(score)