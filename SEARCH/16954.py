# 움직이는 미로 탈출

'''
게임 설명
왼쪽 아래 -> 오른쪽 위 로 이동해야 함 
이 게임판은 1초마다 벽이 아래로 한칸씩 움직임 
욱제는 안움직이거나, 대각선 포함 8방향, 총 9개의 칸으로 이동가능 (벽은 이동 불가)
1초동안 욱제가 먼저 이동 하고 나서, 벽이 움직임 

벽이 움직일 때 욱제 칸으로 가면 더이상 욱제는 이동 못함 
욱제의 캐릭터가 가장 오른쪽 윗 칸으로 이동할 수 있는지 없는지 구해보자 (있으면 1, 없으면 0)

로직
아래를 종료시 까지 반복
1. 욱제 움직임) 초기 (7,7)에 우재 표시 =(u) 
    - 각 초 마다 욱제 9칸으로 움직임 (.인 빈칸으로만 이동 가능, 그리고 방문 안한 칸) 움직인건 board에 2로 표시 
    - 종료 조건: (0, 7) 로 이동 가능하면 1 출력 후 종료 
2. 벽 움직임) 모든 벽(#)에 대해 행 한칸 아래로 이동 -> 보드 업데이트 
    - 이동하려고 할때 .이나 u 로 모두 이동 가능 
3. 마지막 종료 조건
    - 더이상 보드에 u가 없음 (어차피 8*8 이니까 다 탐색해도 될듯) 
    - 그럼 0출력
    
'''

from collections import deque
dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 9칸 이동 
dy = [0, 0, -1, 1, -1, 1, -1, 1]
board = []
for _ in range(8) : board.append(list(map(str, input().strip())))

board[7][0] = 'u'
visited = [[0 for _ in range(8)] for _ in range(8)]
visited[7][0] = 1

def is_inrange(x, y) :
    return 0<=x<8 and 0<=y<8

def move_ukjae() : 
    # 이것도 문제 였음 - 이동할 때 마다 방문처리 초기화 해줘야 함
    # 벽의 이동 때문에 이전에 갔던 곳으로 다시 가야할 수도 있으니까 
    visited = [[0 for _ in range(8)] for _ in range(8)] 
    new_board = [b[:] for b in board]

    for i in range(8) : 
        for j in range(8) : 
            if board[i][j] == 'u' : 
                for d in range(8) :
                    nx, ny = i+dx[d], j+dy[d]
                    if (nx, ny) == (0, 7) :
                        print(1)
                        exit()
                    if is_inrange(nx, ny) and board[nx][ny] == '.' and not visited[nx][ny]: 
                        visited[nx][ny] = 1
                        new_board[nx][ny] = 'u'
    
    return new_board

def move_wall() : # 이게 문제 였음 - 아래에서 거꾸로 해야 함
    new_board = [b[:] for b in board]
    for i in range(7, -1, -1) : 
        for j in range(8) : 
            if board[i][j] == '#' :
                nx, ny = i+1, j
                if is_inrange(nx, ny) : 
                    new_board[i][j] = '.'
                    new_board[nx][ny] = '#' 
    
    return new_board

def check_exit() : 
    for i in range(8) : 
        for j in range(8) : 
            if board[i][j] == 'u' : return True
    
    return False


while True :
    # 각 함수마다 단계별로 수행 잘 되었는지 확인하기
    board = move_ukjae()
    board = move_wall()
    if not check_exit() : 
        print(0)
        exit()
