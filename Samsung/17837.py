# 새로운 게임 2

"""
로직
0. 보드랑 말 상태 관리
    - board(2차원): 0 흰색, 1 빨간, 2 파란
    - piece_board: 말들이 들어있는 게임판 (따로 관리)
    - info: 말의 좌표와 방향 저장

1. 말이 한칸에 4개 이상 쌓이기 전까지 말을 이동
    - 1번 말부터 순서대로 이동
    이동하려는 칸이 
    1) 흰색인 경우
        - 이동하려는 칸에 말이 있으면 그 위에 올려놓음
        - 이때 이동하려는 말(A) 위에 다른 말이 쌓여있으면, 그 말들도 같이 이동 extend
    2) 빨간색인 경우
        - A번 말과 그 위에 있는 모든 말을 순서 바꿔서 이동시킴
    3) 파란색인 경우 (= 체스판 벗어나는 경우도 이 경우로 침) ***
        - 이동 방향을 반대로 하고 한칸 이동 
        - 이동 방향을 반대로 했는데 또 파란색이면(or 경계 넘어가면) 이동X 가만히
        - *** 방향 바꾸고 나서 이동할 칸이 빨간색이면 거꾸로 넣어야 함!!
    - 말 하나 이동할 때 마다 종료조건 체크 해야 함!! 

2. 게임 종료되는 턴 번호 출력 
    - 1000보다 커지는 순간 -1 출력하고 강제종료
"""
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1] # 우좌상하
dy = [1, -1, 0, 0]

N, K = map(int, input().split())
board = []
for _ in range(N) : board.append(list(map(int, input().split())))
info = [[-1, -1, -1]]

piece_board = [[[] for _ in range(N)] for _ in range(N)]

for k in range(K) : 
    x, y, d = map(int, input().split())
    info.append([x-1, y-1, d-1])
    piece_board[x-1][y-1] = [k+1]

def is_inrange(x, y):
    return 0<= x <N and 0<= y <N

def reverse_dir(direct) :
    if direct == 0: return 1
    if direct == 1 : return 0
    if direct == 2 : return 3
    if direct == 3 : return 2

def move_piece(num) : # A 위에 쌓인 것만 잘라서 이동
    x, y, d = info[num]
    nx, ny = x + dx[d], y + dy[d]
    if not is_inrange(nx, ny): 
        d = reverse_dir(d) # 방향 바꿔 
        info[num][2] = d
        nx, ny = x + dx[d], y + dy[d]
        if not is_inrange(nx, ny) or board[nx][ny] == 2: 
            return piece_board, info # 방향 바꿨는데도 경계 넘어가거나 파란색이면 가만히. 방향만 바꿔둠

    color = board[nx][ny]
    pieces = piece_board[x][y]
    for p in range(len(pieces)) : # A의 인덱스 구하기
        if pieces[p] == num : 
            idx = p
            break
    piece_board[x][y] = pieces[0:idx] # 빼는 것도 해야됨
    
    if color == 0 : piece_board[nx][ny].extend(pieces[idx:])
    elif color == 1 : 
        rev = pieces[idx:]
        piece_board[nx][ny].extend(rev[::-1])

    elif color == 2 : 
        d = reverse_dir(d) # 방향 바꿔 
        info[num][2] = d
        nx, ny = x + dx[d], y + dy[d]
        if not is_inrange(nx, ny) or board[nx][ny] == 2: # 방향 바꿨는데도 경계 넘어가거나 파란색이면 가만히
            piece_board[x][y] = pieces # 이때 아까 뺐던거 다시 넣어주기
            return piece_board, info 

        # 여기서 바꾼 방향으로 이동할 칸의 색상 고려해서, 빨간 색이면 뒤집어서 넣어줘야 함 !! 
        color = board[nx][ny]
        if color == 0 : 
            piece_board[nx][ny].extend(pieces[idx:])
        else : # 빨강 
            rev = pieces[idx:]
            piece_board[nx][ny].extend(rev[::-1])

    # info도 수정해줘야 함. 방향 바꿨다면 그것도 업데이트 해줘야 함 
    for i in pieces[idx:] :
        info[i][0], info[i][1] = nx, ny
    return piece_board, info

for turn in range(1, 1001) :
    for i in range(1, K+1) : 
        piece_board, info = move_piece(i) # 이동
        
        for a in range(N) :# 종료 조건 체크 - 이걸 말이 움직이는 중간중간에 체크를 해줘야 한다
            for b in range(N) :
                if piece_board[a][b] == 0 : continue
                if len(piece_board[a][b]) >= 4 :
                    print(turn)
                    exit()

print(-1)
exit()