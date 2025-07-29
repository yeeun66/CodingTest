# 탈출

'''
로직
. : 빈곳 / * : 물 차있는 곳 / X : 돌 / D : 도착지(굴) / S : 고슴도치 위치 
S가 D에 도착할 때 까지 아래를 반복 
1. 고슴도치 한칸 이동 - move_animal
    - 고슴도치 좌표에 처음에는 첫 좌표만 추가
    - 이동할 칸에 대해 이동 가능하다면 새로운 고슴도치 좌표배열에 좌표 추가. 보드에도 업데이트
        - 이동할 칸이 D이면 시간 출력 후 종료 
        - 다음 이동할 칸이 빈칸이고, 그 빈칸에 대해 상하좌우에 *이 없으면 이동 가능
        - 이동할 칸이 빈칸이 아니거나, 빈칸이더라도 상하좌우에 *이 있다면 이동 불가
    - 새로운 고슴도치 좌표배열 리턴 

2. 물(*) 한칸 씩 확장 
    - 이동할 칸이 빈칸일 때 한칸 확장 가능
    - 이전 보드에 있던 물에 대해, 새로운 보드에 물 추가한 버전으로 새로운 보드 리턴

3. 종료 조건 
    - move_animal 에서 D를 잘 만나서 종료하거나, 
    - move_animal 에서 새로운 좌표가 비어있을 때 (즉, 더이상 고슴도치 이동할 곳이 없으면) 
        - 'KAKTUS' 출력 후 종료
'''

# from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
board = []
for _ in range(r) : board.append(list(map(str, input().strip())))

visited = [[0 for _ in range(c)] for _ in range(r)]
gosem = []
for i in range(r) : 
    if gosem : break
    for j in range(c) : 
        if board[i][j] == 'S' : 
            gosem.append((i, j))
            visited[i][j] = 1
            break

def is_inrange(x, y) : 
    return 0<=x<r and 0<=y<c

def move_animal(sec) : 
    new_gosem  = []
    for x, y in gosem : 
        board[x][y] = '.'
        for i in range(4) : 
            nx, ny = x + dx[i], y + dy[i]
            if is_inrange(nx, ny) and not visited[nx][ny]: 
                if board[nx][ny] == '.' : 
                    poss = True
                    for k in range(4) : # 이동하려는 칸에서 인접한 칸에 물이 있는지 검사
                        cx, cy = nx + dx[k], ny + dy[k]
                        if is_inrange(cx, cy) and board[cx][cy] == '*' : poss = False
                    if poss : 
                        visited[nx][ny] = 1
                        new_gosem.append((nx, ny))
                        board[nx][ny] = 'S'
                elif board[nx][ny] == 'D' : 
                    print(sec)
                    exit()
    
    if not new_gosem : 
        print('KAKTUS')
        exit()
    
    return new_gosem

def move_water() : 
    new_board = [b[:] for b in board]
    
    for i in range(r) : 
        for j in range(c) : 
            if board[i][j] == '*' : 
                for k in range(4) : 
                    nx, ny = i + dx[k], j + dy[k]
                    if is_inrange(nx, ny) and board[nx][ny] == '.' : 
                        new_board[nx][ny] = '*'
    
    return new_board

s = 0
while True : 
    s += 1
    gosem = move_animal(s)
    board = move_water()


